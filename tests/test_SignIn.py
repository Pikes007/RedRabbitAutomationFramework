import pytest
from pageObjects.SignInPage import SignInPage
from testData.FormSubmissionData import FormSubmissionData
from utilities.BaseClass import BaseClass


class TestReportIssue(BaseClass):

    def test_sign_in(self, get_data):
        sign_in = SignInPage(self.driver)
        assert "Sign in to your account" in self.driver.page_source
        print("Landed on sign in page")
        success, admin_dashboard = sign_in.perform_sign_in(get_data)

        if success:
            print("Successful sign in - landed on administrator dashboard")
            self.take_screenshot("SuccessfulLogIn.png")
            admin_dashboard.log_out()
            assert "Sign in to your account" in self.driver.page_source

        else:
            assert sign_in.get_incorrect_login_message() in self.driver.page_source
            print("Incorrect email or password warning displayed")
            self.take_screenshot("IncorrectEmailOrPassword.png")

    @pytest.fixture(scope="class", params=FormSubmissionData.test_sign_in_data)
    def get_data(self, request):
        return request.param
