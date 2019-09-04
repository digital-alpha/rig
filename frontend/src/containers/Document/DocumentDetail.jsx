import React from 'react'
import { Button, Row, Icon} from 'antd';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import {
  getDetailDocument,
  updateDetailInfo
} from '../../actions/document'
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

  componentWillMount(){
    this.props.getDetailDocument(this.props.match.params.id)
  }

  render() {

    return (
      <div>
      	<Row type="flex" align="middle">
	      	<h1>Edit Document</h1>
	      	<div className="toggle-view" style={{margin: '0 auto'}}>
            
	      		<Button.Group style={{marginLeft: '-65px'}}>
              View:&nbsp;&nbsp;
		      		<Button type={this.state.docVisible?'primary':'light'} icon="file-text" onClick={this.changeDocView}/>
		      		<Button type={this.state.formVisible?'primary':'light'}  icon="form" onClick={this.changeFormView}/>
		      	</Button.Group>
	      	</div>
	    </Row>
      	<DocEditForm docVisible={this.state.docVisible} formVisible={this.state.formVisible} data={this.props.detail_info} updateInfo={(values) => this.props.updateDetailInfo(values) }/>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  detail_info: state.document.detail_info
});

const mapDispatchToProps = dispatch => bindActionCreators({
  getDetailDocument,
  updateDetailInfo
}, dispatch);


export default connect(mapStateToProps, mapDispatchToProps)(DocumentDetail)