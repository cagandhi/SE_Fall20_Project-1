import React, {Component, PureComponent} from "react";
import {Card, Col, Row, Table} from "antd";
import Cookies from "js-cookie";
import {
    get_file_name_wise_time_spent,
    get_language_wise_time_spent,
    get_language_wise_user_summary,
    get_weekday_wise_user_summary
} from "../api_calls/calls";
import {Cell, Legend, Pie, PieChart, Tooltip} from "recharts";

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

const CustomTooltip = ({ active, payload, label }) => {
    if (active) {
        alert(JSON.stringify(payload))
        return (
            <div className="custom-tooltip">
                <p className="label">{`${payload} : ${payload[0].value}`}</p>
            </div>
        );
    }

    return null;
};

export default class Dashboard_home extends PureComponent{

    constructor(props) {
        super(props);

        this.state = {
            "api_token": "",
            "extension_wise_summary_data": [],
            "weekday_wise_summary": [],
            "language_wise_total_time_data": []
        }

    }

    transform_extension_wise_data(data){

        let transformed_data = []

        for(const d in data){

            transformed_data.push({name: data[d]["language"], value: data[d]["count"]});
        }
        return transformed_data;
    }

    transform_weekday_data(data){

        let transformed_data = []

        for(const d in data){

            transformed_data.push({name: data[d]["day"], value: data[d]["count"]});
        }
        return transformed_data;
    }

    transform_language_wise_total_data(data){

        let transformed_data = []

        for(const d in data){
            transformed_data.push({detected_language: data[d]["detected_language"], total_time: data[d]["total_time"]});
        }

        return transformed_data;
    }

    transform_file_name_wise_total_data(data){

        let transformed_data = []

        for(const d in data){
            transformed_data.push({file_name: data[d]["file_name"], total_time: data[d]["total_time"]});
        }

        return transformed_data;
    }

    componentDidMount() {
        const api_token = Cookies.get("api_token", undefined);
        if (api_token !== undefined && api_token !== null){
            get_language_wise_user_summary(api_token).then(data =>{
                if (JSON.stringify(data["data"]) !== JSON.stringify({})){
                    this.setState({extension_wise_summary_data: this.transform_extension_wise_data(data["data"])}, ()=>{
                        this.setState({api_token: api_token});
                    });
                }
            })

            get_weekday_wise_user_summary(api_token).then(data=>{
                if (JSON.stringify(data["data"]) !== JSON.stringify({})) {
                    this.setState({weekday_wise_summary: this.transform_weekday_data(data["data"])}, () => {
                        this.setState({api_token: api_token});
                    });
                }
            })

            get_language_wise_time_spent(api_token).then(data=>{
                if (JSON.stringify(data["data"]) !== JSON.stringify({})) {
                    this.setState({language_wise_total_time_data: this.transform_language_wise_total_data(data["data"])}, () => {
                        this.setState({api_token: api_token});
                    });
                }
            })

            get_file_name_wise_time_spent(api_token).then(data=>{
                if (JSON.stringify(data["data"]) !== JSON.stringify({})) {
                    this.setState({filename_wise_total_time_data: this.transform_file_name_wise_total_data(data["data"])}, () => {
                        this.setState({api_token: api_token});
                    });
                }
            })
        }else{
            this.setState({api_token: undefined})
        }
    }



    render() {

        const language_wise_time_spent_table_column = [
            {
                title: "Coding Language",
                key: "detected_language",
                dataIndex: "detected_language"
            },
            {
                title: "Time Spent (seconds)",
                key: "total_time",
                dataIndex: "total_time"
            }
        ]

        const filename_wise_time_spent_table_column = [
            {
                title: "File Name",
                key: "file_name",
                dataIndex: "file_name"
            },
            {
                title: "Time Spent (seconds)",
                key: "total_time",
                dataIndex: "total_time"
            }
        ]

        return (
            <div style={{padding: "10px"}}>
                <Row>
                    <Col span={12} style={{padding: "10px"}}>
                        <Card title={"File extension wise file count worked on"}>
                            <div className={"center"}>
                                <PieChart width={800} height={400}>
                                    <Pie data={this.state.extension_wise_summary_data}
                                         cx={120}
                                         cy={200}
                                         innerRadius={60}
                                         outerRadius={80}
                                         fill="#8884d8"
                                         paddingAngle={5}
                                         dataKey="value"
                                         label>
                                        {this.state.extension_wise_summary_data.map((entry, index) => <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />)}
                                    </Pie>
                                    <Tooltip active={true} />
                                    <Legend/>
                                </PieChart>
                            </div>
                        </Card>
                    </Col>
                    <Col span={12} style={{padding: "10px"}}>
                        <Card title={"Weekday wise distinct coding languages worked upon"}>
                            <div className={"center"}>
                                <PieChart width={400} height={400}>
                                    <Pie data={this.state.weekday_wise_summary}
                                         cx={120}
                                         cy={200}
                                         innerRadius={40}
                                         outerRadius={80}
                                         fill="#8884d8"
                                         paddingAngle={5}
                                         dataKey="value"
                                         label>
                                        <Tooltip active={true}/>
                                        {this.state.weekday_wise_summary.map((entry, index) => <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />)}
                                    </Pie>
                                    <Tooltip active={true}/>
                                    <Legend/>
                                </PieChart>
                            </div>
                        </Card>
                    </Col>
                </Row>
                <Row style={{padding: "10px"}}>
                    <Col span={24}>
                        <Card title={"Time Spent on Coding Languages"}>
                            <Table dataSource={this.state.language_wise_total_time_data} columns={language_wise_time_spent_table_column}/>
                        </Card>
                    </Col>
                </Row>
                <Row style={{padding: "10px"}}>
                    <Col span={24}>
                        <Card title={"Time Spent on Files"}>
                            <Table dataSource={this.state.filename_wise_total_time_data} columns={filename_wise_time_spent_table_column}/>
                        </Card>
                    </Col>
                </Row>
            </div>
        );
    }

}