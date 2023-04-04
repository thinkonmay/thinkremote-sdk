import requests, ujson
from utility import utility

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

mySecret = Secret()


class WebRTCController:

    def __init__(self, public_ip="", private_ip=""):
        mySecret = Secret
        Addresses = Address(public_ip, private_ip)
        url = "https://" + utility.get_app_config()["webrtc_service"]["PROJECT"] + ".functions.supabase.co/constant"
        response = requests.post(url=url, 
            timeout=3, 
            verify=False, 
            headers={'Content-type': 'application/json'}).content.decode("utf-8")
        response = ujson.loads(response)
       

        mySecret = response


    def FetchWorker(cred: ApiKey):
        payload = dict(only_active = False)

        url = mySecret['edge_functions']['worker_profile_fetch']


        try:
            response = requests.post(url=url, 
                            data=payload,
                            timeout=3, 
                            verify=False, 
                            headers={"api_key": cred["key"], "Authorization": "Bearer" + mySecret["secret"]["url"] }).content.decode("utf-8")
            response = ujson.loads(response)
        except:
            pass

    Filter = {
        "worker_id": int,
        "monitor_name": str,
        "sound_name": str
    }

    def CreateSession(filter: Filter, cred: ApiKey):
        payload = dict(filter)
        url = mySecret['edge_functions']['worker_session_create']
        try:
            response = requests.post(url=url, 
                            data=payload,
                            timeout=3, 
                            verify=False, 
                            headers={"api_key": cred["key"], "Authorization": "Bearer" + mySecret["secret"]["url"] }).content.decode("utf-8")
        except:
            pass
        return str

    

    def DeactiveSession(self, session_id: str, cred: ApiKey):
        payload = dict(worker_session_id=session_id)
        url = mySecret['edge_functions']['worker_session_deactivate']
        try:
            response = requests.post(url=url, 
                                    data=payload,
                                    timeout=3, 
                                    verify=False, 
                                    headers={"api_key": cred["key"], "Authorization": "Bearer" + mySecret["secret"]["url"] }).content.decode("utf-8")

        except:
            pass

        return True