# Changelog

All notable changes to the Domoticz N8N Plugin will be documented in this file.

## [0.0.1] - 2024-01-XX

### Added
- Initial release of Domoticz N8N Plugin
- N8N API integration with API key authentication
- Automatic device creation for all N8N workflows
- On/Off switches for each workflow in Domoticz
- Activate/Deactivate workflow functionality
- Custom N8N dashboard page embedded in Domoticz
- Support for both N8N Cloud and self-hosted instances
- HTTPS/HTTP connection support
- Configurable update interval
- Debug logging modes
- Automatic workflow state synchronization
- Device persistence across restarts

### Features
- **Workflow Management**: Control N8N workflows directly from Domoticz
- **Real-time Updates**: Automatic synchronization of workflow states
- **Custom Dashboard**: Full N8N interface accessible within Domoticz
- **Flexible Configuration**: Works with cloud and self-hosted N8N instances
- **Easy Setup**: Simple configuration with API key authentication

### Technical Details
- Uses N8N REST API v1
- Python requests library for HTTP communication
- Domoticz plugin framework integration
- Device mapping persistence using DeviceID field
- Configurable HTTPS support for secure connections

### Known Limitations
- Requires Python requests module
- API key must have workflow read/write permissions
- Update interval minimum recommended: 30 seconds
- Custom page requires N8N instance to allow iframe embedding

## [Unreleased]

### Planned Features
- Execute workflow on demand
- Display workflow execution status
- Show last execution time
- Workflow execution history
- Error notifications
- Workflow tags support
- Filter workflows by project
- Webhook integration for real-time updates
- Statistics and metrics display
- Bulk workflow operations

---

## Version Format

This project follows [Semantic Versioning](https://semver.org/):
- MAJOR version for incompatible API changes
- MINOR version for new functionality in a backwards compatible manner
- PATCH version for backwards compatible bug fixes

## Categories

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements
