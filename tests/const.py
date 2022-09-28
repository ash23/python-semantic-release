A_FULL_VERSION_STRING = "1.11.567"
A_PRERELEASE_VERSION_STRING = "2.3.4-dev.23"
A_FULL_VERSION_STRING_WITH_BUILD_METADATA = "4.2.3+build.12345"

EXAMPLE_REPO_OWNER = "example_owner"
EXAMPLE_REPO_NAME = "example_repo"

COMMIT_MESSAGE = "{version}\n\nAutomatically generated by python-semantic-release"

# Different in-scope commits that produce a certain release type
ANGULAR_COMMITS_PATCH = [
    "fix: something annoying\n",
    "fixup the bugfix\n",
    "oops it broke again\n",
    "fix\n",
    "fix\n",
    "fix\n",
    "fix\n",
    "fix: release the bugfix-fix\n",
]
ANGULAR_COMMITS_MINOR = [
    "feat: something special\n",
    "fix: needed a tweak\n",
    "tweaked again\n",
    "tweaked again\n",
    "tweaked again\n",
    "fix\n",
    "fix\n",
    "feat: last minute rush order\n",
]
# Take previous commits and insert a breaking change
ANGULAR_COMMITS_MAJOR = ANGULAR_COMMITS_MINOR.copy()
ANGULAR_COMMITS_MAJOR.insert(
    4, "fix!: big change\n\nBREAKING CHANGE: reworked something for previous feature\n"
)

EMOJI_COMMITS_PATCH = [
    ":bug: something annoying\n",
    "fixup the bugfix\n",
    "oops it broke again\n",
    "fix\n",
    "fix\n",
    "fix\n",
    "fix\n",
    "fix\n",
    ":bug: release the bugfix-fix\n",
]
EMOJI_COMMITS_MINOR = [
    ":sparkles: something special\n",
    ":sparkles::pencil: docs for something special\n",
    ":bug: needed a tweak\n",
    "tweaked again\n",
    "tweaked again\n",
    "tweaked again\n",
    "fix\n",
    "fix\n",
    # Emoji in description should not be used to evaluate change type
    ":sparkles: last minute rush order\n\n:boom: Good thing we're 10x developers",
]
EMOJI_COMMITS_MAJOR = EMOJI_COMMITS_MINOR.copy()
EMOJI_COMMITS_MAJOR.insert(4, ":boom: Move to the blockchain")

SCIPY_FORMATTED_COMMIT_BODY_PARTS = [
        # a squash merge that preserved PR commit messages
        (
            "DOC: import ropy.transform to test for numpy error",
            "DOC: lower numpy version",
            "DOC: lower numpy version further",
            "MAINT: remove debugging import",
        ),
        # empty body
        (),
        # formatted body
        (
            """Bumps [sphinx](https://github.com/sphinx-doc/sphinx) from 3.5.3 to 4.1.1.
            - [Release notes](https://github.com/sphinx-doc/sphinx/releases)
            - [Changelog](https://github.com/sphinx-doc/sphinx/blob/4.x/CHANGES)
            - [Commits](https://github.com/sphinx-doc/sphinx/commits/v4.1.1)""",
            """---
            updated-dependencies:
            - dependency-name: sphinx
            dependency-type: direct:development
            update-type: version-update:semver-major""",
        ),
        (
            "Bug spotted on Fedora, see https://src.fedoraproject.org/rpms/scipy/pull-request/22",
            "The `int[::]` annotation is used to accept non-contiguous views.",
        ),
        ("[skip azp] [skip actions]",),
]

# Note - the scipy commit testing in v7 is very comprehensive -
# fixtures for commits that should evaluate to the various scopes
# are in tests/fixtures/scipy


TAG_COMMITS_PATCH = [
    ":nut_and_bolt: something annoying\n",
    "fixup the bugfix\n",
    "oops it broke again\n",
    "fix\n",
    "fix\n",
    "fix\n",
    "fix\n",
    ":persevere: fix\n"
    ":nut_and_bolt: release the bugfix-fix\n",
]
TAG_COMMITS_MINOR = [
    ":sparkles: something special\n",
    ":nut_and_bolt: needed a tweak\n",
    "tweaked again\n",
    "tweaked again\n",
    "tweaked again\n",
    "fix\n",
    "fix\n",
    ":sparkles: last minute rush order\n",
]
TAG_COMMITS_MAJOR = TAG_COMMITS_MINOR.copy()
TAG_COMMITS_MAJOR.insert(
    4,
    ":nut_and_bolt: big change\n\nBREAKING CHANGE: reworked something for previous feature\n",
)

EXAMPLE_PROJECT_NAME = "example"
EXAMPLE_PROJECT_VERSION = "0.2.2"

