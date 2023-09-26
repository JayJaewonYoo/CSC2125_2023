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

## Some possible assignment 1 todos:
- Update description generation code to initialize on startup rather than on each upload
- Remove the need for the ram library and write code to run it on pytorch directly
    - The reason for this is that there seems to be some dependency conflicts because ram wants an earlier version of transformers than is required for the description model

## Notes on preparing recognize anything model (model used for tagging and/or captioning):
- https://github.com/xinyu1205/recognize-anything
- Have to run: pip install git+https://github.com/xinyu1205/recognize-anything.git
    - But requires rust to work, install using: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
- Running the code to install the pretrained model weights requires wget to be installed
## installing hugging face transformers for description generation:
- pip install git+https://github.com/huggingface/transformers
- Note may have to use --upgrade to ensure that latest version is being used
## How to test assignment 1 code:
1.Activate the virtual environment
2. Run `flask forge`
3. Run `flask run`
4. Go to the shown link
5. Login using the test account above
6. Click the upload icon next to the notifications icon
7. Upload an image
