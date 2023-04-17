import axios from 'axios';
import { FetchOption, FetchResponse, Filter, Secret } from './model';

const ANON_KEY = process.env.ANON_KEY ?? "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpwYWdxd2dyenF4b3lkZXpneGtoIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODExODI5OTIsImV4cCI6MTk5Njc1ODk5Mn0.GAqX45RRsQ8TIoBokIbtgODXjbB3LU_yX9Nkihz_f68"
const PROJECT  = process.env.PROJECT  ?? "zpagqwgrzqxoydezgxkh"
const API_KEY  = process.env.API_KEY





export class SdkFunction {
	public async FetchWorker(option?: FetchOption): Promise<FetchResponse | Error> {
		const url = `https://${PROJECT}.functions.supabase.co/worker_profile_fetch`
		const res = await axios<any>(url, {
			method: "POST",
			data: option ? {...option, use_case : 'cli' } : { use_case : 'cli' },
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
