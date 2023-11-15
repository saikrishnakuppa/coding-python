# Sample Fast API

## Local Setup

This project requires a minimum of Python 3.12.

To run API locally:

```bash

# 1. Install pipenv package manager
pip install pipenv==2023.10.3

# 2. Install project dependencies (this will automatically set up a virtual env)
PIPENV_VENV_IN_PROJECT=1 pipenv install

# 3. Start the local server
pipenv run server
```

### Alternative option for local setup

As an alternative to pipenv, the project dependencies may be installed using pip, following the creation of a virtual environment.

To run the API locally using pip:

```bash
# 1. Create a virtual environment to isolate the project dependencies
python -m venv .venv

# 2. Activate the virtual environment
# Linux/Bash:
source .venv/Scripts/activate
# MacOS:
source .venv/bin/activate
# Windows:
.venv/Scripts/activate.bat

# 3. Install project dependencies inside the virtual environment
pip install -r requirements.txt

# 4. Start the local server
uvicorn src.main:app --reload
```

## Formatting

Run `pipenv run format` to run formatting for the project via Black.

## Linting

Run `pipenv run lint` to run linting for the project via Pylint.

## Testing

Run `pipenv run test` to run unit tests for the project via Pytest.