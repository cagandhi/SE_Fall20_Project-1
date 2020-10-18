import React, {Component} from 'react';
import 'antd/dist/antd.css';
import { Layout, Menu, notification} from 'antd';
import {BrowserRouter as Router, Link, Route, Switch, Redirect} from "react-router-dom";
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  HistoryOutlined,
  SmileOutlined,
  SettingOutlined,
  ToolOutlined,
  FireFilled
} from '@ant-design/icons';
import Cookies from "js-cookie";
import Login_home from "./components/login_home";
import Dashboard_home from "./components/dashboard_home";
import {Row, Col} from "antd";
import Signup_home from "./components/signup_home";
import Account_info from "./components/account_info";

require('dotenv').config();

const {SubMenu} = Menu;

export default class App extends Component{

  state = {
    'selected_tab': 'build',
    'collapsed_sider': false
  }

  constructor(props) {
    super(props);
    this.toggle_side = this.toggle_side.bind(this);
  }

  toggle_side(){
    this.setState({collapsed_sider: !this.state.collapsed_sider});
  }

  openNotification = () => {
    notification.open({
      message: 'New Updates!',
      description:
          'There are new updates on the dashboard. Checkout updates in the help section under feature history.',
      icon: <SmileOutlined style={{color: "#108ee9"}}/>
    });
  };


  render() {

    const { Header, Footer, Sider, Content } = Layout;


    return (

        <Router>
          <div>
            <Layout>
              <Sider collapsed={this.state.collapsed_sider}>
                <div>
                  <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>

                    {(Cookies.get("api_token") === "undefined" || Cookies.get("api_token") === undefined || Cookies.get("api_token") === null) && <Menu.Item key={"login_signup"} icon={<FireFilled/>}>
                      <Link to={"/login"}>
                        Login
                      </Link>
                    </Menu.Item>}

                    <Menu.Item key={"signup"} icon={<FireFilled/>}>
                      <Link to={"/signup"}>
                        SignUp
                      </Link>
                    </Menu.Item>

                    <Menu.Item key={"dashboard"} icon={<ToolOutlined/>}>
                      <Link to={"/dashboard"}>
                        Dashboard
                      </Link>
                    </Menu.Item>

                    <Menu.Item key={"account"} icon={<FireFilled/>}>
                      <Link to={"/account"}>
                        Account
                      </Link>
                    </Menu.Item>

                  </Menu>
                </div>
              </Sider>
              <Layout>
                <Header style={{background: "white", height: "120px", float: "left"}}>
                  <Row>
                    <Col span={10}>
                      <div>
                        {React.createElement(this.state.collapsed_sider ? MenuUnfoldOutlined : MenuFoldOutlined, {
                          className: 'trigger',
                          onClick: this.toggle_side,
                        })}
                      </div>
                    </Col>
                    <Col span={14}>
                      <div className="center">
                        <h1 style={{color: "#316DC1", margin: "20px"}}>CodeTime</h1>
                      </div>
                    </Col>

                  </Row>


                </Header>
                <Content>
                  <Switch>
                    <Route component={Login_home} path="/login" exact/>
                    <Route component={Signup_home} path="/signup" exact/>
                    <Route component={Dashboard_home} path="/dashboard" exact/>
                    <Route component={Account_info} path="/account" exact/>
                    <Redirect exact from="" to={"/login"}/>

                  </Switch>
                </Content>

                <Footer style={{ textAlign: 'center' }}>
                  CodeTime ©2020
                </Footer>

              </Layout>
            </Layout>
          </div>
        </Router>
    );

  }

}