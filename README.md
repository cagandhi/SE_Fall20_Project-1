# CodeTime - A time tracking plugin for text editors [G23 Project 1]
[![DOI](https://zenodo.org/badge/295515546.svg)](https://zenodo.org/badge/latestdoi/295515546)
[![Build Status](https://travis-ci.org/oaaky/SE_Fall20_Project-1.svg?branch=master)](https://travis-ci.org/oaaky/SE_Fall20_Project-1)
[![GitHub license](https://img.shields.io/github/license/oaaky/SE_Fall20_Project-1)](https://github.com/oaaky/SE_Fall20_Project-1/blob/master/LICENSE)
![GitHub](https://img.shields.io/badge/language-python-blue.svg)
![GitHub issues](https://img.shields.io/github/issues/oaaky/SE_Fall20_Project-1)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/oaaky/SE_Fall20_Project-1)
![YouTube Video Views](https://img.shields.io/youtube/views/CL5W7C9Jw_c?style=social)


### Promo Video
[![CodeTime Promo Video](https://img.youtube.com/vi/CL5W7C9Jw_c/0.jpg)](https://www.youtube.com/watch?v=CL5W7C9Jw_c)

### What is the product?

In this project we are developing a plugin for sublime text editor which will help developers to track the amount of time spent on multiple files, programming languages and projects. The user can perform the analysis of the time spent to improve the productivity by analysing the most frequently used programming language, most productive time of the day, files in project which took maximum time for development and projects which took maximum time for completion. The User can add the project deadlines to the plugin and plugin can help developers to stick to the goal  by predicting the finish time of the project based on the data gathered from the user. Multiple developers can compete with each other through a leader board where a leader board will display the ranking of most productive developer and admin/manager can easily monitor the productivity of each and every developer with the help of a common interface.

### How to setup this plugin?

- Open sublime text.
- Go to preferrences -> Browse packages.
- A new window containing Sublime packages will open up. Let's call this folder `SublimePackagesFolder`.
- Open terminal and go to `SublimePackagesFolder`.
- Clone this repository inside `SublimePackagesFolder`. (This makes sure that Sublime recongnizes our plugin package to execute)

### How to check if the plugin is working?

- Once the repository is cloned in `SublimePackagesFolder`, Open sublime text.
- Open a project/file the you wish to work on.
- Go to `View` -> `Show Console`.
- Now at every action (open, save, switching file), you should be able to see corresponding log entries in console.
