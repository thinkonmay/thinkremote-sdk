import json
import sys

from sdk import SdkFunction
listCommand = sys.argv


def main():

    sdk = SdkFunction()
    if listCommand[1] == "vendor":
        for idx, item in enumerate(listCommand):
            if item == "list-workers": 
                data =  sdk.FetchWorker()
                print(json.dumps(data, separators=(',',':')))
            elif item == "create-session":
                id = -1
                soundcard = "Default Audio Render Device"
                monitor = "Generic PnP Monitor"
                if (listCommand[idx + 1] == "--worker-id"):
                    id = +listCommand[idx + 2]
                    print(id)
                elif listCommand[idx+1] == "--monitor":
                    monitor = listCommand[idx + 2]
                elif listCommand[idx+1] == "--soundcard":
                    soundcard = listCommand[idx + 2]

                sdk.CreateSession(id, soundcard, monitor)
            elif item == "deactivate-session":
                id = -1
                if idx + 1 < len(listCommand) and idx + 2 < len(listCommand): 
                    if  listCommand[idx + 1] == '--session-id':
                        id = int(listCommand[idx + 2])
                    print(id)
    elif listCommand[1] == "--help":
        printHelp()


def printHelp():
	print("required environment (always): 		")
	print(" - PROJECT: project id (ex: \"avmvymkexjarplbxwlnj\")		")
	print("")
	print("A. CLI to do simple tasks, format: ./daemon.exe proxy current")
	print(" -proxy			")
	print("    -current              (when) get current proxy account username (generate if none)	")
	print("    -reset                (when) get new proxy account	")
	print(" -vendor		")
	# print("    -keygen               (when) generate api key for vendor	")
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