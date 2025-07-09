import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage

@pytest.mark.usefixtures("setup_teardown")
class TestContact:
    def test_send_contact_message(self):
        home_page = HomePage(self.driver)
        home_page.click_element(home_page.CONTACT_LINK)
        contact_page = ContactPage(self.driver)
        alert_text = contact_page.click_send_message("test@example.com", "Test Name", "This is a test message.")
        assert "Thanks for the message!!" in alert_text


