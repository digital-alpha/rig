
import { USER } from '../type'


let user = JSON.parse(localStorage.getItem('user'));
const initState = user ? { is_authed: true, user } : {};


const AuthReducer = (state = initState, action) => {
  const { type, payload} = action
  
  switch(type){

    case USER.SIGNED_IN:
      return {
        ...state,
        is_authed: true,
        user: payload
      }

    case USER.SIGNED_OUT:
      return {
        ...state,
        is_authed: false
      }

    default:
        return state
  }
}

export default AuthReducer