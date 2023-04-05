import json
import requests
import os 
ApiKey = {
    "key": str,
    "project": str
}

Account = {
    "username": str,
    "password": str,
    "project": str 
}

Address = {
    "public_ip": str,
    "private_ip": str
}

Secret = {
    'edge_functions' : {
        'user_keygen': '',
        'proxy_register': '',
        'session_authenticate': '',
        'signaling_authenticate': '',
        'turn_register': '',
        'worker_profile_fetch': '',
        'worker_register': '',
        'worker_session_create': '',
        'worker_session_deactivate': '',
    },
    'secret': {
        'anon': '',
        'url': ''
    },
    'google': {
        'client_id': ''
    },
    'conductor': {
        'host': '',
        'grpc_port': ''
    }
}

PROJECT = os.getenv("PROJECT")
API_KEY = os.getenv("API_KEY")

class SdkFunction:
    
    def __init__(self):
        self.mySecret = None
        
    def FetchSecret(self):
        if self.mySecret != None:
            return self.mySecret
        
        self.mySecret = Secret

        url = "https://" + PROJECT + ".functions.supabase.co/constant"
        response = requests.post(url=url, 
            timeout=3, 
            verify=True,
            json=Secret
            )
         
        self.mySecret = json.loads(response.text)
        print("updated secret")

    def FetchWorker(self):
        self.FetchSecret()
        url = self.mySecret["edge_functions"]["worker_profile_fetch"]
        response = requests.post(url=url, 
                        data=json.dumps({ "only_active": False }),
                        timeout=3, 
                        verify=True, 
                        headers={"api_key": API_KEY, "Authorization": "Bearer " + self.mySecret["secret"]["anon"]})
        if (response.status_code != 200):
            return "response "+ response.statusText + " : " + response.data
        response = json.loads(response.text)
        return response

    Filter = {
        "worker_id": int,
        "monitor_name": str,
        "sound_name": str
    }

    def CreateSession(self, filter: Filter):
        payload = dict(filter)
        url = self.mySecret['edge_functions']['worker_session_create']
        response = requests.post(url=url, 
            data=payload,
            timeout=3, 
            verify=True, 
            headers={"api_key": API_KEY, "Authorization": "Bearer " + self.mySecret["secret"]["anon"] })
        if (response.status_code != 200):
            return "response "+ response.statusText + " : " + response.data
        response = json.loads(response.text)
        return response

    

    def DeactiveSession(self, session_id: str):
        self.FetchSecret()
        url = self.mySecret["edge_functions"]["worker_session_deactivate"]
        print(url)
        response = requests.post(url=url, 
            data=json.dumps({ "worker_session_id": session_id }),
            timeout=3, 
            verify=True, 
            headers={"api_key": API_KEY, "Authorization": "Bearer " + self.mySecret["secret"]["anon"] })

        print(response.text)
        if (response.status_code != 200):
            return print("response " + str(response.status_code) + " : " + response.text)
        response = json.loads(response.text)
        return response