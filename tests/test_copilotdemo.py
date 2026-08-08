
from playwright.sync_api import Page, expect, Playwright


def test_search(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()
    page.fill("input[name='q']", "Playwright Python")
    page.press("input[name='q']", "Enter")
    page.wait_for_selector("text=Playwright Python")
    #Q: get the url of the first search result
    first_result_url = page.locator("h3").first.evaluate("node => node.parentElement.href")
    print(f"First search result URL: {first_result_url}")


