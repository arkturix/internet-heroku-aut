# internet-heroku-aut
Test automation for the-internet.herokuapp.com website using Python 3.6.

---

## Requirements

Python 3.6 is required for this automation to run using pytest.

The required packages can be found in the `requirements.txt` file in the repository. Use of a Python virtual environment (venv) is recommended. Installing the requirements can be achieved by running:

```bash
python -m pip install -r requirements.txt
```

Google Chrome is currently the only supported browser, and the chromedriver is required by Selenium.

---

## Usage

Run the tests via a pyinvoke task by invoking the the runtests command from a command prompt or terminal in the project virtual environment. The following is an example of running this:

```bash
invoke runtests tests
```

The default pytest mark used by this command is `smoke`, but other marks could be supplied. More information on the various arguments that could be passed:

```
Usage: inv[oke] [--core-opts] runtests [--options] [other tasks here ...]

Docstring:
  Run tests via pytest.

Options:
  -h STRING, --headless=STRING      Run browser UI tests in headless mode
  -p STRING, --pytestmarks=STRING   Run tests with the given markers. Default: smoke
  -t STRING, --tests=STRING         The file or folder from which to run tests
  -v, --variables                   Path to yaml file from which to use variables. Default: tests/variables.yaml
  -y STRING, --pytestexprs=STRING   Run tests by the given expressions


```

The tests should be platform agnostic and capable of being run on Windows, Mac, or Linux.

---

## Future Work

This project has a lot of potential to show of Python Selenium test skills. Several items should be considered for future work on this project:

- Better logging utility
- More page objects and test cases for other pages on the site
- Better test reports

---

## License
[MIT](https://choosealicense.com/licenses/mit/)
