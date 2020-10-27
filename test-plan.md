# Test Plan

In this document we describe our test plan for the project in terms of performance benchmarking and results comparisons.

## Motivation

The task in Homework 3 assignment was to record the time taken by human beings to detect and rectify bugs introduced in three different languages for game of life. Most of the process was automated but there is still a scope of human errors to record time manually. CodeTime could be a solution to this error caused by humans as it involves their minimal involvement. The user who is given the task to detect and rectify bugs can follow the same process of opening the file they want to correct and start debugging. The start time and end time will automatically get recorded as soon as the user opens a file and closes it. He can view his result on the dashboard later. The time taken during this process can be compared with the time taken by the group 18’s / some other group’s previous report in homework 3 and the expected result should be that the time taken by enabling codeTime will be more accurate than the previous tests performed in Homework 3. 

## Lab Testing / Human Trials Setup

We propose to perform the task of debugging game of life code which is implanted with bugs. 

The whole debugging process should be conducted in following fashion to benchmark codetime:

1. First a human should debug game of life in exact same setup that was used in Homework 3 and the reading should be recorded. While this exercise is going on we will have a team member from our group note down activities of the user who is debugging the code that can cause error in time reading for debugging. These activities could be like the code is debugged by the user but he/she took some time to stop the timer or the moderator forgot to stop the timer.

2. In the next step we perform the same debugging operation with **CodeTime**. This time the user who is debugging the code has to open the file, debug the program in **sublime text** and when done debugging just close the file. The result of time taken to debug will automatically sync up with our server and show up on users account on the database.

### Important things to consider

  - Make sure the user debugging the code has codetime installed and account logged in with api token configured so that data sync happens seemlessly.
  - The same user debugs the code, and the level of difficulty of bugs in both the scenarios should be comparable.
  - When we talk about delays in time reading, we don't mean error rates in minutes. They could be as small as few seconds. CodeTime is just a tool which aims to make result capturing more accurate.
