import json
import requests
import os 

class SdkFunction:
    def __init__(self):
        self.PROJECT  = os.getenv("PROJECT")
        self.API_KEY  = os.getenv("API_KEY")
        self.ANON_KEY = os.getenv("ANON_KEY")
        
        if self.PROJECT == None:
            self.PROJECT = "avmvymkexjarplbxwlnj"
        if self.ANON_KEY == None:
            self.ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2bXZ5bWtleGphcnBsYnh3bG5qIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODAzMjM0NjgsImV4cCI6MTk5NTg5OTQ2OH0.y2W9svI_4O4_xd5AQk4S4MLJAvQJIp0QrO4cljLB9Ik"
        if self.API_KEY == None:
            raise Exception("None apikey provided")

    WaitOption = {
        "wait_for" : {
            "worker" : {
                "public_ip" : str,
                "private_ip" : str
            }
        }
    }

    def FetchWorker(self, option: WaitOption):
        url = "https://" +self.PROJECT + ".functions.supabase.co/worker_profile_fetch"

        body = { "use_case" : "sdk" }
        timeout = 3 * 10

        if(option != None):
            body["wait_for"] = option["wait_for"]
            timeout = 3 * 60

        response = requests.post(url=url, 
            data=json.dumps(body),
            timeout=timeout, 
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

        "private_ip": str,
        "public_ip": str,

        "reference_email": int,

        "monitor_name": str,
        "sound_name": str
    }

    def CreateSession(self, filter: Filter):
        body = {}
        if filter["worker_id"] != None:
            body["worker_id"] = filter["worker_id"]
        elif filter["private_ip"] != None and filter["public_ip"] != None:
            body["public_ip"] = filter["public_ip"]
            body["private_ip"] = filter["private_ip"]
        else:
            raise Exception("worker_ip or worker_id field is required")
        
        if filter["reference_email"] != None:
            body["reference_email"] = filter["reference_email"]


        url = "https://" +self.PROJECT + ".functions.supabase.co/worker_session_create"
        response = requests.post(url=url, 
            data=json.dumps(body),
            timeout=60, 
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
            timeout=60, 
            verify=True, 
            headers={
                "api_key":self.API_KEY, 
                "Authorization": "Bearer " + self.ANON_KEY
            })

        if (response.status_code != 200):
            return "failed : " + response.content.decode()

        response = json.loads(response.text)
        return response