from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class LinkAssetTicket(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    asset_box = (By.XPATH, "(//input[@placeholder='Start typing to search assets, addresses or linked contacts'])[2]")
    select_lease_box = (By.XPATH, "//input[contains(@placeholder,'Select Lease')]")
    tenant_box = (By.XPATH, "//input[@placeholder='Start typing to search tenants']")
    assign_to_box = (By.XPATH, "//input[@placeholder='Start typing to search users']")
    reporting_method_box = (By.XPATH, "//input[@placeholder='Select Reporting Source']")
    list_of_assets = (By.XPATH, "//div[@class='flex items-center gap-x-2'][span]")
    list_of_tenants = (By.XPATH, "//li[@class = 'el-select-dropdown__item h-auto  selected hover']")
    list_of_assignees = (By.XPATH, "//li[contains (@class ,'el-select-dropdown__item h-auto')]")
    radio_buttons = (By.XPATH, "// div[ @class ='px-2 flex items-center space-x-2'] // div // label")
    search_service_providers = (By.XPATH, "//input[@placeholder='Search Service Providers To Task']")
    list_of_service_providers = (By.XPATH, "//span[@class='mr-1']")


    def get_list_of_assets(self):
        self.driver.find_element(*LinkAssetTicket.asset_box).click()
        asset_list = self.driver.find_elements(*LinkAssetTicket.list_of_assets)
        return asset_list

    def get_list_of_assignees(self):
        self.driver.find_element(*LinkAssetTicket.assign_to_box).click()
        assignee_list = self.driver.find_elements(*LinkAssetTicket.list_of_assignees)
        return assignee_list

    def get_list_of_reporting_methods(self):
        self.driver.find_element(*LinkAssetTicket.reporting_method_box).click()
        i = 21
        reporting_methods_list = []
        while i < 29:
            method_location = f"(//li[contains(@class, 'el-select-dropdown__item')])[{i}]"
            reporting_method = self.driver.find_element(By.XPATH, method_location)
            reporting_methods_list.append(reporting_method)
            i += 1
        return reporting_methods_list

    def get_list_of_tenants(self):
        self.driver.find_element(*LinkAssetTicket.tenant_box).click()
        assignee_list = self.driver.find_elements(*LinkAssetTicket.list_of_tenants)
        return assignee_list

    def click_radio_button(self, text):
        buttons = self.driver.find_elements(*LinkAssetTicket.radio_buttons)
        self.click_on_target_in_list(buttons, text)
        print(f"Clicked on radio button with text {text}")

    def get_list_of_service_providers(self):
        self.driver.find_element(*LinkAssetTicket.search_service_providers).click()
        list_of_providers = self.driver.find_elements(*LinkAssetTicket.list_of_service_providers)
        return list_of_providers
