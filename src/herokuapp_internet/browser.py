# Base class implementing Selenium
from requests.models import HTTPError
from selenium import webdriver
import platform
import subprocess
from pathlib import Path
import requests
import zipfile
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
ROOT_DIR = Path(__file__).absolute().parents[2]


class Browser:
    def __init__(self, browser="chrome", locale="en-US", headless=False, **kwargs):
        self._browser = browser
        self._locale = locale
        self._platform = platform.system()
        self._logs_dir = ROOT_DIR / "logs"
        self._logs_dir.mkdir(exist_ok=True)
        self._driver_parent_dir = ROOT_DIR / "sel_drivers"
        self._driver_file = None
        self.driver = None
        self._headless = headless
        self.setup_driver()

    def __del__(self):
        self.quit()

    def setup_driver(self):
        """Setup the Selenium web driver"""
        if self._browser is not "chrome":
            raise NotImplementedError("Oops! We can't use that browser, yet...")
        self._install_chromedriver()

        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument(f"--lang={self._locale}")
        driver_options.add_argument("start-maximized")
        if self._headless:
            driver_options.add_argument("headless")
        driver_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        driver_log_path = self._driver_parent_dir / "chromedriver.log"

        logger.info("Starting driver...")
        self.driver = webdriver.Chrome(
            executable_path=self._driver_file,
            options=driver_options,
            desired_capabilities=driver_capabilities,
            service_args=["--verbose"],
            service_log_path=driver_log_path,
        )

    def _get_chrome_version(self) -> str:
        """Get the version of Chrome running locally"""
        if self._platform == "Linux" or self._platform == "Darwin":
            output = subprocess.check_output("google-chrome --version", shell=True)
            chrome_version = output.decode("utf-8").strip().split()[2]
        elif self._platform == "Darwin":
            output = subprocess.check_output(
                "/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --version",
                shell=True,
            )
            chrome_version = output.decode("utf-8").strip().split()[2]
        else:
            if Path(
                "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            ).is_file:
                output = subprocess.check_output(
                    r'wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
                    shell=True,
                )
                chrome_version = output.decode("utf-8").strip().split("=")[1]
            else:
                output = subprocess.check_output(
                    r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
                    shell=True,
                )
                chrome_version = output.decode("utf-8").strip().split("=")[1]
        return chrome_version

    def _download_chromedriver(self, chrome_version: str) -> Path:
        """Downloads the chromedriver for the specified version"""
        if (
            not chrome_version
        ):  # If no Chrome version is provided we will grab the latest driver
            chrome_version = requests.get(
                "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
            ).text
        if self._platform == "Linux":
            dl_url = f"https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_linux64.zip"
            driver_filename = "chromedriver"
        elif self._platform == "Darwin":
            dl_url = f"https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_mac64.zip"
            driver_filename = "chromedriver"
        else:
            dl_url = f"https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_win32.zip"
            driver_filename = "chromedriver.exe"
        dl_zip_filename = Path(dl_url).name
        dl_zip_file = self._driver_parent_dir / dl_zip_filename
        self._driver_parent_dir.mkdir(exist_ok=True)

        # Download the zip file
        response = requests.get(dl_url)
        dl_zip_file.write_bytes(response.content)

        # Extract the zip file
        with zipfile.ZipFile(dl_zip_file, "r") as dl_zip:
            dl_zip.extract(driver_filename, self._driver_parent_dir)

        return self._driver_parent_dir / driver_filename

    def _install_chromedriver(self):
        """Download and install chromedriver"""
        if not any([
            Path(self._driver_parent_dir / "chromedriver").exists,
            Path(self._driver_parent_dir / "chromedriver.exe").exists,
        ]):
            logger.info("Installing the chromedriver")
            self._download_chromedriver(self._get_chrome_version)

    def quit(self):
        """Clean up webdriver session. Without this sessions would stack up on system."""
        logger.debug("Quitting the webdriver session.")
        self.dump_chrome_console_logs()
        self.driver.quit()

    def dump_chrome_console_logs(self):
        """Dump the chrome console logs at the end of a webdriver session"""
        logger.info("Dumping browser console logs")
        try:
            for console_entry in self.driver.get_log("browser"):
                logger.debug(console_entry)
        except HTTPError:
            # Driver connection already closed
            pass

    def get_page(self, url, port=None):
        """Get a page"""
        _url = f"{url}:{port}" if port else url
        logger.debug(f"Attempting to retrieve url: {_url}")
        self.driver.get(_url)

    def take_screenshot(self, img_name=None):
        """Take a screenshot of the current session"""
        # Create screenshot file name
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        if img_name:
            sshot_name = f"{img_name}-{timestamp}.png"
        else:
            sshot_name = f"{logger.name}-{timestamp}.png"
        sshot_folder = self._logs_dir / "screenshots"
        sshot_folder.mkdir(exist_ok=True)
        img_path = sshot_folder / img_name

        # Take the screenshot and save it to the filename
        self.driver.save_screenshot(img_path)
        logger.info(f"Saved screenshot to {img_path}")
