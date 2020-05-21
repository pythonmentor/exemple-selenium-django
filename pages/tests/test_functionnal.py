from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True


class ChromeFunctionalTestCases(StaticLiveServerTestCase):
    """Functional tests using the Chrome web browser in headless mode."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDown(self):
        super().tearDownClass()
        self.driver.quit()

    def setUp(self):
        User = get_user_model()
        User.objects.create_user(
            username="tchappui", password="openClassrooms.2020"
        )

    def test_user_can_connect_and_disconnect(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "tchappui"
        )
        self.driver.find_element_by_css_selector('#id_password').send_keys(
            "openClassrooms.2020"
        )
        self.driver.find_element_by_css_selector('#button-submit').click()
        logout = self.driver.find_element_by_css_selector('#button-logout')
        self.assertEqual(
            logout.text,
            "Déconnexion",
            "Disconnect button should be available.",
        )


class FirefoxFunctionalTestCases(StaticLiveServerTestCase):
    """Functional tests using the Firefox web browser in headless mode."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox(firefox_options=firefox_options)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDown(self):
        super().tearDownClass()
        self.driver.quit()

    def setUp(self):
        User = get_user_model()
        User.objects.create_user(
            username="tchappui", password="openClassrooms.2020"
        )

    def test_user_can_connect_and_disconnect(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "tchappui"
        )
        self.driver.find_element_by_css_selector('#id_password').send_keys(
            "openClassrooms.2020"
        )
        self.driver.find_element_by_css_selector('#button-submit').click()
        logout = self.driver.find_element_by_css_selector('#button-logout')
        self.assertEqual(
            logout.text,
            "Déconnexion",
            "Disconnect button should be available.",
        )
