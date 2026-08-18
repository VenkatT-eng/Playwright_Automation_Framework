from playwright.sync_api import Playwright, expect, Page

def test_login(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://demo.opencart.com/")

    myframe=page.frame_locator("#my-iframe-id")
    myframe.fill("#username", "myusername")
    myframe.fill("#password", "mypassword")
    myframe.click("#login-button")


def test_nested_frame(page:Page):
    page.goto("https://the-internet.herokuapp.com/nested_frames")
    top_frame=page.frame_locator("frame[name='frame-top']")

    left_inner_txt=page.frame_locator("frame[name='frame-left']").locator("body").inner_text()
    print(f"Left Frame Text:", {left_inner_txt})


    nested_frame_locator=page.frame_locator("frame[name='frame-top']").frame_locator("frame[name='frame-bottom']").locator("body").inner_text()
    print(f"Nested Frame Text:", {nested_frame_locator})


