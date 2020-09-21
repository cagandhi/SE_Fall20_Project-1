#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:41:40 2020

@author: nirav
"""
import mimetypes
from plotly.offline import plot 
import plotly.graph_objs as go
from collections import defaultdict
from datetime import datetime

#def show_graphs():
sample_data = open("sublime_logs","r").read()
logs = sample_data.split("\n")

#file_type_mapping = {
#        "ASP Classic" : ["asp"],
#        "ASP.NET" : ["aspx", "axd", "asx", "asmx", "ashx"],
#        "CSS" : ["css"],
#        "Coldfusion" : ["cfm"],
#        "Erlang" : ["yaws"],
#        "Flash" : ["swf"],
#        "HTML" : ["html","htm","xhtml","jhtml"],
#        "Java" : ["jsp","jspx","wss",""]
#        
#        
#        }

logs_dict = {}
for log in logs[:-1]:
    log_date, log_file_path, start_time, end_time = log.split(",")
    end_time, start_time = float(end_time), float(start_time)
    file_type = mimetypes.guess_type(log_file_path)
    if file_type[0] is not None:
        file_type = file_type[0].split("/")[-1].split("-")[-1]
    else:
        file_type = "other"
    logs_dict[log_file_path] = {"st":start_time,"dt":datetime.strptime(log_date, "%Y-%m-%d"), "et":end_time,"duration":end_time-start_time,"type":file_type}

################################- Pie Chart-
durations = defaultdict(int)
for file_path in logs_dict.keys():
    duration = logs_dict[file_path]["duration"]
    file_type = logs_dict[file_path]["type"]
    durations[file_type] += duration
    
trace_timespan = go.Pie(labels=list(durations.keys()),values=list(durations.values()))
fig = go.Figure(data=[trace_timespan])
plot(fig,filename="standchigolund.html")
###############################

###############################-Time fill graph per filetype
durations = defaultdict(dict)
for file_path in logs_dict.keys():
    duration = logs_dict[file_path]["duration"]
    file_type = logs_dict[file_path]["type"]
    date = logs_dict[file_path]["dt"]

    if date in durations[file_type]:
        durations[file_type][date] += duration
    else:
        durations[file_type][date] = duration

data = []
for file_type in durations.keys():
    trace_timespan = go.Scatter(x=list(durations[file_type].keys()),y=list(durations[file_type].values()),name=file_type, fill='tozeroy')
    data.append(trace_timespan)
fig = go.Figure(data=data)
plot(fig,filename="standchigolund.html")


    

