# Albumy

*Capture and share every wonderful moment.*

> Example application for *[Python Web Development with Flask](https://helloflask.com/en/book/1)* (《[Flask Web 开发实战](https://helloflask.com/book/1)》).

Demo: http://albumy.helloflask.com

![Screenshot](https://helloflask.com/screenshots/albumy.png)

## Installation

clone:
```
$ git clone https://github.com/greyli/albumy.git
$ cd albumy
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
generate fake data then run:
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).

## Notes on Assignment 1 work:
- Functions for updating description/tags seems to be in albumy/blueprints/main.py
- Seems like in the upload() function of albumy/blueprints/main.py, we can change the description and the tags using the Photo class intiailization. This class is defined in albumy/albumy/models.py

## Notes on preparing recognize anything model (model used for tagging and/or captioning):
- https://github.com/xinyu1205/recognize-anything
- Have to run: pip install git+https://github.com/xinyu1205/recognize-anything.git
    - But requires rust to work, install using: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
- Running the code to install the pretrained model weights requires wget to be installed
