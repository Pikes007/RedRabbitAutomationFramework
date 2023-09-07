import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def click_button_by_text(self, button_text):
        try:
            button_xpath = f"//button[normalize-space()='{button_text}']" or f"//button@value='{button_text}']" or f"//label[contains(., '{button_text}')]/input[@type='radio' and @value='{button_text}']']"
            button = self.driver.find_element(By.XPATH, button_xpath)
            button.click()
            print(f"Clicked on button with text: {button_text}")
        except NoSuchElementException as e:
            print(f"Button with text '{button_text}' not found", str(e))

    def get_text_of_element(self, locator):
        element = self.driver.find_element(*locator)
        element_text = element.text
        print("Element text: ", element_text)
        return element_text

    def take_screenshot(self, filename):
        self.driver.get_screenshot_as_file(filename)

    def click_on_target_in_list(self, targeted_list, target):
        for item in targeted_list:
            if target == item.text:
                item.click()
                return True
        return False

    def hover_on_element(self, element):
        hover = self.driver.find_element(*element)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover).perform()