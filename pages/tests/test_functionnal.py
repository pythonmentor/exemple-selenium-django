from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model

from selenium import webdriver

User = get_user_model()

options = webdriver.ChromeOptions()
options.add_argument('headless')

class ChromeFunctionalTestCases(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get(self.live_server_url)

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        User.objects.create_user(username="tchappui", password="openClassrooms.2020")
        

    def tearDown(self):
        self.driver.close()

    def test_user_can_connect_and_disconnect(self):
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys("tchappui")
        self.driver.find_element_by_css_selector('#id_password').send_keys("openClassrooms.2020")
        self.driver.find_element_by_css_selector('#button-submit').click()
        logout = self.driver.find_element_by_css_selector('#button-logout')
        self.assertEqual(logout.text, "Déconnexion")