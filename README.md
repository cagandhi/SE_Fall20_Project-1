# CodeTime - A time tracking plugin for text editors [G23 Project 1]

### Promo Video
[![CodeTime Promo Video](https://img.youtube.com/vi/CL5W7C9Jw_c/0.jpg)](https://www.youtube.com/watch?v=CL5W7C9Jw_c)

### What is the product?

In a nutshell, this is an extension for text editors which would let developers analyze the time it takes for them to write code in various languages broken down by projects and files they are working on. The primary purpose of such an extension is to allow developers to see the tasks that took more time for them to build and plan accordingly in the future.

### How to setup this plugin?

- Let's say: `path1` = `<path to root of this github repo>`
- Open sublime text.
- Go to preferrences -> Browse packages.
- A window new containing Sublime packages will open up. Let's call this folder `SublimePackagesFolder`.
- Open terminal and go to `SublimePackagesFolder`.
- Run command: `ln -s "<path1>/code/SublimePlugin" "CodeTime"`. (Note: keep the path names inside double quotes).