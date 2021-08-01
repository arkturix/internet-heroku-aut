from invoke import task
from pathlib import Path
import logging

logger = logging.getLogger(__name__)
ROOT_DIR = Path(__file__).absolute().parents[1]
TEST_DIR = ROOT_DIR / 'tests'


@task(help={
    'pytestmarks': 'Run tests with the given markers',
    'pytestexprs': 'Run tests by the given expressions',
    'variables': 'Path to yaml file from which to use variables. Default: tests/variables.yaml',
    'headless': 'Run browser UI tests in headless mode'
})
def runtests(ctx, pytestmarks, pytestexprs, variables=TEST_DIR / 'variables.yaml', headless=False):
    pass
