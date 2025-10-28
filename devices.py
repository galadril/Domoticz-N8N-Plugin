"""Device management for N8N plugin"""

import Domoticz


class DeviceManager:
    """Manages Domoticz devices for N8N workflows"""

    def __init__(self):
        self.api = None
        self.device_mapping = {}  # Maps Unit to device info
        self.workflow_to_unit = {}  # Maps workflow ID to device Unit

    def _load_device_mapping(self, devices):
        """Load existing device mappings from Domoticz devices"""
        for unit, device in devices.items():
            if device.DeviceID:
                # DeviceID stores the workflow ID
                workflow_id = device.DeviceID
                self.workflow_to_unit[workflow_id] = unit
                self.device_mapping[unit] = {
                    "device_type": "workflow",
                    "workflow_id": workflow_id,
                }
        Domoticz.Debug(f"Loaded {len(self.device_mapping)} device mappings")

    def get_device_info(self, unit):
        """Get device information for a unit"""
        return self.device_mapping.get(unit)

    def create_workflow_devices(self, workflows, devices):
        """Create Domoticz devices for N8N workflows"""
        for workflow in workflows:
            workflow_id = workflow.get("id")
            workflow_name = workflow.get("name", f"Workflow {workflow_id}")

            if not workflow_id:
                continue

            # Check if device already exists
            if workflow_id in self.workflow_to_unit:
                Domoticz.Debug(f"Device already exists for workflow: {workflow_name}")
                continue

            # Find next available unit
            unit = 1
            while unit in devices:
                unit += 1

            # Create switch device for workflow
            Domoticz.Device(
                Name=workflow_name,
                Unit=unit,
                TypeName="Switch",
                DeviceID=workflow_id,
                Used=1,
            ).Create()

            Domoticz.Log(
                f"Created device for workflow: {workflow_name} (Unit: {unit})"
            )

            # Store mapping
            self.workflow_to_unit[workflow_id] = unit
            self.device_mapping[unit] = {
                "device_type": "workflow",
                "workflow_id": workflow_id,
            }

            # Set initial state
            active = workflow.get("active", False)
            devices[unit].Update(
                nValue=1 if active else 0, sValue="On" if active else "Off"
            )

    def update_workflow_devices(self, workflows, devices):
        """Update workflow devices with current state"""
        for workflow in workflows:
            workflow_id = workflow.get("id")
            active = workflow.get("active", False)

            if workflow_id in self.workflow_to_unit:
                unit = self.workflow_to_unit[workflow_id]
                if unit in devices:
                    current_state = devices[unit].nValue
                    new_state = 1 if active else 0

                    # Only update if state changed
                    if current_state != new_state:
                        devices[unit].Update(
                            nValue=new_state, sValue="On" if active else "Off"
                        )
                        Domoticz.Debug(
                            f"Updated workflow {workflow.get('name')}: {'Active' if active else 'Inactive'}"
                        )
