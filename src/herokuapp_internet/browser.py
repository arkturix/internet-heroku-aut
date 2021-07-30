# Base class implementing Selenium
from os import PathLike
import selenium
import platform
import subprocess
from pathlib import Path
import requests
import zipfile
import logging

logger = logging.getLogger(__name__)
ROOT_DIR = Path(__file__).absolute().parents[2]


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
        self._driver_parent_dir = ROOT_DIR / 'sel_drivers'
        self._driver_file = None
        self._driver = None

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
        elif self._platform == 'Darwin':
            output = subprocess.check_output(
                '/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --version',
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

    def _download_chromedriver(self, chrome_version: str) -> Path:
        """Downloads the chromedriver for the specified version"""
        if not chrome_version:  # If no Chrome version is provided we will grab the latest driver
            chrome_version = requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE").text
        if self._platform == 'Linux':
            dl_url = f"https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_linux64.zip"
            driver_filename = 'chromedriver'
        elif self._platform == 'Darwin':
            dl_url = f"https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_mac64.zip"
            driver_filename = 'chromedriver'
        else:
            dl_url = f"https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_win32.zip"
            driver_filename = 'chromedriver.exe'
        dl_zip_filename = Path(dl_url).name
        dl_zip_file = self._driver_parent_dir / dl_zip_filename

        # Download the zip file
        response = requests.get(dl_url)
        dl_zip_file.write_bytes(response.content)

        # Extract the zip file
        with zipfile.ZipFile(dl_zip_file, 'r') as dl_zip:
            dl_zip.extract(driver_filename, self._driver_parent_dir)

        return self._driver_parent_dir / driver_filename
        
    def _install_chromedriver(self):
        """Download and install chromedriver"""
        if not Path(self._driver_parent_dir / 'chromedriver').exists or not Path(self._driver_parent_dir / 'chromedriver.exe').exists:
            logger.info("Installing the chromedriver")
            self._download_chromedriver(self._get_chrome_version)

