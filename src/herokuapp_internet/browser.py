# Base class implementing Selenium
import selenium
import platform
import subprocess
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class Browser:

    def __init__(
        self,
        browser='chrome',
        locale='en-US',
        **kwargs
    ):
        self._browser = browser
        self._locale = locale
        self._platform = platform.system()

    def setup_driver(self):
        if self._browser is not 'chrome':
            raise NotImplementedError("Oops! We can't use that browser, yet...")
        self._install_chromedriver()

    def _get_chrome_version(self) -> str:
        """Get the version of Chrome running locally"""
        if self._platform == 'Linux' or self._platform == 'Darwin':
            output = subprocess.check_output(
                "google-chrome --version",
                shell=True
            )
            chrome_version = output.decode('utf-8').strip().split()[2]
        else:
            if Path("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe").is_file:
                output = subprocess.check_output(
                    r'wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
                    shell=True
                )
                chrome_version = output.decode('utf-8').strip().split('=')[1]
            else:
                output = subprocess.check_output(
                    r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
                    shell=True
                )
                chrome_version = output.decode('utf-8').strip().split('=')[1]
        return chrome_version
        
    def _install_chromedriver(self):
        if self._platform == 'Linux' or self._platform == 'Darwin':
            pass
        else:
            pass

