"""N8N API client"""

import Domoticz
import json
try:
    import requests
except ImportError:
    Domoticz.Error("Python requests module not found. Please install it: pip3 install requests")
    requests = None

class N8NApi:
    """Client for N8N API"""
    
    def __init__(self, address, port, api_key, use_https=False):
        self.address = address
        self.port = port
        self.api_key = api_key
        self.use_https = use_https
        self.protocol = "https" if use_https else "http"
    
        # Build base URL
        if self.port and self.port != "":
  self.base_url = f"{self.protocol}://{self.address}:{self.port}/api/v1"
   else:
            # For cloud instances, no port needed
     self.base_url = f"{self.protocol}://{self.address}/api/v1"
   
        Domoticz.Debug(f"N8N API initialized with base URL: {self.base_url}")
    
    def _get_headers(self):
 """Get headers for API requests"""
        return {
            'accept': 'application/json',
   'X-N8N-API-KEY': self.api_key
        }
    
    def _make_request(self, method, endpoint, data=None, params=None):
        """Make an API request"""
        if not requests:
            Domoticz.Error("requests module not available")
          return None
    
        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers()
        
      try:
      Domoticz.Debug(f"Making {method} request to: {url}")
    
            if method == "GET":
         response = requests.get(url, headers=headers, params=params, timeout=10)
     elif method == "POST":
          response = requests.post(url, headers=headers, json=data, timeout=10)
            elif method == "PUT":
                response = requests.put(url, headers=headers, json=data, timeout=10)
            elif method == "DELETE":
       response = requests.delete(url, headers=headers, timeout=10)
      else:
    Domoticz.Error(f"Unsupported HTTP method: {method}")
     return None
    
            if response.status_code == 200:
            return response.json()
  elif response.status_code == 401:
        Domoticz.Error("Authentication failed. Check your API key.")
       return None
          else:
          Domoticz.Error(f"API request failed with status {response.status_code}: {response.text}")
         return None
         
      except requests.exceptions.Timeout:
        Domoticz.Error(f"Request to {url} timed out")
      return None
        except requests.exceptions.ConnectionError:
            Domoticz.Error(f"Could not connect to {url}")
       return None
     except Exception as e:
            Domoticz.Error(f"Error making API request: {str(e)}")
     return None
    
    def get_workflows(self, active=None, limit=100):
        """Get all workflows"""
        params = {
     'limit': limit
        }
 
        if active is not None:
            params['active'] = 'true' if active else 'false'
        
   result = self._make_request("GET", "/workflows", params=params)
        
        if result and 'data' in result:
     workflows = result['data']
    Domoticz.Debug(f"Retrieved {len(workflows)} workflows")
            return workflows
        
        return []
    
    def get_workflow(self, workflow_id):
        """Get a specific workflow by ID"""
        return self._make_request("GET", f"/workflows/{workflow_id}")
    
    def activate_workflow(self, workflow_id):
  """Activate a workflow"""
  Domoticz.Debug(f"Activating workflow: {workflow_id}")
    result = self._make_request("POST", f"/workflows/{workflow_id}/activate")
        return result is not None
    
 def deactivate_workflow(self, workflow_id):
        """Deactivate a workflow"""
        Domoticz.Debug(f"Deactivating workflow: {workflow_id}")
        result = self._make_request("POST", f"/workflows/{workflow_id}/deactivate")
        return result is not None
