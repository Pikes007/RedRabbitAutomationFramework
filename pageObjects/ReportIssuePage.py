from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReportIssuePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.ref_num_list = []

    problem_location = (By.XPATH, "//input[@id='location']")
    problem_item = (By.XPATH, "//input[@id='item']")
    problem_description = (By.XPATH, "//textarea[@id='description']")
    address = (By.XPATH, "//input[@id='address']")
    client_name = (By.XPATH, "//input[@id='name']")
    client_email = (By.XPATH, "//input[@id='reporter_email']")
    client_mobile = (By.XPATH, "//input[@id='mobile']")
    comments = (By.XPATH, "//textarea[@id='comments']")
    ref_number_element = (By.XPATH, "//span[@class = 'text-indigo-600 text-lg']")
    max_issues_reached_message = (By.XPATH, "//button[normalize-space()='Maximum issues reached']")
    max_issues_reached_popup = (By.XPATH, "//p[normalize-space()='Maximum issues reached']")

    def fill_in_form(self, data):
        issue_locations = self.driver.find_elements(*ReportIssuePage.problem_location)
        issue_locations[0].send_keys(data["issue#1_location"])
        issue_locations[1].send_keys(data["issue#2_location"])
        issue_locations[2].send_keys(data["issue#3_location"])
        issue_descriptions = self.driver.find_elements(*ReportIssuePage.problem_description)
        issue_descriptions[0].send_keys(data["issue#1_description"])
        issue_descriptions[1].send_keys(data["issue#2_description"])
        issue_descriptions[2].send_keys(data["issue#3_description"])
        self.driver.find_element(*ReportIssuePage.address).send_keys(data["physical_address"])
        self.driver.find_element(*ReportIssuePage.client_name).send_keys(data["form_name"])
        self.driver.find_element(*ReportIssuePage.client_email).send_keys(data["email_address"])
        self.driver.find_element(*ReportIssuePage.client_mobile).send_keys(data["form_mobile"])
        self.driver.find_element(*ReportIssuePage.comments).send_keys(data["comments"])
        self.click_button_by_text("Submit")

    def get_max_issues_alert(self):
        return self.driver.find_element(*ReportIssuePage.max_issues_reached_message)

    def get_max_issues_popup(self):
        return self.wait.until(EC.visibility_of_element_located(self.max_issues_reached_popup))

    def save_ref_number_to_file(self, entry):
        self.ref_num_list.append(entry)

        with open("C:\\Users\\Hello\\PycharmProjects\\pythonSeleniumTraining\\redRabbitStaging\\testData\\ReferenceNumbers.py", "r") as file:
            lines = file.readlines()
        ref_num_list_end = lines.index("    ]\n")
        lines.insert(ref_num_list_end, f"        '{entry}',\n")

        with open("C:\\Users\\Hello\\PycharmProjects\\pythonSeleniumTraining\\redRabbitStaging\\testData\\ReferenceNumbers.py", "w") as file:
            file.writelines(lines)
