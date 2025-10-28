# Domoticz N8N Plugin

A Domoticz plugin for monitoring and controlling N8N workflow automations.

## Features

- **Workflow Management**: View and control all your N8N workflows from Domoticz
- **On/Off Switches**: Each workflow gets a switch in Domoticz to activate/deactivate it
- **Custom Dashboard**: Embedded N8N interface accessible from Domoticz
- **Real-time Updates**: Automatically syncs workflow states
- **Cloud & Self-hosted Support**: Works with both N8N Cloud and self-hosted instances

## Requirements

- Domoticz (latest version recommended)
- Python 3.x
- Python `requests` module
- N8N instance (cloud or self-hosted)
- N8N API key

## Installation

1. Clone this repository to your Domoticz plugins directory:
   ```bash
   cd domoticz/plugins
   git clone https://github.com/galadril/Domoticz-N8N-Plugin.git
   ```

2. Install Python dependencies:
   ```bash
   pip3 install requests
```

3. Restart Domoticz

4. Go to **Setup > Hardware** in Domoticz

5. Add new hardware with type "Domoticz N8N Plugin"

## Configuration

### Getting your N8N API Key

1. Log in to your N8N instance
2. Go to **Settings > API**
3. Create a new API key
4. Copy the generated key

### Plugin Settings

- **N8N Host**: 
  - For self-hosted: `localhost` or your server IP/hostname
  - For N8N Cloud: `your-instance.app.n8n.cloud`
  
- **Port**: 
  - Default for self-hosted: `5678`
  - For N8N Cloud: Leave empty or use `443`

- **Use HTTPS**: 
  - Enable for N8N Cloud or if your self-hosted instance uses SSL

- **API Key**: Your N8N API key

- **Install Custom Page**: Enable to embed N8N dashboard in Domoticz

- **Update Interval**: How often to check for workflow state changes (in seconds)

## Usage

### Workflow Switches

After configuration, the plugin will create a switch for each workflow in your N8N instance:

- **Turn On**: Activates the workflow in N8N
- **Turn Off**: Deactivates the workflow in N8N
- The switch state automatically syncs with N8N

### Custom Dashboard

If you enabled "Install Custom Page", access the N8N dashboard through:
- Domoticz menu: **Custom > N8N**
- The embedded interface provides full access to your N8N instance

## Supported N8N API Endpoints

- `GET /api/v1/workflows` - List all workflows
- `POST /api/v1/workflows/{id}/activate` - Activate a workflow
- `POST /api/v1/workflows/{id}/deactivate` - Deactivate a workflow

## Troubleshooting

### Connection Issues

- Verify your N8N instance is accessible from the Domoticz server
- Check the API key is correct and has proper permissions
- For self-hosted instances, ensure the port is correct and not blocked by firewall
- For HTTPS connections, ensure SSL certificates are valid

### Devices Not Appearing

- Check the Domoticz log for errors
- Ensure your API key has permissions to list workflows
- Verify workflows exist in your N8N instance

### Debug Mode

Enable debug logging in the plugin settings to see detailed API communication:
1. Go to plugin hardware settings
2. Set "Debug" to "Basic Debugging" or higher
3. Check Domoticz logs for detailed information

## Development

### Project Structure

```
Domoticz-N8N-Plugin/
??? plugin.py       # Main plugin file
??? api.py             # N8N API client
??? devices.py  # Device management
??? constants.py    # Configuration constants
??? n8n.html          # Custom dashboard page
??? README.md         # This file
```

### Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under the MIT License.

## Credits

- Author: Mark Heinis
- Based on the Domoticz EVCC IO Plugin architecture
- N8N API documentation: https://docs.n8n.io/api/

## Links

- [GitHub Repository](https://github.com/galadril/Domoticz-N8N-Plugin)
- [N8N Official Site](https://n8n.io)
- [Domoticz Home Automation](https://www.domoticz.com)
