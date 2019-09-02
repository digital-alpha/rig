import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import {
  getUploadedDocuments,
  processDocument,
  deleteDocument,
  saveToCSV,
  clearDB
} from '../../actions/document'

import { Table, Input, Button, Icon, Row, Col} from 'antd';
import Highlighter from 'react-highlight-words';

import Toolbar from "../../components/Toolbar/Toolbar";
import DocModal from "../../components/Modal/DocModal";
import UploadDrawer from "../../components/Drawer/UploadDrawer";

import './Home.css'


class Home extends React.Component {
  state = {
    searchText: '',
    visibleModal: false,
    visibleDrawer: false,
    placement: 'left' ,
    loading: false,
  };

  showModal = () => {
    this.setState({
      visibleModal: true,
    });
  };

  hideModal = () => {
    this.setState({
      visibleModal: false,
    });
  };

  showDrawer = () => {
    this.setState({
      visibleDrawer: true,
    });
  };

  onClose = () => {
    this.setState({
      visibleDrawer: false,
    });
  };

  getColumnSearchProps = dataIndex => ({
    filterDropdown: ({ setSelectedKeys, selectedKeys, confirm, clearFilters }) => (
      <div style={{ padding: 8 }}>
        <Input
          ref={node => {
            this.searchInput = node;
          }}
          placeholder={`Search ${dataIndex}`}
          value={selectedKeys[0]}
          onChange={e => setSelectedKeys(e.target.value ? [e.target.value] : [])}
          onPressEnter={() => this.handleSearch(selectedKeys, confirm)}
          style={{ width: 188, marginBottom: 8, display: 'block' }}
        />
        <Button
          type="primary"
          onClick={() => this.handleSearch(selectedKeys, confirm)}
          icon="search"
          size="small"
          style={{ width: 90, marginRight: 8 }}
        >
          Search
        </Button>
        <Button onClick={() => this.handleReset(clearFilters)} size="small" style={{ width: 90 }}>
          Reset
        </Button>
      </div>
    ),
    filterIcon: filtered => (
      <Icon type="search" style={{ color: filtered ? '#1890ff' : undefined }} />
    ),
    onFilter: (value, record) =>
      record[dataIndex]
        .toString()
        .toLowerCase()
        .includes(value.toLowerCase()),
    onFilterDropdownVisibleChange: visible => {
      if (visible) {
        setTimeout(() => this.searchInput.select());
      }
    },
    render: text => (
      <Highlighter
        highlightStyle={{ backgroundColor: '#ffc069', padding: 0 }}
        searchWords={[this.state.searchText]}
        autoEscape
        textToHighlight={text.toString()}
      />
    ),
  });

  handleSearch = (selectedKeys, confirm) => {
    confirm();
    this.setState({ searchText: selectedKeys[0] });
  };

  handleReset = clearFilters => {
    clearFilters();
    this.setState({ searchText: '' });
  };

  onClickRow = (e, row, index) => {
    this.showModal()
  }

  async processDocument () {
      this.setState({
        loading: true
      })

      await this.props.processDocument();
      this.props.getUploadedDocuments()

       this.setState({
        loading: false
      })
  }

  componentWillMount(){
    this.props.getUploadedDocuments()
  }

  clearDB(){
    if(window.confirm('Are you sure to clean database?'))
      this.props.clearDB()
  }


  render() {

    const columns = [
      {
        title: 'Title',
        dataIndex: 'title',
        key: 'title',
        width: '40%',
        ...this.getColumnSearchProps('title'),
        sorter: (a, b) => a.title.length - b.title.length,
        render: (text, record) => {
          if(record.process_date == '')
            return <strong>{text}</strong>
          else return <Link to={`document/${record.id}`}>{text}</Link>},
      },
      {
        title: 'Uploaded By',
        dataIndex: 'author',
        key: 'author',
        ...this.getColumnSearchProps('author'),
        sorter: (a, b) => a.author.length - b.author.length,
      },
      {
        title: 'Uploaded Date',
        dataIndex: 'upload_date',
        key: 'upload_date',
        ...this.getColumnSearchProps('upload_date'),
        sorter: (a, b) => {

          let dateA = !a.upload_date
            ? new Date().getTime()
            : new Date(a.upload_date).getTime();

          let dateB = !b.upload_date
            ? new Date().getTime()
            : new Date(b.upload_date).getTime();

          return dateA-dateB;
        }
      },
      {
        title: 'Processed Date',
        dataIndex: 'process_date',
        key: 'process_date',
        ...this.getColumnSearchProps('process_date'),
        defaultSortOrder: 'descend',
        sorter: (a, b) => {

          let dateA = !a.process_date
            ? new Date().getTime()
            : new Date(a.process_date).getTime();

          let dateB = !b.process_date
            ? new Date().getTime()
            : new Date(b.process_date).getTime();

          return dateA-dateB;
        }
      },
      {
        title: 'Operation',
        dataIndex: 'operation',
        key: 'operation',
        width: 100,
        align: 'center',
        render: (text, record) => (
          <span>
            <Button type="primary" shape="circle" icon="delete" onClick={() => {this.props.deleteDocument(record.id)}}/>
          </span>
        ),
        fixed: 'right'
      },
    ];


    let documents = this.props.document || []

    return(
      <div>
        <h1>Process Document</h1>
        <UploadDrawer visible={this.state.visibleDrawer} onClose={() => this.onClose()} callback={() => this.props.getUploadedDocuments()}/>
        <Row gutter={30}>
          <Col sm={24} md={24}>
              <Toolbar loading={this.state.loading} showDrawer={() => this.showDrawer()} saveToCSV={() => this.props.saveToCSV()} clearDB={() => this.clearDB()} processDocs = {() => this.processDocument() }/>
              <DocModal visible={this.state.visibleModal} hideModal={() => this.hideModal()} />
              <Table columns={columns} 
              dataSource={documents} onChange={this.handleChange} bordered={true} scroll={{ x: 1300}}/>
          </Col>
        </Row>
      </div>
    )
  }
}

const mapStateToProps = state => ({
  document: state.document.documents
});

const mapDispatchToProps = dispatch => bindActionCreators({
  getUploadedDocuments,
  processDocument,
  deleteDocument,
  saveToCSV,
  clearDB
}, dispatch);

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Home)