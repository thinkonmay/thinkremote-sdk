import axios from 'axios';
import { FetchOption, FetchResponse, Filter } from './model';

const ANON_KEY = process.env.ANON_KEY ?? "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2bXZ5bWtleGphcnBsYnh3bG5qIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODAzMjM0NjgsImV4cCI6MTk5NTg5OTQ2OH0.y2W9svI_4O4_xd5AQk4S4MLJAvQJIp0QrO4cljLB9Ik"
const PROJECT  = process.env.PROJECT  ?? "avmvymkexjarplbxwlnj"
const API_KEY  = process.env.API_KEY





export class SdkFunction {
	public async FetchWorker(option?: FetchOption): Promise<FetchResponse | Error> {
		const url = `https://${PROJECT}.functions.supabase.co/worker_profile_fetch`
		const res = await axios<any>(url, {
			method: "POST",
			data: option ? {...option, use_case : 'sdk' } : { use_case : 'sdk' },
			headers: {
				'api_key': API_KEY,
				'Authorization': `Bearer ${ANON_KEY}`
			}
		})
		if (res.status != 200) {
			return new Error(`response ${res.statusText} : ${res.data}`)
		}

		return res.data
	}

	public async CreateSession(filter: Filter): Promise<{
		session_id : number
		url        : string
	} | Error> {
		const url = `https://${PROJECT}.functions.supabase.co/worker_session_create`
		const res = await axios<any>( url, {
			method: "POST",
			data: filter,
			headers: {
				'api_key': API_KEY,
				'Authorization': `Bearer ${ANON_KEY}`
			}
		})
		if (res.status != 200) {
			return new Error(res.data)
		}

		return res.data 
	}

	public async DeactivateSession(sessionId: number) : Promise<string | Error>{
		const url = `https://${PROJECT}.functions.supabase.co/worker_session_deactivate`
		const res = await axios( url, {
            method: "POST",
			data: { 
				worker_session_id: sessionId 
			},
			headers: {
				'api_key': API_KEY,
				'Authorization': `Bearer ${ANON_KEY}`
			}
		})

        if(res.status != 200) {
			return new Error(res.data)
        }

		return res.data
	}
}
