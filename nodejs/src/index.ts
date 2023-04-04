
import * as dotenv from 'dotenv';
import {SdkFunction} from './sdk_function';
dotenv.config()


const failed = -1;
const short_task = 0;
const worker_node = 1;

const listCommand = process.argv

listCommand.forEach(async (val, index) => {
	console.log(index + ': ' + val);
	const sdk = new SdkFunction()
	switch (val) {
		case 'vendor': {
			for (let i = index + 1; i <= listCommand.length; i++) {
				switch (listCommand[i]) {
					case 'list-workers': {
						const data = await sdk.fetchWorker()
					}
					case 'create-session': {
						let id = -1
						let soundcard = "Default Audio Render Device"
						let monitor = "Generic PnP Monitor"
						switch (listCommand[i + 1]) {
							case '--worker-id': {
								id = +listCommand[i + 2]
								console.log(id);
							}
							case '--monitor': {
								monitor = listCommand[i + 2]
							}
							case '--soundcard': {
								soundcard = listCommand[i + 2]
							}

						}

						await sdk.CreateSession({
							worker_id: id,
							soudcard_name: soundcard,
							monitor_name: monitor,
						})

					}
					case 'deactivate-session': {
						let id = -1
						if (listCommand[i + 1] === '--session-id') {
							id = +listCommand[i + 2]
						}
						console.log(id);
					}
					default:
						break;
				}
			}
		}
		case '--help': {
			printHelp()
		}

	}
});

function printHelp() {
	console.log("required environment (always): 		")
	console.log(" - PROJECT: project id (ex: \"avmvymkexjarplbxwlnj\")		")
	console.log("")
	console.log("A. CLI to do simple tasks, format: ./daemon.exe proxy current")
	console.log(" -proxy			")
	console.log("    -current              (when) get current proxy account username (generate if none)	")
	console.log("    -reset                (when) get new proxy account	")
	console.log(" -vendor		")
	//console.log("    -keygen               (when) generate api key for vendor	")
	console.log("    -list-workers         (when) list all workers belong to account	")
	console.log("    -create-session       (when) create new worker session	")
	console.log("        --worker-id       (use) daemon vendor create-session --worker-id 12	")
	console.log("        --monior          (use) daemon vendor create-session --monitor \"\\\\.\\DISPLAY1\"	")
	console.log("        --soundcard       (use) daemon vendor create-session --soundcard \"Default Audio Render Device\"     ")
	console.log("    -deactivate-session   (when) deactivate running worker session	")
	console.log("        --session-id      (use) daemon vendor deactivate-session --session-id 12	")
	console.log("")
	console.log("B. Run the worker node   ")
	console.log("     1. ./daemon.exe proxy current  ")
	console.log("     2. run ./scripts/installService.bat as Administrator ")
}