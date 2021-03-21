# python-lint-boilerplate
Boilerplate / PoC automated linting for python projects using [doit](https://github.com/pydoit/doit), [pylint](https://github.com/PyCQA/pylint), [flake8](https://github.com/PyCQA/flake8), [bandit](https://github.com/PyCQA/bandit), and [mypy](https://github.com/python/mypy).

## Prerequisites
Python 3.9+, or 3.5+ if you're prepared to adjust some of the typings.

## Installation
### (Optional) Create and activate [virtual environment](https://docs.python.org/3/library/venv.html).
```shell
python -m venv venv
```
| Platform        | Shell           | Command to activate virtual environment  |
| ------------- |-------------| -----|
| POSIX/wsl | bash/zsh | $ `source venv/bin/activate` |
| | fish | $ `source venv/bin/activate.fish` |
| | csh/tcsh | $ `source venv/bin/activate.csh` |
| | PowerShell Core | $ `venv/bin/Activate.ps1` |
| Windows | cmd.exe | C:\> `venv\Scripts\activate.bat` |
| | PowerShell |	PS C:\> `venv\Scripts\Activate.ps1` |
### Install dependencies
```shell
pip -r requirements.txt
```
### Running
```shell
doit
```
Alternatively:
```shell
python dodo.py
```

## Configuration
The files checked are in the `PY_FILES` global, these can be hardcoded or determined at runtime via `os.listdir`, `os.walk`, etc. 
