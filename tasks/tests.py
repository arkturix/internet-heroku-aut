from invoke import task
from pathlib import Path
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
ROOT_DIR = Path(__file__).absolute().parents[1]
TEST_DIR = ROOT_DIR / 'tests'


@task(help={
    "tests": "The file or folder from which to run tests",
    'pytestmarks': 'Run tests with the given markers. Default: smoke',
    'pytestexprs': 'Run tests by the given expressions',
    'variables': 'Path to yaml file from which to use variables. Default: tests/variables.yaml',
    'headless': 'Run browser UI tests in headless mode'
})
def runtests(ctx, tests, pytestmarks='smoke', pytestexprs='', variables=TEST_DIR / 'variables.yaml', headless="false"):
    """Run tests via pytest."""
    # Compile pytest command
    pytest_cmd = "python -m pytest --durations=0"
    if pytestmarks:
        pytest_cmd += f" -m {pytestmarks}"
    if pytestexprs:
        pytest_cmd += f" -k {pytestexprs}"
    if variables:
        pytest_cmd += f" --variables={variables}"
    pytest_cmd += f" --headless={headless} --junitxml={ROOT_DIR / 'logs' / ('junitxml-'+datetime.now().strftime('%Y%m%d-%H%M')+'.xml')} {tests}"

    # Run pytest command
    logger.debug(f"Running pytest with command: {pytest_cmd}")
    ctx.run(pytest_cmd)
