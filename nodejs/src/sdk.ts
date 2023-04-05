import axios, { AxiosResponse } from 'axios';
import { FetchResponse, Filter, Secret, WorkerProfile } from './model';

const PROJECT = process.env.PROJECT
const API_KEY = process.env.API_KEY


export class SdkFunction {
	secret: Secret | null;

	constructor() {
		this.secret = null
	}

	async fetchSecret() {
		if (this.secret != null) {
			return
		}

		const res = await axios<Secret>(`https://${PROJECT}.functions.supabase.co/constant`, {
			method: "POST",
			data: JSON.stringify({}) as string
		})

		this.secret = res.data 
		console.log('updated secret')
	}

	async fetchWorker(): Promise<FetchResponse | Error> {
		await this.fetchSecret()

		const url = this.secret.edge_functions.worker_profile_fetch
		const res = await axios<any>(url, {
			method: "POST",
			data: {only_active:false},
			headers: {
				'api_key': API_KEY,
				'Authorization': `Bearer ${this.secret.secret.anon}`
			}
		})
		if (res.status != 200) {
			return new Error(`response ${res.statusText} : ${res.data}`)
		}

		return res.data
	}

	async CreateSession(filter: Filter): Promise<{
		session_id : number
		url        : string
	} | Error> {
		await this.fetchSecret()

		const url = this.secret.edge_functions.worker_session_create
		const res = await axios<any>({
			url,
			method: "POST",
			data: filter,
			headers: {
				'api_key': API_KEY,
				'Authorization': `Bearer ${this.secret.secret.anon}`
			}
		})
		if (res.status != 200) {
			return new Error(res.data)
		}

		return res.data 
	}

	async DeactivateSession(sessionId: number) : Promise<string | Error>{
		await this.fetchSecret()

		const body = { worker_session_id: sessionId }

		const url = this.secret.edge_functions.worker_session_deactivate
		const res = await axios({
			url,
            method: "POST",
			data: body,
			headers: {
				'api_key': API_KEY,
				'Authorization': `Bearer ${this.secret.secret.anon}`
			}
		})

        if(res.status != 200) {
			return new Error(res.data)
        }

		return res.data
	}
}
