import pytest
from playwright.sync_api import expect, Page, Playwright


def test_commands(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://tutorialsninja.com/demo/")
    expect(page).to_have_title("Your Store")
    page.frame_locator("iframe[name='gdpr-consent-notice']").get_by_role("button", name="Accept All").click()
    page.get_by_role("link", name="My Account").click()
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("E-Mail Address").click()


    page.get_by_label("Uploads files").set_input_files("testdata/pdffile.pdf")
    page.get_by_label("Uploads files").set_input_files(
        files=[{"name": "pdffile.pdf", "mimeType": "application/pdf", "buffer": b"%PDF-1.4\n%..." }],)

    page.get_by_label("Uploads files").set_input_files(["file1.pdf", "file2.pdf"])

    page.get_by_label("I agree to the Privacy Policy").check()
    expect(page.get_by_label("Subscribe to our newsletter!")).to_be_checked()


    ##dropdown values selection
    page.get_by_label("Select your country").select_option("India")
    page.get_by_label("Select your country").select_option(value="India")
    page.get_by_label("Select your country").select_option(label="India")


    ##Mouse click
    page.get_by_role("button").click()
    page.get_by_role("button").dblclick()
    page.get_by_role("button").click(button="right")
    page.get_by_text("Item").click(modifiers=["Control"])
    page.get_by_text("Item").hover()
    page.get_by_text("Item").click(position={ "x": 10, "y": 10})

    page.get_by_role("button").click(force=True)


    ##Keys and shortcuts
    page.get_by_role("textbox").press("Enter")
    page.get_by_role("textbox").press("Control+A")
    page.get_by_role("textbox").press("Control+C")


    ##drag and drop

    page.locator("#item-to-be-dragged").drag_to(page.locator("#item-to-drop-at"))

    page.locator("#item-to-be-dragged").hover()
    page.mouse.down()
    page.locator("item-to-drop-at").hover()
    page.mouse.up()


    ##Scrolling
    page.get_by_role("button").click()
    page.get_by_text("Footer Text").scroll_into_view_if_needed()







