"""
Boilerplate make/linting for Python projects.
"""

# stdlib
import os
import os.path as path
import sys
from typing import Callable, Optional, TypedDict, Union

# 3rd-party
import pylint.lint
import mypy.api

# Globals
CURRENT_DIR: str = path.dirname(path.realpath(__file__))
PY_FILES: list[str] = [
    listing for listing in os.listdir(CURRENT_DIR)
    if path.isfile(path.join(CURRENT_DIR, listing)) and listing.endswith('.py')
]


class DoitDict(TypedDict, total=False):
    """
    Roughly the fields and types doit expects.
    """
    # pylint: disable=R0903
    basename: str
    name: Optional[str]
    actions: list[Union[Callable, str]]
    doc: str
    verbosity: int
    file_dep: list[str]
    targets: list[str]


def task_pylint() -> DoitDict:
    """
    Run pylint analysers.
    """
    def action() -> None:
        filename: str
        for filename in PY_FILES:
            pylint.lint.Run(
                ['--ignored-classes=mypy.api', filename],
                exit=False
            )

    return {
        'actions': [action],
        'verbosity': 2
    }


def task_flake8() -> DoitDict:
    """
    Run flake8 analysers.
    """
    return {
        'actions': [
            f'flake8 --exit-zero {filename}' for filename in PY_FILES
        ],
        'verbosity': 2
    }


def task_mypy() -> DoitDict:
    """
    Analyse type hints if present.
    """
    def action() -> None:
        # stderr, stdout, exit code.
        result: tuple[str, str, int] = mypy.api.run(
            ['--ignore-missing-import', *PY_FILES]
        )
        if result[0]:
            print(result[0], file=sys.stderr)

    return {
        'actions':   [action],
        'verbosity': 2
    }


def task_bandit() -> DoitDict:
    """
    Search for common security issues.
    """
    return {
        'actions': [
            f'bandit -r -q {filename}' for filename in PY_FILES
        ],
        'verbosity': 2
    }


if __name__ == '__main__':
    import doit
    doit.run(globals())
