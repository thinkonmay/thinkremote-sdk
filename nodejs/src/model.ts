export interface WorkerProfile {
    id: 18
    account_id: string
    inserted_at: string
    last_check: string

    match_sessions: {
        id: number
        worker_profile_id: number
        manifest: {
            fail_count: number
            hid_port: number
            hid_process_id: number
            hub_process_id: number
        }
        signaling_config: {
            HostName: string
            SignalingPort: number
            WebsocketURL: string
        }
        webrtc_config:{
            iceServers: any
        }
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

export interface Secret {
    edge_functions: {
        user_keygen: string
        proxy_register: string
        session_authenticate: string
        signaling_authenticate: string
        turn_register: string
        worker_profile_fetch: string
        worker_register: string
        worker_session_create: string
        worker_session_deactivate: string
    }
    secret: {
        anon: string
        url: string
    }
    google: {
        client_id: string
    }
    conductor: {
        host: string
        grpc_port: number
    }
}


export interface FetchResponse {
    active: WorkerProfile[]
    unactive: WorkerProfile[]
}

