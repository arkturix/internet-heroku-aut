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

Run the tests using pytest from a command prompt or terminal. The following is an example command to trigger the tests with the decorator `smoke` when the working directory is the repository root:

```bash
python -m pytest --durations=0 --variables=tests\variables.yaml -m smoke tests\
```

The tests should be platform agnostic and capable of being run on Windows, Mac, or Linux.

---

## License
[MIT](https://choosealicense.com/licenses/mit/)