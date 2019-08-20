import React from 'react'
import { Form, Icon, Input, Button, Row} from 'antd';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import {
  signin
} from '../../actions/auth'
import DocEditForm from "../../components/Form/DocEditForm";


class DocumentDetail extends React.Component {
  state = {
    docVisible: true,
    formVisible: true
  };

  changeDocView = () => {
  	if(this.state.formVisible) 
  		this.setState({docVisible: !this.state.docVisible})
  }

  changeFormView = () => {
  	if(this.state.docVisible) 
  		this.setState({formVisible: !this.state.formVisible})
  }

  render() {
    return (
      <div>
      	<Row type="flex" align="middle" justify="space-between">
	      	<h1>Edit Document</h1>
	      	<div className="toggle-view">
	      	View:&nbsp;&nbsp;
	      		<Button.Group>
		      		<Button type={this.state.docVisible?'primary':'light'} icon="file-text" onClick={this.changeDocView}/>
		      		<Button type={this.state.formVisible?'primary':'light'}  icon="form" onClick={this.changeFormView}/>
		      	</Button.Group>
	      	</div>
	    </Row>
      	<DocEditForm docVisible={this.state.docVisible} formVisible={this.state.formVisible}/>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  auth: state.auth
});

const mapDispatchToProps = dispatch => bindActionCreators({
  signin
}, dispatch);


export default connect(mapStateToProps, mapDispatchToProps)(DocumentDetail)