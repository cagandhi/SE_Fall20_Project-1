# CodeTime - A time tracking plugin for text editors [G23 Project 1]
[![DOI](https://zenodo.org/badge/295515546.svg)](https://zenodo.org/badge/latestdoi/295515546)
[![Build Status](https://travis-ci.org/oaaky/SE_Fall20_Project-1.svg?branch=master)](https://travis-ci.org/oaaky/SE_Fall20_Project-1)
[![GitHub license](https://img.shields.io/github/license/oaaky/SE_Fall20_Project-1)](https://github.com/oaaky/SE_Fall20_Project-1/blob/master/LICENSE)
![GitHub](https://img.shields.io/badge/language-python-blue.svg)
![GitHub issues](https://img.shields.io/github/issues/oaaky/SE_Fall20_Project-1)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/oaaky/SE_Fall20_Project-1)
![YouTube Video Views](https://img.shields.io/youtube/views/CL5W7C9Jw_c?style=social)


## About CodeTime

- CodeTime is a plugin for Sublime Text editor which will help developers to track the amount of time spent on multiple files, programming languages and projects. The user will be able to perform the analysis of the time spent to improve the productivity by analysing the most frequently used programming language, most productive time of the day, files in project which took maximum time for development and projects which took maximum time for completion.

- The developer can add the project deadlines to the plugin and the plugin can help developers stick to their goal by predicting the finish time of the project based on the data gathered from the user. Multiple developers can compete with each other through a leaderboard where a leaderboard will display the ranking of most productive developer and admin/manager can easily monitor the productivity of each and every developer with the help of a common interface.

[Project Requirement](https://github.com/oaaky/SE_Fall20_Project-1/blob/master/project_requiremnt.md) | [Architecture Diagram](https://github.com/oaaky/SE_Fall20_Project-1/blob/master/architecure.png) | [UI MockUps](https://github.com/oaaky/SE_Fall20_Project-1/blob/master/Capture.PNG)

[![CodeTime Promo Video](https://img.youtube.com/vi/CL5W7C9Jw_c/0.jpg)](http://tiny.cc/codeTimePromo)


## Installation (For non-contributors)

1. Open Sublime Text.
2. Go to Preferences -> Browse packages.
3. A new window containing Sublime packages directory will open up. Let's call this folder `SublimePackagesFolder`.
4. Open your terminal and navigate to `SublimePackagesFolder`.
5. Clone this repository inside `SublimePackagesFolder` (This makes sure that Sublime recognizes our plugin package to execute).
6. You are all set. The plugin is now active and is running in the background.


## Usage (For non-contributors)

1. Open Sublime Text.
2. Open a file that you wish to work on.
3. In the file pane, right click and select the option `View CodeTime Dashboard`.


## Setup (For contributors)

## How to Contribute? (For contributing developers)

Please take a look at our CONTRIBUTING.md where we provide instructions on contributing to the repo and taking the plugin development further.

### What things are planned for Phase 2?

- The data generated will be sent to server.
- Local data analysis will be shifted to server based dashboard.
- Slack notification of weekly report to user will be sent through server.
- Leaderboard based on user's usage of files.
- Adding support for other editors such as visual code.
- Possible realtime analysis of the user's file.
