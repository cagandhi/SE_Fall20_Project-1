# Guide to install and start contributing

## Contents

- [Guide to install and start contributing](#guide-to-install-and-start-contributing)
  - [Contents](#contents)
  - [Plugin Installation for every user](#plugin-installation-for-every-user)
  - [Usage](#usage)
  - [Setup (For contributors)](#setup-for-contributors)
  - [Django App](#django-app)
    - [Django App Installation (For contributors)](#django-app-installation-for-contributors)
      - [Requirements](#requirements)
      - [Steps to follow for Django App setup](#steps-to-follow-for-django-app-setup)
    - [Django App Documentation (For contributors)](#django-app-documentation-for-contributors)
  - [How to Run Tests (For contributors)](#how-to-run-tests-for-contributors)
    - [For Sublime Plugin](#for-sublime-plugin)
    - [For Django Web App](#for-django-web-app)
  - [How to Run Linter](#how-to-run-linter)
  - [How to run the Code Coverage](#how-to-run-the-code-coverage)

## Plugin Installation for every user

1. Open Sublime Text.
2. Go to Preferences -> Browse packages.
3. A new window containing Sublime packages directory will open up. Let's call this folder `SublimePackagesFolder`.
4. Open your terminal and navigate to `SublimePackagesFolder`.
5. Clone this repository inside `SublimePackagesFolder` (This makes sure that Sublime recognizes our plugin package to execute).
6. Copy the [Context.sublime-menu](code/SublimePlugin/Config/Context.sublime-menu) file to your User Packages directory. To go to User Packages directory, navigate to `SublimePackagesFolder/User` folder.
7. Change configuration settings in the [CustomPreferences.sublime-settings](code/SublimePlugin/Config/CustomPreferences.sublime-settings) file.
   1. timeout - Set the interval you want to run the logging thread
   2. api_token - Token to connect to the hosted Django API
   3. python-env - The absolute path of the python environment for this project (can be just left as `python3` if native environment is to be used)
   4. request-url - The url for the django api to send the log values to
8. You are all set. The plugin is now active and is running in the background.

## Usage

1. Open Sublime Text.
2. Open a file that you wish to work on.
3. In the file pane, right click and select the option `View CodeTime Dashboard`.
4. Access the Django UI TBD

## Setup (For contributors)

> <strong>Note:</strong> Please install and use Sublime Text 3 only for development.

1. Perform the steps in the [Installation](#plugin-installation-for-every-user) section described above.
2. Install Package Control by pressing `ctrl+shift+p (Win/Linux)` or `cmd+shift+p (Mac)`.
3. Run `python setup.py install` to install all the dependencies.
4. Back in Sublime Text, Open Package Control by pressing `ctrl+shift+p (Win/Linux)` or `cmd+shift+p (Mac)`. Navigate to option `Package Control: Install Package`. Install packages: `SublimeLinter`, `SublimeLinter-flake8`, `sublack`, `UnitTesting`.
5. Navigate to `Package Settings` option under `Preferences` in Menu bar. For `Mac` users, the `Preferences` option will be found under `Sublime Text` in Menu bar.
6. Once under Package Settings, move to `SublimeLinter > Settings`. You will see that a file with the name `SublimeLinter.sublime-settings - User` opens up. Copy the following code snippet to ignore a linting error related to Tabs vs Spaces war.

```
// SublimeLinter Settings - User
{
    "linters": {
        "flake8": {
            "args": ["--ignore=W191"],
        }
    }
}

```

## Django App

### Django App Installation (For contributors)

#### Requirements

1. `python --version` <br/>
    >= 3.6
2. `mysql --version` <br/>
   [mysql Ver 14.14 Distrib 5.7.31](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/), for Linux (x86_64) using  EditLine wrapper
3. [Django and code base requirements](../code/codetime_server/requirements.txt/requirements.txt)
4. Linter, which adheres to PEP8 standards:`flake8`
5. For auto code formatters, we have used `black` and we recommend the same.
  
> <strong>Note:</strong> We recommend using virtualenv. Also, always makemigrations and commit those new migration files to respository to keep track of changes to Database.

#### Steps to follow for Django App setup

1. Install MySQL Client, Use user `$DB_USER` and assign password `$DB_PASSWORD`
2. Export the following variables, better add to user profile:
   1. `export MYSQL_CODE_TIME_DB_NAME=codetime_db`
   2. `export MYSQL_CODE_TIME_USER=$DB_USER`
   3. `export MYSQL_CODE_TIME_PASSWORD=$DB_PASSWORD`
   4. `export MYSQL_CODE_TIME_HOST=localhost`
   5. `export MYSQL_CODE_TIME_CONNECTION_PORT=3306`
   6. `export CODE_TIME_SECRET_KEY=Sample`
3. Install all the [requirements](../code/codetime_server/requirements.txt/requirements.txt)) in your environment.
4. Go to the codetime_server folder tree, `cd code/codetime_server`
5. Run following commands:
   1. `python manage.py makemigrations`
   2. `python manage.py migrate`
   3. Finally run server on port 8000:
      1. `python manage.py runserver 0.0.0.0:8000`

### Django App Documentation (For contributors)

Refer to the `WHAT` documentation of codetime_server over here: [docs](https://prithvipatl.github.io/docs/build/html/index.html)

## How to Run Tests (For contributors)

### For Sublime Plugin

1. For local execution of the tests, make sure that the Sublime package `UnitTesting` is installed.
2. Navigate to a test file in `tests` folder that you want to run your tests for.
3. Open Package Control and type in `UnitTesting: Test Current Package`.
4. The tests will run and a small output panel pops up showing that the tests are running.

For more information and guide on how to run tests, take a look at this [README.md by randy3k](https://github.com/randy3k/UnitTesting/blob/master/README.md). For examples on how to write tests for sublime plugin, take a look at this [Repo by randy3k](https://github.com/randy3k/UnitTesting-example).

### For Django Web App

1. Navigate to the folder `code/codetime_server` and run the command `manage.py test codetime`

## How to Run Linter

1. Run the command `flake8 --max-line-length=200` from the root folder

## How to run the Code Coverage

1. From the root folder run the command `coverage run --source='.' --omit=*sgi*,*app*`
