"""
<plugin key="Domoticz-N8N-Plugin" name="Domoticz N8N Plugin" author="Mark Heinis" version="0.0.1" wikilink="https://github.com/galadril/Domoticz-N8N-Plugin/wiki" externallink="https://github.com/galadril/Domoticz-N8N-Plugin">
	<description>
        Plugin for retrieving and controlling N8N workflows from Domoticz.
  </description>
	<params>
		<param field="Address" label="N8N Host (e.g., localhost or your-instance.app.n8n.cloud)" width="300px" required="true" default="localhost"/>
		<param field="Port" label="Port" width="30px" required="true" default="5678"/>
		<param field="Mode1" label="Use HTTPS" width="75px">
			<options>
				<option label="Yes" value="true"/>
				<option label="No" value="false" default="true"/>
			</options>
		</param>
		<param field="Password" label="API Key" width="300px" required="true" default="" password="true"/>
		<param field="Mode2" label="Install Custom Page" width="75px">
			<options>
				<option label="Yes" value="true" default="true"/>
				<option label="No" value="false"/>
			</options>
		</param>
		<param field="Mode3" label="Update interval (seconds)" width="30px" required="true" default="60"/>
		<param field="Mode6" label="Debug" width="200px">
			<options>
				<option label="None" value="0" default="true"/>
				<option label="Python Only" value="2"/>
				<option label="Basic Debugging" value="62"/>
				<option label="Basic+Messages" value="126"/>
				<option label="Connections Only" value="16"/>
				<option label="Connections+Queue" value="144"/>
				<option label="All" value="-1"/>
			</options>
		</param>
	</params>
</plugin>
"""

import Domoticz
import os
import traceback
from shutil import copy2

# Import our modules
from api import N8NApi
from devices import DeviceManager
from constants import DEFAULT_UPDATE_INTERVAL


class BasePlugin:
    """Main N8N Plugin class"""

    def __init__(self):
        self.api = None
        self.device_manager = None
        self.run_again =6
        self.update_interval = DEFAULT_UPDATE_INTERVAL
        self.plugin_path = os.path.dirname(os.path.realpath(__file__))
        self.install_custom_page = True
        self.use_https = False

    def _install_custom_page(self):
        """Install the custom N8N dashboard page"""
        if not self.install_custom_page:
            Domoticz.Log(
                "Custom N8N dashboard installation skipped (disabled in settings)"
            )
            return

        html_file = os.path.join(self.plugin_path, "n8n.html")
        target_file = os.path.join("www", "templates", "n8n.html")

        # Update configuration in the HTML file
        with open(html_file, "r") as f:
            content = f.read()

        # Determine protocol
        protocol = "https" if self.use_https else "http"

        # Replace the placeholders
        content = content.replace("{{N8N_PROTOCOL}}", protocol)
        content = content.replace("{{N8N_ADDRESS}}", Parameters["Address"])
        content = content.replace("{{N8N_PORT}}", Parameters["Port"]) 

        # Write to temporary file
        temp_file = os.path.join(self.plugin_path, "n8n_temp.html")
        with open(temp_file, "w") as f:
            f.write(content)

        # Copy to target location
        if os.path.exists(target_file):
            os.remove(target_file)
        copy2(temp_file, target_file)

        # Clean up
        os.remove(temp_file)

        Domoticz.Log("Custom N8N dashboard installed successfully")

    def _remove_custom_page(self):
        """Remove the custom N8N dashboard page"""
        target_file = os.path.join("www", "templates", "n8n.html")
        if os.path.exists(target_file):
            os.remove(target_file)
        Domoticz.Log("Custom N8N dashboard removed")

    def onStart(self):
        Domoticz.Debug("onStart called")

        # Set update interval
        if Parameters["Mode3"] != "":
            self.update_interval = int(Parameters["Mode3"])

        # Set custom page installation preference
        self.install_custom_page = Parameters["Mode2"] == "true"

        # Set HTTPS preference
        self.use_https = Parameters["Mode1"] == "true"

        # Set Debugging
        Domoticz.Debugging(int(Parameters["Mode6"]))

        # Initialize API client
        self.api = N8NApi(
            address=Parameters["Address"],
            port=Parameters["Port"],
            api_key=Parameters["Password"],
            use_https=self.use_https,
        )

        # Initialize device manager
        self.device_manager = DeviceManager()
        self.device_manager.api = self.api

        # Load existing device mappings
        self.device_manager._load_device_mapping(Devices)

        # Fetch initial workflows to create devices
        self._get_initial_workflows()

        # Install custom page if enabled
        if self.install_custom_page:
            self._install_custom_page()

        Domoticz.Heartbeat(10)

    def onStop(self):
        Domoticz.Debug("onStop called")
        if self.install_custom_page:
            self._remove_custom_page()

    def onHeartbeat(self):
        self.run_again -=1
        if self.run_again <=0:
            self.run_again = self.update_interval //10
            self.update_workflows()

    def _get_initial_workflows(self):
        """Fetch initial workflows to create devices"""
        try:
            workflows = self.api.get_workflows()
            if workflows:
                Domoticz.Log(f"Found {len(workflows)} workflows")
                self.device_manager.create_workflow_devices(workflows, Devices)
        except Exception as e:
            Domoticz.Error(f"Error getting initial workflows: {str(e)}")
            Domoticz.Error(traceback.format_exc())

    def update_workflows(self):
        """Update workflow devices with current data"""
        try:
            Domoticz.Debug("Updating workflows")
            workflows = self.api.get_workflows()
            if workflows:
                self.device_manager.update_workflow_devices(workflows, Devices)
        except Exception as e:
            Domoticz.Error(f"Error updating workflows: {str(e)}")
            Domoticz.Error(traceback.format_exc())

    def onCommand(self, Unit, Command, Level, Hue):
        """Handle commands sent to devices"""
        Domoticz.Debug(
            f"onCommand called for Unit: {Unit} Command: {Command} Level: {Level}"
        )

        device_info = self.device_manager.get_device_info(Unit)
        if not device_info:
            Domoticz.Error(f"Unknown device unit: {Unit}")
            return

        device_type = device_info["device_type"]
        workflow_id = device_info["workflow_id"]

        try:
            if device_type == "workflow":
                # Toggle workflow active state
                if Command == "On":
                    if self.api.activate_workflow(workflow_id):
                        Devices[Unit].Update(nValue=1, sValue="On")
                        Domoticz.Log(f"Activated workflow: {Devices[Unit].Name}")
                elif Command == "Off":
                    if self.api.deactivate_workflow(workflow_id):
                        Devices[Unit].Update(nValue=0, sValue="Off")
                        Domoticz.Log(f"Deactivated workflow: {Devices[Unit].Name}")
        except Exception as e:
            Domoticz.Error(f"Error handling command: {str(e)}")
            Domoticz.Error(traceback.format_exc())


# Global plugin instance
_plugin = BasePlugin()


def onStart():
    global _plugin
    _plugin.onStart()


def onStop():
    global _plugin
    _plugin.onStop()


def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()


def onCommand(Unit, Command, Level, Hue):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Hue)
