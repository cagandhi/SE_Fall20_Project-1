import React, {Component} from "react";
import {Form, Input, Button, Checkbox, Card, message} from 'antd';
import {signup} from "../api_calls/calls";

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


export default class Signup_home extends Component{

    constructor(props) {
        super(props);

    }

    onFinish = (values) => {
        signup(values).then(data=>{
            if(data["status"] === 200){
                message.success({content: "Successfully Signed Up", duration: 2, style: {position: "fixed", left: "50%", top: "20%", color: "#316DC1"}})
            }
            else
                message.error({content: data["message"], duration: 2, style: {position: "fixed", left: "50%", top: "20%", color: "#316DC1"}})
        })
    }

    onFinishFailed = (errorInfo) => {
        console.log('Failed:', errorInfo);
    }

    render() {
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
                                SignUp
                            </Button>
                        </Form.Item>
                    </Form>
                </Card>

            </div>
        );
    }

}