import React, {Component} from "react";
import Cookies from "js-cookie";
import {Redirect} from 'react-router-dom';
import {Button, Card} from "antd";
import {get_account_info} from "../api_calls/calls";



export default class Account_info extends Component {

    constructor(props) {
        super(props);
        this.state = {
            "api_token": "",
            "user_data": undefined
        }
        this.logout = this.logout.bind(this);
    }

    componentDidMount() {
        const api_token = Cookies.get("api_token", undefined);
        if (api_token !== undefined && api_token !== null){
            get_account_info(api_token).then(data =>{
                this.setState({user_data: data["data"]}, ()=>{
                    this.setState({api_token: api_token});
                });
            })
        }else{
            this.setState({api_token: undefined})
        }
    }

    logout(){
        Cookies.set("api_token", undefined);
        this.setState({api_token: undefined});
    }

    render() {


        if(this.state.api_token === undefined || this.state.api_token === "undefined"){
            return(<Redirect to={"/login"}/>);
        }

        else if(this.state.api_token === ""){
            return(<div></div>);
        }
        else{
            return (
                <div style={{padding: "20px", margin: "20px"}}>
                    <Card title={"Account Info"}>
                        <p>{"Username: " + this.state.user_data["username"]}</p>
                        <p>{"API Token: "+ this.state.user_data["api_token"]}</p>
                        <Button type={"primary"} onClick={this.logout}>Log Out</Button>
                    </Card>
                </div>
            );
        }

    }


}