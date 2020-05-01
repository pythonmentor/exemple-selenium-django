from io import BytesIO
from subprocess import run

from django.core.management.base import BaseCommand
from requests import get


class Command(BaseCommand):
    help = 'Downloads webdrivers'

    def install_latest_chromedriver(self):
        """Downloads the latest chromedriver for linux64."""
        version = get(
            "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
        ).text
        url = (
            "https://chromedriver.storage.googleapis.com"
            f"/{version}/chromedriver_linux64.zip"
        )
        with open('chromedriver.zip', 'wb') as f:
            f.write(get(url).content)
        return run(['sudo', 'unzip', 'chromedriver.zip', '-d', '/usr/local/bin'])

    def install_latest_geckdriver(self):
        """Downloads the latest geckodriver for linux64."""
        response = get(
            "https://api.github.com/repos/mozilla/geckodriver/releases/latest"
        )
        urls = [
            asset['browser_download_url'] 
            for asset in response.json().get('assets', []) 
            if "linux64" in asset.get('name', '')
        ]
        for url in urls:
            with open('geckodriver.tar.gz', 'wb') as f:
                f.write(get(url).content)
            return run(
                ['sudo', 'tar', '-xvzf', 'geckodriver.tar.gz', '-C', '/usr/local/bin']
            )

    def handle(self, *args, **options):
        """Main entry point."""
        self.stdout.write(self.style.SUCCESS('Installing latest chromedriver.'))
        self.install_latest_chromedriver()
        self.stdout.write(self.style.SUCCESS('Installing latest geckodriver.'))
        self.install_latest_geckdriver()