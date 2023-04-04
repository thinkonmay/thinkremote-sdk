import axios, { AxiosResponse } from 'axios';

interface WorkerProfile {
	name: string
}

interface Filter {
	worker_id: number
	monitor_name: string
	soudcard_name: string
}

interface Secret {
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



const SUPABASE_URL = process.env.SUPABASE_URL
const SUPABASE_TOKEN = process.env.SUPABASE_TOKEN
const API_KEY = process.env.API_KEY
const SUPABASE_ANON_KEY = process.env.SUPABASE_ANON_KEY
const url = "http://example.com/movies.json"

var secret: Secret[];

export class SdkFunction {
	data: WorkerProfile[]
	constructor() {
		this.data = []
		this.fetchWorker()
	}



	async fetchWorker(): Promise<WorkerProfile[]> {

		const body = { only_active: false }

		const res = await axios('https://jsonplaceholder.typicode.com/users', {
			method: "GET",
			//body: JSON.stringify(body),
			//headers: {
			//	'api_key': API_KEY,
			//	'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
			//}
		})
		const dataParse = await res.data
		this.data = dataParse as WorkerProfile[]
		return this.data
	}

	async CreateSession(filter: Filter): Promise<WorkerProfile> {

		const res = await axios({
			url,
			method: "POST",
			data: filter,
			headers: {
				'api_key': API_KEY,
				'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
			}
		})
		const dataParse = await res.data()
		return dataParse as WorkerProfile
	}

	async DeactivateSession(sessionId: number) {
		const body = { worker_session_id: sessionId }

		const res = await axios({
			// secret.edge_functions.worker_session_deactivate,
            method: "POST",
			data: body,
			headers: {
				'api_key': API_KEY,
				'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
			}
		})
		const dataParse = await res.data() as AxiosResponse
		
        if(dataParse.status == 200) {

        }

	}
}
