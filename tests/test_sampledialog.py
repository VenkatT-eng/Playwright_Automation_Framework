import pytest
from playwright.sync_api import Page, expect


def test_sample_dialog(page: Page):
    page.goto("https://tesautomationpractice.blogspot.com/")

    def handle_dialog(dialog):
        page.wait_for_timeout(5000)
        dialog.accept()  # Accept the dialog

        page.on("dialog", handle_dialog)  # Register the dialog handler
        page.locator("button[onclick='myFunction()']").click()  # Trigger the dialog
        page.wait_for_timeout(5000)  # Wait for the dialog to appear

    def test_handle_dialog2(page: Page):

        page.goto("https://tesautomationpractice.blogspot.com/")

        page.on("dialog", lambda dialog: dialog.accept())
        page.wait_for_timeout(5000)
        page.locator("button[onclick='myFunction()']").click()  # Trigger the dialog
        page.wait_for_timeout(5000)  # Wait for the dialog to appear

    def test_handle_confirm_dialog(page: Page):
        page.goto("https://tesautomationpractice.blogspot.com/")

        page.on("dialog", lambda dialog: dialog.accept())
        page.wait_for_timeout(5000)
        page.on("dialog", lambda dialog: dialog.dismiss())
        page.wait_for_timeout(5000)

        page.locator("#confirm").click()  # Trigger the confirm dialog
        page.wait_for_timeout(5000)

        text=page.locator("#demo").inner_text()

        expect(page.locator("#demo")).to_have_text("You pressed OK!")
        page.wait_for_timeout(5000)



