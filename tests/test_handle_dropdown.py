from playwright.sync_api import Page, expect

def test_handle_dropdown(page: Page):
    page.goto("example.com")  # Replace with the actual URL containing the dropdown
    dropdown=page.locator("#country-select")

    dropdown.select_option(label="India")

    dropdown.select_option(value="IN")

    dropdown.select_option(index=2)
    expect(dropdown).to_have_text("India")


def test_handle_multiple_dropdown(page: Page):
    page.goto("example.com")  # Replace with the actual URL containing the multiple dropdowns
    dropdown=page.locator("#country-select")
    dropdown.select_option(label=["India","USA","UK"])
    dropdown.select_option(value=["IN","US","UK"])


def test_custom_dropdown(page:Page):
    page.goto("example.com")  # Replace with the actual URL containing the custom dropdown
    page.locator("#custom-dropdown").click()
    page.locator(".dropdown-item").filter(has_text="India").click()
    page.locator(".dropdown-item", has_text="India").click()


def test_verify_dropdown_options(page:Page):
    page.goto("example.com")  # Replace with the actual URL containing the dropdown
    all_dropdown_options=page.locator("#country-select>option").all_text_contents()

    assert "India" in all_dropdown_options
    assert "USA" in all_dropdown_options

