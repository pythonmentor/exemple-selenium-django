from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True

firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True


class ChromeFunctionalTestCases(StaticLiveServerTestCase):
    """Functional tests using the Chrome web browser in headless mode."""

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(self.live_server_url)

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        User = get_user_model()
        User.objects.create_user(username="tchappui", password="openClassrooms.2020")
        

    def tearDown(self):
        self.driver.close()

    def test_user_can_connect_and_disconnect(self):
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys("tchappui")
        self.driver.find_element_by_css_selector('#id_password').send_keys("openClassrooms.2020")
        self.driver.find_element_by_css_selector('#button-submit').click()
        logout = self.driver.find_element_by_css_selector('#button-logout')
        self.assertEqual(logout.text, "Déconnexion", "Disconnect button should be available.")

    def test_database_uses_postgresql(self):
        self.assertIn("postgresql", settings.DATABASES['default']['ENGINE'], "Database must be postgresql")



class FirefoxFunctionalTestCases(StaticLiveServerTestCase):
    """Functional tests using the Firefox web browser in headless mode."""

    def setUp(self):
        self.driver = webdriver.Firefox(firefox_options=firefox_options)
        self.driver.get(self.live_server_url)

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        User = get_user_model()
        User.objects.create_user(username="tchappui", password="openClassrooms.2020")
        

    def tearDown(self):
        self.driver.close()

    def test_user_can_connect_and_disconnect(self):
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys("tchappui")
        self.driver.find_element_by_css_selector('#id_password').send_keys("openClassrooms.2020")
        self.driver.find_element_by_css_selector('#button-submit').click()
        logout = self.driver.find_element_by_css_selector('#button-logout')
        self.assertEqual(logout.text, "Déconnexion", "Disconnect button should be available.")