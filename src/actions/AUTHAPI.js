import axios from 'axios'
import config from './config'

const AUTHAPI = axios.create({
  baseURL: config.API_ROOT_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

AUTHAPI.interceptors.request.use(
  config => {
    config.headers.Authorization = `${window.localStorage.getItem('tokenType')} 
                  ${window.localStorage.getItem('accessToken')}`
    return config
  },
  error => {
    return Promise.reject(error.response)
  },
)

AUTHAPI.interceptors.response.use(
  response => {
    return response
  },
  error => {
    return Promise.reject(error.response)
  },
)

export default AUTHAPI
