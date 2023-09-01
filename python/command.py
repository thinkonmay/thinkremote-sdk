import json
import sys
import yaml

from sdk import SdkFunction
listCommand = sys.argv


def main():


    if len(listCommand) < 1 or len(listCommand) < 2:
        return
    if listCommand[1] == "vendor":
        sdk = SdkFunction()
        for idx, item in enumerate(listCommand):
            if item == "list-workers": 
                data = sdk.FetchWorker(option=None) # if you want to fetch all active worker
                print(yaml.dump(data))
            elif item == "create-session":
                id = None
                resp = sdk.CreateSession({ "worker_id" : id,
                                            "public_ip": "103.182.163.13",
                                            "private_ip": "192.168.1.116",
                                            "reference_email": "test@gmail.com" })
                print(yaml.dump(resp))
            elif item == "deactivate-session":
                
                id = -1
                if idx + 1 < len(listCommand) and idx + 2 < len(listCommand): 
                    if  listCommand[idx + 1] == '--session-id':
                        id = int(listCommand[idx + 2])
                if id != -1:
                    sdk.DeactiveSession(id)
            elif item == "analytic":
                resp = sdk.FetchAnalytic()
                
                print(yaml.dump(resp))
    elif listCommand[1] == "--help":
        printHelp()


def printHelp():
	print("required environment (always): 		")
	print(" - PROJECT: project id (ex: \"avmvymkexjarplbxwlnj\")		")
	print("")
	print("A. CLI to do simple tasks, format: ./daemon.exe proxy current")
	print(" -vendor		")
	print("    -list-workers         (when) list all workers belong to account	")
	print("    -create-session       (when) create new worker session	")
	print("        --worker-id       (use) daemon vendor create-session --worker-id 12	")
	print("        --monior          (use) daemon vendor create-session --monitor \"\\\\.\\DISPLAY1\"	")
	print("        --soundcard       (use) daemon vendor create-session --soundcard \"Default Audio Render Device\"     ")
	print("    -deactivate-session   (when) deactivate running worker session	")
	print("        --session-id      (use) daemon vendor deactivate-session --session-id 12	")
	print("")
	print("B. Run the worker node   ")
	print("     1. ./daemon.exe proxy current  ")
	print("     2. run ./scripts/installService.bat as Administrator ")

if __name__ == "__main__":
    main()