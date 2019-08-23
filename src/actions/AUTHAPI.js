import axios from 'axios'
import {API_ROOT_URL} from './config'

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const AUTHAPI = axios.create({
  baseURL: API_ROOT_URL,
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${localStorage.getItem('token')}`
  }
})

AUTHAPI.interceptors.request.use(
  config => {
    config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`
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
    if(error.response.statusText === 'Unauthorized')
      localStorage.removeItem('token');
    return Promise.reject(error.response)
  },
)

export default AUTHAPI
