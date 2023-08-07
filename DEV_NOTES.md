# Development Set Up

From root directory


## Set up and activate virtual environment
- WINDOWS
  - `python -m venv env && .\env\Scripts\activate`
- UNIX
  - `python3 -m venv env && source env/bin/activate`
- PYENV
  - `pyenv virtualenv env && pyenv activate env`


## Install libraries and package
- WINDOWS
  - `python -m pip install -e ".[dev]"`
- UNIX:
  - `python3 -m pip install -e '.[dev]'`



# Each development cycle

## Check linting
`flake8`

## Run tests
`pytest -v --cache-clear`

## Run tests against all supported versions
`tox`

## Run coverage check and view percentage in shell
`coverage run -m pytest && coverage report`

## Run coverage check and view details in broswer
- WINDOWS
  - `coverage run -m pytest && coverage html && start htmlcov\index.html`
- UNIX
  - `coverage run -m pytest && coverage html && open ./htmlcov/index.html`


# MkDocs and RTD documentation development
- Serve documentation from local machine: `mkdocs serve`


# RTD Publish
- Log into RTD
- Go to "My Projects" > meraki-cli
- Click "Build Version"


# Publish

## Update Meraki SDK package
`pip3 install --upgrade meraki`

## Run all dev cycle tests
- See above

## Regenerate Command Guide
`python3 .command_guide_build.py`

## Update Versions
- Update `__version__.py`
- Update referenced version in `README.md`
- Add the new version notes to `CHANGELOG.md`
- `deactivate`
- `bash commit.sh`
- Update DevNet by pulling changes (https://developer.cisco.com/codeexchange/github/repo/PackeTsar/meraki-cli#edit)
