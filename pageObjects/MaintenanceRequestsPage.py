import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from pageObjects.LinkAssetTicket import LinkAssetTicket


class MaintenanceRequestsPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    maintenance_requests_list = (By.XPATH, "//span[@class='hover:text-indigo-600']")
    scroll_next_list = (By.XPATH, "//button[6]//*[name()='svg']")
    scroll_next_list_again = (By.XPATH, "//button[7]//*[name()='svg']")
    flag_item = (By.XPATH, "//div[@class='text-gray-600']")

    def locate_ref_number_in_maintenance_requests_list(self, target_number, current_page=1):

        if current_page == 1:
            next_page_button = self.wait.until(EC.element_to_be_clickable(self.scroll_next_list))
        else:
            next_page_button = self.driver.find_element(*MaintenanceRequestsPage.scroll_next_list_again)

        while True:
            flag_item = self.driver.find_element(*MaintenanceRequestsPage.flag_item)
            current_flag_text = flag_item.text.split()
            elements = self.wait.until(EC.presence_of_all_elements_located(self.maintenance_requests_list))
            found = self.click_on_target_in_list(elements, target_number)

            if current_flag_text[3] == current_flag_text[5]:
                if found:
                    print(f"Ref number {target_number} found")
                    ticket = LinkAssetTicket(self.driver)
                    return ticket
                else:
                    print("Reached the end of list, ref number not found")
                    break

            if found:
                print(f"Ref number {target_number} found.")
                ticket = LinkAssetTicket(self.driver)
                return ticket

            next_page_button.click()
            time.sleep(1)
