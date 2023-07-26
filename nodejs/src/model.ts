export interface WorkerProfile {
    proxy_profile_id: number
    worker_profile_id: number
    match_sessions: {
        session_id: number

        worker_session_id: number
        worker_profile_id: number
        account_session_id:  string
        webrtc_config:{
            iceServers: any
        }
        signaling_config: {
            Data: any
            Audio: any
            Video: any
            HostName: string
            ValidationUrl: number
        }

        media_config: {
            monitor: any
            soundcard: any
        }

        auth_config: {
            token: string
        }

        start_at: string
        last_check: string
        metadata: any
        url: string
        

        user_session : {
            user_session_id : number
            user_email : string
            last_check : string
            start_at : string
        }[]
    }[]

    inserted_at: string
    last_check: string
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
        partitions : string[]
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
            Name: string
            DeviceID: string
            pipeline: {
                Plugin: string
                PipelineHash: string
                PipelineString: string
            }
        }[]
    }


 
    metadata: {}
    public_ip: string
    private: string
    
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

