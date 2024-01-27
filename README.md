### Hexlet tests and linter status:
[![Maintainability](https://api.codeclimate.com/v1/badges/79cd5baa75e2d3433ee5/maintainability)](https://codeclimate.com/github/DmGorokhov/Magic-Ball/maintainability)

### About:
Magic Ball- it's a page of predictions.  
Here you can ask a worrying question and get an answer


### Requirements:

* python >= 3.10
* flask >= 3.0.1
* flask-session >= 0.6.0
* flask-wtf >= 1.2.1
* gunicorn >= 21.2.0
* python-dotenv >= 1.0.0
* Make (is used to run utility through console-command)
* Poetry >1.2.2

**Poetry** is setup by the commands:

**Linux, macOS, Windows (WSL):**

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Details on installing and using the **Poetry** package are available in [official documentation](https://python-poetry.org/docs/).

To install **Poetry** you need **Python 3.7+** use the information from the official website [python.org](https://www.python.org/downloads/)

### Installation

Cloning the repository

```bash
git clone git@github.com:DmGorokhov/Magic-Ball
cd Magic-Ball
```

Activate virtual environment

```bash
poetry shell
```
**Create .env file and set environment variables using file .env.example as example.
For development purposes you can leave these variables as suggested in example.
If you would like leave example variables (do it only for developer and check purposes) type in terminal:**
```commandline
mv .env.example .env
```

Setup app
```bash
make install
```

### Basic commands:
When cloning app repository, you may need to install Make for run short console-commands described below.
```
make dev   # starts the app on the local server in the development environment
```
```
make start   # start the app in the production environment
```
```
make clean-sessions  # remove all sessions files
```