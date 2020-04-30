from io import BytesIO
import tarfile
from zipfile import ZipFile

from requests import get
from invoke import task


def install_latest_chromedriver():
    """Downloads and unzip the latest chromedriver for linux64."""
    response = get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
    response = requests.get(
        "https://chromedriver.storage.googleapis.com"
        f"/{response.text}/chromedriver_linux64.zip"
    )
    with ZipFile(BytesIO(response.content)) as f:
        f.extractall()

def install_latest_geckdriver():
    response = get(
        "https://api.github.com/repos/mozilla/geckodriver/releases/latest"
    )
    urls = [
        asset['browser_download_url'] 
        for asset in response.json()['assets'] 
        if "linux64" in asset['name']
    ]
    with tarfile.open(fileobj=BytesIO(get(urls[0]).content), mode="r|gz") as f:
        f.extractall()

@task
def install_webdrivers(c):
    install_latest_chromedriver()
    install_latest_geckdriver()