import { DOCUMENT } from '../../reducers/type'
import AUTHAPI from '../AUTHAPI'
import moment from 'moment';
import { message } from 'antd'


export const getUploadedDocuments = () => {
  return (dispatch) => {
    let data = {
      method: 'get',
      url: 'api/document/',
    }

    return AUTHAPI(data).then(res => {
      res.data = res.data.map((obj, index) => {
        return {
          'key': index,
          'title': obj['file'].split('/')[obj['file'].split('/').length - 1],
          'id': obj['id'],
          'upload_date': moment(new Date(obj['uploaded_at'])).format('lll'),
          'author': obj['uploaded_by'],
          'process_date': '',
        }
      })
      return dispatch({ type: DOCUMENT.DOC_ALL, payload: res.data })
    }).catch(err => {
      throw err
    })
  }
}


export const getDetailDocument = (doc_id) => {
  return (dispatch) => {
    let data = {
      method: 'get',
      url: 'api/detail/' + doc_id,
    }

    return AUTHAPI(data).then(res => {
      return dispatch({ type: DOCUMENT.DETAIL_INFO, payload: res.data[0] })
    }).catch(err => {
      throw err
    })
  }
}


export const saveToCSV = () => {  
  return (dispatch) => {
    let data = {
      method: 'POST',
      url: 'UploadMulti/csv/'
    }

    return AUTHAPI(data).then(res => {
      
    }).catch(err => {
      throw err
    })
  }
}

export const clearDB = () => {
  return (dispatch) => {
    let data = {
      method: 'GET',
      url: 'api/clear/'
    }

    return AUTHAPI(data).then(res => {
      message.success('Database is cleared successfully!');
      return dispatch({ type: DOCUMENT.DOC_ALL, payload: []})
    }).catch(err => {
      throw err
    })
  }
}


export const deleteDocument = (doc_id) => {
  return (dispatch) => {
    let data = {
      method: 'GET',
      url: 'api/clear/'+doc_id
    }

    return AUTHAPI(data).then(res => {
      message.success('Document is deleted successfully!');
      return dispatch({ type: DOCUMENT.DOC_DELETED, payload: {'doc_id': doc_id}})
    }).catch(err => {
      throw err
    })
  }
}

export const processDocument = () => {
  return (dispatch) => {
    let data = {
      method: 'GET',
      url: 'api/process/'
    }

    return AUTHAPI(data).then(res => {
      message.success('Documents are processed successfully!');
      
    }).catch(err => {
      throw err
    })
  }
}
