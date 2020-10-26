# CodeTime - A time tracking plugin for text editors

[![DOI](https://zenodo.org/badge/295515546.svg)](https://zenodo.org/badge/latestdoi/295515546)
[![Build Status](https://travis-ci.org/adarshtri/CodeTime.svg?branch=master)](https://travis-ci.org/github/adarshtri/CodeTime)
[![GitHub license](https://img.shields.io/github/license/oaaky/SE_Fall20_Project-1)](https://github.com/oaaky/SE_Fall20_Project-1/blob/master/LICENSE)
![GitHub](https://img.shields.io/badge/language-python-blue.svg)
![GitHub issues](https://img.shields.io/github/issues/adarshtri/CodeTime)

## About CodeTime

- CodeTime is a plugin for Sublime Text editor which will help developers to track the amount of time spent on multiple files, programming languages and projects. The user will be able to perform the analysis of the time spent to improve the productivity by analysing the most frequently used programming language, most productive time of the day, files in project which took maximum time for development and projects which took maximum time for completion.

- The developer can add the project deadlines to the plugin and the plugin can help developers stick to their goal by predicting the finish time of the project based on the data gathered from the user. Multiple developers can compete with each other through a leaderboard where a leaderboard will display the ranking of most productive developer and admin/manager can easily monitor the productivity of each and every developer with the help of a common interface.

[Project Requirement](docs/Project_Requirements.md) | [Architecture](docs/architecure.png) | [UI MockUps](docs/Capture.PNG) | [Working Dashboard](docs/CodeTimeDashboard.png) | [Installation and Usage Guide](docs/guide.md)

[![CodeTime](https://img.youtube.com/vi/lnOyBFZFu7g/0.jpg)](https://youtu.be/lnOyBFZFu7g)

## How to Contribute

Please take a look at our CONTRIBUTING.md where we provide instructions on contributing to the repo and taking the plugin development further.

## What things have been done for Phase 1

- Created the design and architecture of the project
- Implemented the logic to collect the data in background
- Implemented the code to generate the graphs to analyse the time spent. ([Current Working Dashboard](docs/CodeTimeDashboard.png))
- Integrated the code with sublime text editor
- Unit tests
- Build and Packaging of the plugin

## What is being done for Phase 2

- The data generated is being sent to Django based server.
- Local data analysis will be shifted to user dashboard on server.
- Leaderboard based on user's usage of files.
- Possible realtime analysis of the user's file.
