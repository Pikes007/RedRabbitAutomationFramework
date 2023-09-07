from selenium.webdriver.common.by import By
from pageObjects.AdminDashboardPage import AdminDashboardPage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    sign_in_banner = (By.XPATH, "//h2[normalize-space()='Sign in to your account']")
    email_box = (By.XPATH, "//input[@id='email']")
    password_box = (By.XPATH, "//input[@id='password']")
    incorrect_login_message = (By.XPATH, "//strong[normalize-space()='Your email or password is incorrect']")

    def get_sign_in_banner(self):
        return self.driver.find_element(*SignInPage.sign_in_banner)

    def perform_sign_in(self, data):
        self.driver.find_element(*SignInPage.email_box).send_keys(data["email_address"])
        self.driver.find_element(*SignInPage.password_box).send_keys(data["password"])
        self.click_button_by_text("Sign in")
        admin_dashboard = AdminDashboardPage(self.driver)
        success = admin_dashboard.is_logged_in()
        return success, admin_dashboard

    def get_incorrect_login_message(self):
        message = self.wait.until(EC.visibility_of_element_located(self.incorrect_login_message))
        message_text = message.text
        return message_text
