# 🚀 Domoticz N8N Plugin 


**Integrate N8N workflow automations directly into Domoticz.**
Monitor, control, and embed your N8N workflows seamlessly in your Domoticz setup. ⚡

<img width="800" height="430" alt="image" src="https://github.com/user-attachments/assets/c57829f0-7f42-4b4e-9060-e73308895df3" />

---


## 🛠 Requirements

* 🏠 Domoticz (latest version recommended)
* 🐍 Python 3.x
* 📦 Python `requests` module (`pip3 install requests`)
* 🌐 N8N instance (cloud or self-hosted)
* 🔑 N8N API key

---

## 📥 Installation

1. **Clone the plugin** to your Domoticz plugins directory:

   ```bash
   cd domoticz/plugins
   git clone https://github.com/galadril/Domoticz-N8N-Plugin.git
   ```

2. **Install Python dependencies**:

   ```bash
   pip3 install requests
   ```

3. **Restart Domoticz** 🔄

4. **Add the plugin hardware**:

   * Go to **Setup > Hardware** ⚙️
   * Add new hardware and select **Domoticz N8N Plugin**

---

## ⚙️ Configuration

### 1️⃣ Obtain Your N8N API Key

1. Log in to your N8N instance 🌐
2. Navigate to **Settings > API** 🔧
3. Generate a new API key and copy it 🔑

### 2️⃣ Plugin Settings

* **N8N Host**:

  * Self-hosted: `localhost` or your server IP/hostname 🖥️
  * N8N Cloud: `your-instance.app.n8n.cloud` ☁️

* **Port**:

  * Default self-hosted: `5678` 🔌
  * N8N Cloud: `443` or leave empty 🌐

* **Use HTTPS**: Enable for N8N Cloud or SSL-enabled self-hosted instances 🔒

* **API Key**: Paste your N8N API key here 🔑

* **Install Custom Page**: Enable to embed the N8N dashboard in Domoticz 🖼️

* **Update Interval**: Interval (in seconds) to sync workflow states ⏱️

---

## 🎛 Usage

### 🔄 Workflow Switches

Once configured, each workflow becomes a switch in Domoticz:

* **Turn On** – Activates the workflow in N8N ✅
* **Turn Off** – Deactivates the workflow ❌
* Switch states automatically sync with N8N 🔄

### 🖥️ Custom Dashboard

If "Install Custom Page" is enabled:

* Access via Domoticz menu: **Custom > N8N** 🖱️
* Full N8N interface embedded in Domoticz for direct workflow management 🎛️

---

## 📡 Supported N8N API Endpoints

* `GET /api/v1/workflows` – List all workflows 📜
* `POST /api/v1/workflows/{id}/activate` – Activate a workflow ✅
* `POST /api/v1/workflows/{id}/deactivate` – Deactivate a workflow ❌

---

## ⚠️ Troubleshooting

### 🌐 Connection Issues

* Ensure Domoticz can reach your N8N instance 🖥️
* Verify API key and permissions 🔑
* Check ports for self-hosted instances and firewalls 🔌
* For HTTPS, verify SSL certificates 🔒

### ❌ Devices Not Appearing

* Review Domoticz logs for errors 📄
* Confirm API key has permission to list workflows ✅
* Verify that workflows exist in your N8N instance 📝

### 🐞 Debug Mode

Enable detailed logging:

1. Go to the plugin hardware settings ⚙️
2. Set **Debug** to *Basic Debugging* or higher 🔍
3. Check Domoticz logs for detailed API communication 📜

---

## 🤝 Contributing

Contributions are welcome!
Submit pull requests or open issues for bugs, improvements, and new features 💡

---

## 🔗 Links

* [GitHub Repository](https://github.com/galadril/Domoticz-N8N-Plugin) 🏷️
* [N8N Official Site](https://n8n.io) 🌐
* [Domoticz Home Automation](https://www.domoticz.com) 🏠
