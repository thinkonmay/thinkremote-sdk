export interface WorkerProfile {
    id: 18
    account_id: string
    inserted_at: string
    last_check: string

    match_sessions: {
        id: number
        worker_profile_id: number
        signaling_config: {
            HostName: string
            SignalingPort: number
            WebsocketURL: string
        }
        webrtc_config:{
            iceServers: any
        }

        user_session : {
            user_session_id : number
            user_email : string
            last_check : string
            start_at : string
        }[]
    }[]

    hardware: {
        BIOS       : string
        CPU        : string
        Disks      : string[]
        GPUs       : string[]
        Hostname   : string
        NICs       : string[]
        PrivateIP  : string
        PublicIP   : string
        RAM        : string
        timestamp  : string
    }
    media_device: {
        monitors: {
              Adapter: string
              DeviceName: string
              MonitorName: string
              Framerate: number
              Height: number
              MonitorHandle: number
              Width: number
              IsPrimary: boolean
        }[],
        soundcards: {
            Api: string
            DeviceID: string
            Name: string
            IsDefault: boolean
            IsLoopback: boolean
        }[]
        timestamp: string
    }
}

export interface Filter {
	worker_id: number
	monitor_name: string
	soudcard_name: string
}

export type FetchOption = {
	wait_for : {
		worker : {
			public_ip  : string
			private_ip : string
		}
	}
}


export type FetchResponse = {
    active: WorkerProfile[]
} | {
    target: WorkerProfile
}

