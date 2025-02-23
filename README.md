# Tiny
TinyURL code exercise.

With Flask. And Pytest.

## Installation

### Get the `https://github.com/Craftermath/Tiny` repo

You can do whatever you want to get the code: clone, fork, download. After making your own copy of the "Tiny" repository you will have your own project to study.  

### Run in your local development environment

I suggest this sequence of commands in a terminal of a linux with python already installed:

1. Create your environment:
```
python -m venv play
```
2. Activate your environment:
```
. play/bin/activate
```
3. Update your pip:
```
pip install --upgrade pip
```

#### Install requirements

```
pip install -r requirements.txt
```

#### Run 

```
python run.py
```

You should see something like:

```
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```
And you need to open the link http://127.0.0.1:5000 in your browser. 
Good Luck! 

#### Tests

```
pytest
```

You should see something like:

```
============================= test session starts ==============================
platform linux -- Python 3.13.2, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/fadora/Studystation/Tiny
configfile: pyproject.toml
plugins: flask-1.3.0
collected 5 items                                                              

tests/test_views.py ....s                                                [100%]

========================= 4 passed, 1 skipped in 3.81s =========================

```

Have fun!

