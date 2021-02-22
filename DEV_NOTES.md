# Development Set Up

From current directory


## Set up and activate virtual environment
- WINDOWS
  - `python -m venv env && .\env\Scripts\activate`
- UNIX
  - `python3 -m venv env && source env/bin/activate`


## Install libraries and package
- WINDOWS
  - `python -m pip install -e ".[dev]"`
- UNIX:
  - `python3 -m pip install -e '.[dev]'`



# Each development cycle

## Run tests
pytest -v

## Check linting
pytest --flake8 -v --cache-clear

## Run coverage check and view percentage in shell
- WINDOWS
  - `coverage run -m pytest && coverage report | find "__main__"`
- UNIX
  - `coverage run -m pytest && coverage report | grep __main__`

## Run coverage check and view details in broswer
- WINDOWS
  - `coverage run -m pytest && coverage html && start htmlcov\index.html`
- UNIX
  - `coverage run -m pytest && coverage html && open ./htmlcov/index.html`
