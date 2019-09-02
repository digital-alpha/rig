import React, { Fragment } from 'react'
import { Route, Link } from 'react-router-dom';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import {
  signout,
  currentUser
} from '../../actions/auth'

import { Layout, Menu, Avatar, Affix, Drawer, Button } from 'antd';

import Home from '..//Home/Home';
import DocumentDetail from '../Document/DocumentDetail';
import BreadcrumbHeader from "../../components/BreadcrumbHeader";

import './App.css'

const { Header, Content, Footer } = Layout;
const { SubMenu } = Menu


class App extends React.Component{
  state = {
    visible: false
  }

  showDrawer = () => {
    this.setState({
      visible: true,
    });
  }

  onClose = () => {
    this.setState({
      visible: false,
    });
  };

  async getCurrentUser() {
    await this.props.currentUser()
  }

  componentWillMount(){
     if(!this.props.auth.is_authed){
       window.location = '/login'
     } else {
       this.getCurrentUser()
     }
  }

  render() {
    let username = this.props.auth.user || '';

    return (
        <Layout className="layout">
         <Affix offsetTop={0}>
            <Header className="header">
              <div className="navLogo"></div>
              <Menu className="navbar"
                mode="horizontal"
                defaultSelectedKeys={['1']}
                style={{ lineHeight: '64px' }}
              >
                <Menu.Item key="1"><Link to="/">Home</Link></Menu.Item>
                <Menu.Item key="2"><Link to="/users">Tab2</Link></Menu.Item>
                <Menu.Item key="3"><Link to="/users">Tab3</Link></Menu.Item>
              </Menu>
              <div className="rightContainer">
                <Menu key="user" className="user-profile" mode="horizontal" onClick={this.handleClickMenu}>
                  <SubMenu
                    title={
                      <Fragment>
                        <span style={{ color: '#999', marginRight: 4 }}>
                          Hi,
                        </span>
                        <span>{username}</span>
                        <Avatar style={{ marginLeft: 8 }} src='' />
                      </Fragment>
                    }
                  >
                    <Menu.Item key="SignOut">
                      <Link to="/login" onClick={() => this.props.signout()}>Sign out</Link>
                    </Menu.Item>
                  </SubMenu>
                </Menu>
                <Button className="barsMenu" type="primary" onClick={this.showDrawer} icon='menu' style={{display: 'none'}}>
                </Button>
              </div>
              <Drawer
                title="Menus"
                placement="right"
                closable={false}
                onClose={this.onClose}
                visible={this.state.visible}
              >
                <Menu 
                  mode="vertical"
                  defaultSelectedKeys={['1']}
                  style={{ lineHeight: '64px' }}
                >
                  <Menu.Item key="1"><Link to="/">Home</Link></Menu.Item>
                  <Menu.Item key="2"><Link to="/users">Tab2</Link></Menu.Item>
                  <Menu.Item key="3"><Link to="/users">Tab3</Link></Menu.Item>
                </Menu>
                <Menu 
                  mode="vertical"
                  defaultSelectedKeys={['1']}
                  style={{ lineHeight: '64px' }}
                >
                  <Menu.Item key="SignOut">
                    <Link to="/login" onClick={() => this.props.signout()}>Sign out</Link>
                  </Menu.Item>
                </Menu>
              </Drawer>
            </Header>
          </Affix>
        <Content style={{ padding: '0 50px' }}>
          <BreadcrumbHeader></BreadcrumbHeader>

          <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
              <main>
                  <Route exact path="/" component={Home} />
                  <Route path="/document/:id" component={DocumentDetail} />
              </main>
          </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>Employee @2019 Created by RIG</Footer>
      </Layout>
    )
  }
}

const mapStateToProps = state => ({
  auth: state.auth
});

const mapDispatchToProps = dispatch => bindActionCreators({
  signout,
  currentUser
}, dispatch);


export default connect(mapStateToProps, mapDispatchToProps)(App)