EXAMPLE_PYPROJECT_TOML_CONTENT = rf"""
[tool.poetry]
name = "{EXAMPLE_PROJECT_NAME}"
version = "{EXAMPLE_PROJECT_VERSION}"
description = "Just an example"
license = "MIT"
authors = ["semantic-release <not-a.real@email.com>"]
readme = "README.md"
classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Framework :: FastAPI",
    "Framework :: Pytest",
    "Intended Audience :: Education",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Education",
    "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
]

[tool.poetry.urls]
"Repository" = "https://github.com/relekang/python-semantic-release"
"Bug Tracker" = "https://github.com/relekang/python-semantic-release"
"Homepage" = "https://github.com/relekang/python-semantic-release"

[tool.poetry.scripts]
hello-world = "hello-world:main"

[tool.poetry.dependencies]
python = "^3.8"
fastapi = "^0.74.0"
uvicorn = "^0.17.5"
PyYAML = "^6.0"
python-dotenv = "^0.19.2"
motor = "^2.5.1"
pymongo = "^3.12.0"

[tool.poetry.dev-dependencies]
pytest = "^6.2"
bandit = "^1.7.2"
mypy = "0.931"
black = "^22.1.0"
safety = "^1.10.3"
flake8 = "^4.0.1"
types-PyYAML = "^6.0.4"
python-semantic-release = "^7.25.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.semantic_release]
version_variable = [
    "src/{EXAMPLE_PROJECT_NAME}/__init__.py:__version__",
]
version_toml = "pyproject.toml:tool.poetry.version"
branch = "main"
upload_to_pypi = false
upload_to_repository = false
upload_to_release = true
build_command = "pip install poetry && poetry build"

[tool.isort]
profile = "black"
src_paths = ["src"]
known_first_party = "{EXAMPLE_PROJECT_NAME}"
known_third_party = ["fastapi", "pydantic", "motor", "bson", "uvicorn"]
combine_as_imports = true

[tool.mypy]
python_version=3.7

mypy_path="src"

show_column_numbers=true
show_error_context=true
pretty=true
error_summary=true

follow_imports="normal"
ignore_missing_imports=true

disallow_untyped_calls=true
warn_return_any=true
strict_optional=true
warn_no_return=true
warn_redundant_casts=true
warn_unused_ignores=true
warn_unused_configs=true
disallow_any_generics=true

warn_unreachable=true
disallow_untyped_defs=true
check_untyped_defs=true

cache_dir="/dev/null"

[[tool.mypy.overrides]]
module = "tests.*"
allow_untyped_defs = true
allow_incomplete_defs = true
allow_untyped_calls = true
"""

EXAMPLE_SETUP_CFG_CONTENT = rf"""
[metadata]
name = example
version = {EXAMPLE_PROJECT_VERSION}
description = Just an example really
long_description = file: README.md
long_description_content_type = text/markdown
author = semantic-release
author_email = not-a.real@email.com
url = https://github.com/relekang/python-semantic-release
python_requires = >=3.7


[options]
zip_safe = True
include_package_data = True
packages = find:
install_requires =
    PyYAML==6.0
    pydantic==1.9.0

[options.extras_require]
dev =
    tox
    twine==3.1.1

test =
    pytest
    pytest-cov
    pytest-mock
    pytest-aiohttp

lint =
    flake8
    black>=22.6.0
    isort>=5.10.1

[options.packages.find]
exclude =
    test*

[bdist_wheel]
universal = 1

[coverage:run]
omit = */tests/*

[tools:pytest]
python_files = tests/test_*.py tests/**/test_*.py

[isort]
skip = .tox,venv
default_section = THIRDPARTY
known_first_party = {EXAMPLE_PROJECT_NAME},tests
multi_line_output=3
include_trailing_comma=True
force_grid_wrap=0
use_parentheses=True
line_length=88

[flake8]
max-line-length = 88

[semantic_release]
version_variable = {EXAMPLE_PROJECT_NAME}/__init__.py:__version__
"""

EXAMPLE_SETUP_PY_CONTENT = rf"""
import re
import sys

from setuptools import find_packages, setup


def _read_long_description():
    try:
        with open("readme.rst") as fd:
            return fd.read()
    except Exception:
        return None


with open("{EXAMPLE_PROJECT_NAME}/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

try:
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    pass

setup(
    name="{EXAMPLE_PROJECT_NAME}",
    version="{EXAMPLE_PROJECT_VERSION}",
    url="http://github.com/relekang/python-semantic-release",
    author="semantic-release",
    author_email="not-a.real@email.com",
    description="Just an example",
    long_description=_read_long_description(),
    packages=find_packages(exclude=("tests",)),
    license="MIT",
    install_requires=[
        "click>=7,<9",
        "click_log>=0.3,<1",
        "gitpython>=3.0.8,<4",
        "invoke>=1.4.1,<2",
        "semver>=2.10,<3",
        "twine>=3,<4",
        "requests>=2.25,<3",
        "wheel",
        "python-gitlab>=2,<4",
        # tomlkit used to be pinned to 0.7.0
        # See https://github.com/relekang/python-semantic-release/issues/336
        # and https://github.com/relekang/python-semantic-release/pull/337
        # and https://github.com/relekang/python-semantic-release/issues/491
        "tomlkit~=0.10",
        "dotty-dict>=1.3.0,<2",
        "dataclasses==0.8; python_version < '3.7.0'",
        "packaging",
    ],
    extras_require={{
        "test": [
            "coverage>=5,<6",
            "pytest>=5,<6",
            "pytest-xdist>=1,<2",
            "pytest-mock>=2,<3",
            "pytest-lazy-fixture~=0.6.3",
            "responses==0.13.3",
            "mock==1.3.0",
        ],
        "docs": ["Sphinx==1.3.6", "Jinja2==3.0.3"],
        "dev": ["tox", "isort", "black"],
        "mypy": ["mypy", "types-requests"],
    }},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
"""
