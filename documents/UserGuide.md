

# User Guide

## Install dependencies

User must install all the required dependencies for the program to run.

Installation of dependencies is done with command

```sh
poetry install
```

## Running the program

After having installed the dependencies, the program can be started with a command

```sh
poetry run invoke start
```

## Running tests

```sh
poetry run invoke test
```

## Running pylint

```sh
poetry run invoke lint
```

## Generating test coverage and coverage-report

Test coverage

```sh
poetry run invoke coverage
```

Coverage report

```sh
poetry run invoke coverage-report
```

## Running auto-formatting on the code

```sh
poetry run invoke format
```