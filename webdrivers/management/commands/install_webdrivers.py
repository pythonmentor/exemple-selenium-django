from io import BytesIO
import tarfile
from zipfile import ZipFile

from django.core.management.base import BaseCommand
from requests import get


class Command(BaseCommand):
    help = 'Installs web drivers on linux64.'

    def install_latest_chromedriver(self):
        """Downloads and unzip the latest chromedriver for linux64."""
        version = get(
            "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
        ).text
        response = get(
            "https://chromedriver.storage.googleapis.com"
            f"/{version}/chromedriver_linux64.zip"
        )
        with ZipFile(BytesIO(response.content)) as f:
            f.extractall()

    def install_latest_geckdriver(self):
        """Downloads and unzip the latest geckodriver for linux64."""
        response = get(
            "https://api.github.com/repos/mozilla/geckodriver/releases/latest"
        )
        urls = [
            asset['browser_download_url'] 
            for asset in response.json().get('assets', []) 
            if "linux64" in asset.get('name', '')
        ]
        for url in urls:
            with tarfile.open(
                fileobj=BytesIO(get(url).content), mode="r|gz"
            ) as f:
                return f.extractall()

    def handle(self, *args, **options):
        """Main entry point."""
        self.stdout.write(self.style.SUCCESS('Installing latest chromedriver.'))
        self.install_latest_chromedriver()
        self.stdout.write(self.style.SUCCESS('Installing latest geckodriver.'))
        self.install_latest_geckdriver()