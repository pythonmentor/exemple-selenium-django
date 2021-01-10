import sys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.conf.settings import BASE_DIR
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1920x1080")


class ChromeFunctionalTestCases(StaticLiveServerTestCase):
    """Functional tests using the Chrome web browser in headless mode."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(
            executable_path=f"{BASE_DIR}/webdrivers/geckodriver",
            options=chrome_options,
        )
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def setUp(self):
        User = get_user_model()
        User.objects.create_user(username="tchappui", password="openClassrooms.2020")

    def test_user_can_connect_and_disconnect(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector("#button-login").click()
        self.driver.find_element_by_css_selector("#id_username").send_keys("tchappui")
        self.driver.find_element_by_css_selector("#id_password").send_keys(
            "openClassrooms.2020"
        )
        self.driver.find_element_by_css_selector("#button-submit").click()
        logout = self.driver.find_element_by_css_selector("#button-logout")
        self.assertEqual(
            logout.text,
            "Déconnexion",
            "Disconnect button should be available.",
        )
