import { USER } from '../../reducers/type'
import API from '../API'


export const signin = (obj) => {
  return (dispatch) => {
    let data = {
      method: 'POST',
      url: 'api/api-token-auth',
      data: JSON.stringify(obj)
    }
    return API(data).then(res => {
      let user = {username: 'uni', avatar: ''}
      localStorage.setItem('user', JSON.stringify(user));

      return dispatch({ type: USER.SIGNED_IN, payload: user })
    }).catch(err => {
      throw err
    })
  }
}


export const signout = () => {
  return (dispatch) => {
    localStorage.removeItem('user');
    return dispatch({ type: USER.SIGNED_OUT })
  }
}