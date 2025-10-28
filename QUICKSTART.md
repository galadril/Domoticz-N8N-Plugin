# Quick Start Guide - Domoticz N8N Plugin

## Step 1: Get Your N8N API Key

### For N8N Cloud:
1. Login to your N8N instance at `https://your-instance.app.n8n.cloud`
2. Click on **Settings** (gear icon in bottom left)
3. Navigate to **API** section
4. Click **Create API Key**
5. Give it a name (e.g., "Domoticz Integration")
6. Copy the generated API key - **you won't be able to see it again!**

### For Self-Hosted N8N:
1. Login to your N8N instance (e.g., `http://localhost:5678`)
2. Click on **Settings** (gear icon in bottom left)
3. Navigate to **API** section
4. Click **Create API Key**
5. Give it a name (e.g., "Domoticz Integration")
6. Copy the generated API key

## Step 2: Install the Plugin

### Option A: Git Clone (Recommended)
```bash
cd /home/pi/domoticz/plugins
# Or on Windows: cd C:\Program Files\Domoticz\plugins
git clone https://github.com/galadril/Domoticz-N8N-Plugin.git
```

### Option B: Manual Download
1. Download the plugin from GitHub as ZIP
2. Extract to your Domoticz plugins folder
3. Ensure the folder is named `Domoticz-N8N-Plugin`

## Step 3: Install Dependencies

### Linux/Raspberry Pi:
```bash
sudo pip3 install -r /home/pi/domoticz/plugins/Domoticz-N8N-Plugin/requirements.txt
```

### Windows:
```powershell
pip install -r "C:\Program Files\Domoticz\plugins\Domoticz-N8N-Plugin\requirements.txt"
```

## Step 4: Restart Domoticz

### Linux/Raspberry Pi:
```bash
sudo service domoticz restart
# Or
sudo systemctl restart domoticz
```

### Windows:
- Restart the Domoticz service from Services app
- Or restart Domoticz application

## Step 5: Add Hardware in Domoticz

1. Open Domoticz web interface
2. Go to **Setup** ? **Hardware**
3. Click **Add** at the bottom
4. Fill in the settings:

### Configuration Examples:

#### For N8N Cloud:
- **Name**: N8N Workflows
- **Type**: Domoticz N8N Plugin
- **N8N Host**: `your-instance.app.n8n.cloud` (without https://)
- **Port**: *(leave empty or 443)*
- **Use HTTPS**: Yes
- **API Key**: *(paste your API key)*
- **Install Custom Page**: Yes
- **Update Interval**: 60

#### For Self-Hosted N8N:
- **Name**: N8N Workflows
- **Type**: Domoticz N8N Plugin
- **N8N Host**: `localhost` (or your server IP)
- **Port**: `5678`
- **Use HTTPS**: No (unless you configured SSL)
- **API Key**: *(paste your API key)*
- **Install Custom Page**: Yes
- **Update Interval**: 60

5. Click **Add**

## Step 6: Verify Installation

1. Go to **Setup** ? **Devices**
2. You should see switches for each N8N workflow
3. Click the green arrow (?) to add workflows to your dashboard
4. The custom N8N page should appear in **Custom** ? **N8N** menu

## Step 7: Use Your Workflows

### Control Workflows:
- **Turn On**: Click the switch to activate the workflow in N8N
- **Turn Off**: Click again to deactivate the workflow
- Changes sync automatically between Domoticz and N8N

### Access N8N Dashboard:
- Click **Custom** in the Domoticz menu
- Select **N8N**
- Full N8N interface loads in Domoticz

## Troubleshooting

### Problem: No devices appear
**Solution**: 
- Check Domoticz logs for errors
- Verify API key is correct
- Ensure N8N is accessible from Domoticz server

### Problem: "Authentication failed" error
**Solution**:
- Re-check your API key
- Create a new API key in N8N
- Update the hardware configuration with the new key

### Problem: Cannot connect to N8N
**Solution**:
- Verify host and port are correct
- Check HTTPS setting matches your setup
- Test connection: `curl http://your-host:5678` or `ping your-host`
- Check firewall settings

### Problem: Custom page doesn't load
**Solution**:
- Check if N8N allows embedding (some instances block iframes)
- Verify the URL in the HTML matches your N8N instance
- Try accessing N8N directly in a browser first

### Enable Debug Logging:
1. Go to **Setup** ? **Hardware**
2. Edit the N8N Plugin
3. Set **Debug** to "Basic Debugging"
4. Check logs at **Setup** ? **Log**

## Example Use Cases

1. **Scene Automation**: Create Domoticz scenes that trigger when workflows activate
2. **Notifications**: Get notified when specific workflows start/stop
3. **Scheduling**: Use Domoticz's scheduler to activate/deactivate workflows
4. **Monitoring**: Track workflow states on your Domoticz dashboard
5. **Integration**: Combine N8N automations with other Domoticz devices

## API Rate Limits

N8N API has rate limits:
- Default update interval of 60 seconds is recommended
- For high-frequency updates, consider 30 seconds minimum
- Cloud instances may have stricter limits

## Next Steps

- Explore the N8N dashboard within Domoticz
- Create scenes using workflow switches
- Set up notifications for workflow state changes
- Combine with other Domoticz automation

## Need Help?

- GitHub Issues: https://github.com/galadril/Domoticz-N8N-Plugin/issues
- N8N Documentation: https://docs.n8n.io
- Domoticz Forum: https://www.domoticz.com/forum/

Enjoy your N8N integration with Domoticz! ??
