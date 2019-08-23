import { USER } from '../../reducers/type'
import API from '../API'
import AUTHAPI from '../AUTHAPI'
import { message } from 'antd'

export const signin = (obj) => {
  return (dispatch) => {
    let data = {
      method: 'POST',
      url: 'api/api-token-auth/',
      data: JSON.stringify(obj)
    }
    return API(data).then(res => {
      localStorage.setItem('token', res.data.token);

      return dispatch({ type: USER.SIGNED_IN, payload: res.data.username })
    }).catch(err => {
      message.error('Wrong ID or Password!');
      throw err
    })
  }
}


export const currentUser = (obj) => {
  return (dispatch) => {
    let data = {
      method: 'GET',
      url: 'api/current_user/',
      data: JSON.stringify(obj)
    }
    return AUTHAPI(data).then(res => {
      return dispatch({ type: USER.SIGNED_IN, payload: res.data.username })
    }).catch(err => {
      return dispatch({ type: USER.SIGNED_OUT })
    })
  }
}



export const signout = () => {
  return (dispatch) => {
    localStorage.removeItem('token');
    return dispatch({ type: USER.SIGNED_OUT })
  }
}