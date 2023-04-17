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
        self.PROJECT  = os.getenv("PROJECT")
        self.API_KEY  = os.getenv("API_KEY")
        self.ANON_KEY = os.getenv("ANON_KEY")
        

    FetchOption = {
        "wait_for" : {
            "worker" : {
                "public_ip" : str,
                "private_ip" : str
            }
        }
    }

    def FetchWorker(self, option: FetchOption):
        url = "https://" +self.PROJECT + ".functions.supabase.co/worker_profile_fetch"

        body = { "use_case" : "cli" }

        if(option != None):
            body["wait_for"] = option["wait_for"]

        response = requests.post(url=url, 
            data=json.dumps(option),
            timeout=3, 
            verify=True, 
            headers={
                "api_key":self.API_KEY, 
                "Authorization": "Bearer " + self.ANON_KEY
            })

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

        url = "https://" +self.PROJECT + ".functions.supabase.co/worker_session_create"
        response = requests.post(url=url, 
            data=json.dumps(filter),
            timeout=3, 
            verify=True, 
            headers={
                "api_key":self.API_KEY, 
                "Authorization": "Bearer " + self.ANON_KEY
            })

        if (response.status_code != 200):
            return "failed : " + response.content.decode()

        response = json.loads(response.text)
        return response

    

    def DeactiveSession(self, session_id: str):

        url = "https://" +self.PROJECT + ".functions.supabase.co/worker_session_deactivate"
        response = requests.post(url=url, 
            data=json.dumps({ "worker_session_id": session_id }),
            timeout=3, 
            verify=True, 
            headers={
                "api_key":self.API_KEY, 
                "Authorization": "Bearer " + self.ANON_KEY
            })

        if (response.status_code != 200):
            return "failed : " + response.content.decode()

        response = json.loads(response.text)
        return response