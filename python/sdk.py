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
    "edge_functions" : {
        "user_keygen": str,
        "proxy_register": str,
        "session_authenticate": str,
        "signaling_authenticate": str,
        "turn_register": str,
        "worker_profile_fetch": str,
        "worker_register": str,
        "worker_session_create": str,
        "worker_session_deactivate": str,
    },
    "secret": {
        "anon": str,
        "url": str
    },
    "google": {
        "client_id": str
    },
    "conductor": {
        "host": str,
        "grpc_port": int
    }
}

PROJECT = os.getenv("PROJECT")
API_KEY = os.getenv("API_KEY")

class SdkFunction:
    
    def __init__(self):
        self.mySecret = None
        
    @staticmethod
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
        self.FetchSecret(self)
        payload = { "only_active": False }

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
        try:
            response = requests.post(url=url, 
                            data=payload,
                            timeout=3, 
                            verify=True, 
                            headers={"api_key": API_KEY, "Authorization": "Bearer" + self.mySecret["secret"]["anon"] }).content.decode("utf-8")
        except:
            pass
        return str

    

    def DeactiveSession(self, session_id: str, cred: ApiKey):
        payload = dict(worker_session_id=session_id)
        url = self.mySecret['edge_functions']['worker_session_deactivate']
        try:
            response = requests.post(url=url, 
                                    data=payload,
                                    timeout=3, 
                                    verify=False, 
                                    headers={"api_key": API_KEY, "Authorization": "Bearer" + self.mySecret["secret"]["url"] }).content.decode("utf-8")

        except:
            pass

        return True