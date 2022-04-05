
from invoke import task
import os

source_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "src")

@task
def qt(c):
    """
    Generate all py files from ui files.
    Need to run every time the .ui file of GUI is modified.
    """
    component_dir = os.path.join(source_dir, "gui", "components")

    for filename in os.listdir(component_dir):
        if filename.endswith(".ui"):
            full_path = os.path.join(component_dir, filename)
            c.run(f"pyuic5 {full_path} -o {full_path.replace('.ui', '.py')}")

@task
def start(c):
    """
    Start the program
    """
    main_path = os.path.join(source_dir, "main.py")
    c.run(f"python {main_path}")

@task
def lint(c):
    """
    Run pylint
    """
    c.run("pylint src", pty=True)

@task
def test(c):
    """
    Run tests on the application
    """
    c.run("pytest src", pty=True)

@task
def coverage(c):
    """
    Run test coverage
    """
    c.run("coverage run --branch -m pytest", pty=True)

@task
def coverage_report(c):
    """
    Generate HTML test coverage report.
    """
    c.run("coverage html", pty=True)

