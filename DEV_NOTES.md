# Development Set Up

From current directory

```

# Set up and activate virtual environment
python3 -m venv env && source env/bin/activate

# Install libraries and package
python3 -m pip install -e '.[dev]'


### Each development cycle

# Run tests
pytest -v

# Check linting
pytest --flake8 -v --cache-clear

# Run coverage check and view percentage in shell
coverage run -m pytest && coverage report | grep __main__

# Run coverage check and view details in broswer
coverage run -m pytest && coverage html && open ./htmlcov/index.html

```
