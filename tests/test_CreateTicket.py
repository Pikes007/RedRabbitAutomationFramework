import time
import pytest
from pageObjects.SignInPage import SignInPage
from pageObjects.LinkAssetTicket import LinkAssetTicket
from testData.FormSubmissionData import FormSubmissionData
from utilities.BaseClass import BaseClass


class TestCreateTicket(BaseClass):

    def test_create_ticket(self, get_data):
        sign_in = SignInPage(self.driver)
        success, admin_dashboard = sign_in.perform_sign_in(get_data)
        if success:
            maintenance_requests_page = admin_dashboard.click_maintenance_tab()
            ticket = maintenance_requests_page.locate_ref_number_in_maintenance_requests_list("MR235")
            self.click_button_by_text("Create Ticket")
            self.click_on_target_in_list(ticket.get_list_of_assets(), "Aroma Park Village 1")
            self.click_on_target_in_list(ticket.get_list_of_tenants(), "Tenant")
            self.click_on_target_in_list(ticket.get_list_of_assignees(), "Administrator Administrator")
            ticket.click_radio_button("High")
            self.click_on_target_in_list(ticket.get_list_of_reporting_methods(), "Website")
            self.click_button_by_text("Next")
            self.click_button_by_text("Next")
            self.click_button_by_text("Next")
            self.click_on_target_in_list(ticket.get_list_of_service_providers(), "ABC Plumbing")
            self.click_button_by_text("Next")
            self.click_button_by_text("Create")
            time.sleep(2)
            self.take_screenshot("TicketCreated.png")
        else:
            self.driver.quit()

    @pytest.fixture(scope="class", params=FormSubmissionData.test_sign_in_data)
    def get_data(self, request):
        return request.param
