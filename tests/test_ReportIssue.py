import pytest
from pageObjects.ReportIssuePage import ReportIssuePage
from testData.FormSubmissionData import FormSubmissionData
from utilities.BaseClass import BaseClass


class TestReportIssue(BaseClass):

    def test_report_issue(self, get_data):
        report_issue = ReportIssuePage(self.driver)
        assert "RedRabbit Staging" in self.driver.title
        print("Successfully landed on home page")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_button_by_text(get_data["property_type_button1"])
        self.click_button_by_text(get_data["fault_type_button1"])
        self.click_button_by_text(get_data["fault_type_button2"])
        self.click_button_by_text(get_data["fault_type_button3"])
        assert report_issue.get_max_issues_alert().is_displayed(), "Maximum issues reached message is not displayed"
        print("Max issues reached warning is displayed")
        report_issue.fill_in_form(get_data)
        self.click_button_by_text(get_data["fault_type_button4"])
        assert report_issue.get_max_issues_popup().is_displayed(), "Maximum issues reached pop up is not displayed"
        print("Max issues exceeded pop up is displayed")
        ref_number = self.get_text_of_element(report_issue.ref_number_element)
        report_issue.save_ref_number_to_file(ref_number)
        self.take_screenshot("Reference number.png")

    @pytest.fixture(scope="class", params=FormSubmissionData.test_form_data)
    def get_data(self, request):
        return request.param




