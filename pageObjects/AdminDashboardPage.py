from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.MaintenanceRequestsPage import MaintenanceRequestsPage
from utilities.BaseClass import BaseClass


class AdminDashboardPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    log_out_button = (By.XPATH, "//button[@value='Log Out']")
    admin_menu = (By.XPATH, "//span[@class='text-xl font-medium leading-none mr-1']")
    maintenance_tab = (By.XPATH, "//span[contains(text(),'Maintenance')][1]")
    maintenance_button = (By.XPATH, "//a[contains(text(),'Maintenance Requests')]")

    def is_logged_in(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.admin_menu))
            return True
        except:
            return False

    def log_out(self):
        self.driver.find_element(*AdminDashboardPage.admin_menu).click()
        self.click_button_by_text("Logout")

    def click_maintenance_tab(self):
        self.hover_on_element(AdminDashboardPage.maintenance_tab)
        self.driver.find_element(*AdminDashboardPage.maintenance_button).click()
        maintenance_request_page = MaintenanceRequestsPage(self.driver)
        return maintenance_request_page



