from io import BytesIO
import json
import tarfile
from urllib.request import urlopen
from zipfile import ZipFile

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Installs web drivers on linux64.'

    def install_latest_chromedriver(self):
        """Downloads and unzip the latest chromedriver for linux64."""
        version = urlopen(
            "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
        ).read().decode()
        response = urlopen(
            "https://chromedriver.storage.googleapis.com"
            f"/{version}/chromedriver_linux64.zip"
        )
        with ZipFile(BytesIO(response.read())) as f:
            f.extractall(path='/usr/local/bin')

    def install_latest_geckdriver(self):
        """Downloads and unzip the latest geckodriver for linux64."""
        response = urlopen(
            "https://api.github.com/repos/mozilla/geckodriver/releases/latest"
        )
        urls = [
            asset['browser_download_url'] 
            for asset in json.loads(response.read())['assets'] 
            if "linux64" in asset['name']
        ]
        with tarfile.open(fileobj=urlopen(urls[0]), mode="r|gz") as f:
            f.extractall(path='/usr/local/bin')

    def handle(self, *args, **options):
        """Main entry point."""
        self.stdout.write(self.style.SUCCESS('Installing latest chromedriver.'))
        self.install_latest_chromedriver()
        self.stdout.write(self.style.SUCCESS('Installing latest geckodriver.'))
        self.install_latest_geckdriver()