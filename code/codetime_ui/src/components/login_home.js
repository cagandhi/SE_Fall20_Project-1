import React, {Component} from "react";
import {Form, Input, Button, Checkbox, Card, message} from 'antd';
import {login} from "../api_calls/calls";
import Cookies from "js-cookie";
import {Link, Redirect} from "react-router-dom";

const layout = {
    labelCol: {
        span: 8,
    },
    wrapperCol: {
        span: 16,
    },
};
const tailLayout = {
    wrapperCol: {
        offset: 8,
        span: 16,
    },
};


export default class Login_home extends Component{

    constructor(props) {
        super(props);
        this.state = {
            already_logged_in: false
        }

    }

    componentDidMount() {
        if (Cookies.get("api_token") !== undefined && Cookies.get("api_token") !== null && Cookies.get("api_token") !== "undefined"){
            this.setState({"already_logged_in": true});
        }
    }

    onFinish = (values) => {
        login(values).then(data=>{
            if(data["status"] === 200){
                message.success({content: "Successfully login", duration: 2, style: {position: "fixed", left: "50%", top: "20%", color: "#316DC1"}})
                Cookies.set("api_token", data["data"]["api_token"]);
                this.setState({already_logged_in: true});
            }
            else
                message.error({content: data["message"], duration: 2, style: {position: "fixed", left: "50%", top: "20%", color: "#316DC1"}})
        })
    }

    onFinishFailed = (errorInfo) => {
        console.log('Failed:', errorInfo);
    }

    render() {
        if(this.state.already_logged_in === true){
            message.success({content: "Already logged in.", duration: 2, style: {position: "fixed", left: "50%", top: "20%", color: "#316DC1"}})
            return <Redirect to={'/dashboard'}/>;
        }
        return (
            <div style={{padding: "20px", margin: "15px"}}>
                <Card>
                    <Form
                        {...layout}
                        name="basic"
                        initialValues={{
                            remember: true,
                        }}
                        onFinish={this.onFinish}
                        onFinishFailed={this.onFinishFailed}
                    >
                        <Form.Item
                            label="Username"
                            name="username"
                            rules={[
                                {
                                    required: true,
                                    message: 'Please input your username!',
                                },
                            ]}
                        >
                            <Input />
                        </Form.Item>

                        <Form.Item
                            label="Password"
                            name="password"
                            rules={[
                                {
                                    required: true,
                                    message: 'Please input your password!',
                                },
                            ]}
                        >
                            <Input.Password />
                        </Form.Item>

                        <Form.Item {...tailLayout} name="remember" valuePropName="checked">
                            <Checkbox>Remember me</Checkbox>
                        </Form.Item>

                        <Form.Item {...tailLayout}>
                            <Button type="primary" htmlType="submit">
                                Login
                            </Button>
                        </Form.Item>
                    </Form>
                </Card>

            </div>
        );
    }

}