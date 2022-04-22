![GitHub Actions](https://github.com/ArttuLe/ot-harjoitustyo/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/ArttuLe/ot-harjoitustyo/branch/master/graph/badge.svg?token=qjFDb0OLRG)](https://codecov.io/gh/ArttuLe/ot-harjoitustyo)

# Ohjelmistotekniikka, Harjoitustyö

## Documentation

### [Hour reporting](https://github.com/ArttuLe/ot-harjoitustyo/blob/master/documents/Hours.md)

### [ChangeLog](https://github.com/ArttuLe/ot-harjoitustyo/blob/master/documents/ChangeLog.md)

### [Project Definition](https://github.com/ArttuLe/ot-harjoitustyo/blob/master/documents/ProjectDefinition.md)

### [User Guide](https://github.com/ArttuLe/ot-harjoitustyo/blob/master/documents/UserGuide.md)

### [Architechture](https://github.com/ArttuLe/ot-harjoitustyo/blob/master/documents/ApplicationArchitechture.md)

### [Test Documentation](https://github.com/ArttuLe/ot-harjoitustyo/blob/master/documents/TestDocument.md)

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

## Misc.

The sudoku data is obtained from a Kaggle dataset containing 3 million sudoku puzzles.
The application has 30000 of these puzzles in use.

[The dataset](https://www.kaggle.com/datasets/radcliffe/3-million-sudoku-puzzles-with-ratings?resource=download)
