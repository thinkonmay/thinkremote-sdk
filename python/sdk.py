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


class SdkFunction:
    def __init__(self):
        self.mySecret = None
        self.PROJECT = os.getenv("PROJECT")
        self.API_KEY = os.getenv("API_KEY")
        
    def FetchSecret(self):
        if self.mySecret != None:
            return self.mySecret

        if self.PROJECT == "" or self.PROJECT == None:
            self.PROJECT = "avmvymkexjarplbxwlnj"
        
        url = "https://" +self.PROJECT + ".functions.supabase.co/constant"
        response = requests.post(url=url, 
                                timeout=3, 
                                verify=True,
                                json=Secret)
         
        self.mySecret = json.loads(response.text)
        print("updated secret")

    def FetchWorker(self):
        self.FetchSecret()

        url = self.mySecret["edge_functions"]["worker_profile_fetch"]
        response = requests.post(url=url, 
                        data=json.dumps({ "only_active": False }),
                        timeout=3, 
                        verify=True, 
                        headers={"api_key":self.API_KEY, "Authorization": "Bearer " + self.mySecret["secret"]["anon"]})

        if (response.status_code != 200):
            return "failed : " + response.content.decode()

        response = json.loads(response.text)
        return response

    Filter = {
        "worker_id": int,
        "monitor_name": str,
        "sound_name": str
    }

    def CreateSession(self, filter: Filter):
        self.FetchSecret()

        url = self.mySecret['edge_functions']['worker_session_create']
        response = requests.post(url=url, 
            data=json.dumps(filter),
            timeout=3, 
            verify=True, 
            headers={"api_key":self.API_KEY, "Authorization": "Bearer " + self.mySecret["secret"]["anon"] })

        if (response.status_code != 200):
            return "failed : " + response.content.decode()

        response = json.loads(response.text)
        return response

    

    def DeactiveSession(self, session_id: str):
        self.FetchSecret()

        url = self.mySecret["edge_functions"]["worker_session_deactivate"]
        response = requests.post(url=url, 
            data=json.dumps({ "worker_session_id": session_id }),
            timeout=3, 
            verify=True, 
            headers={"api_key":self.API_KEY, "Authorization": "Bearer " + self.mySecret["secret"]["anon"] })

        if (response.status_code != 200):
            return "failed : " + response.content.decode()

        response = json.loads(response.text)
        return response