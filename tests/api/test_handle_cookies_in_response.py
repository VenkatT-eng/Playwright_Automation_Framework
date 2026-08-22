from playwright.sync_api import Playwright

from tests.api.test_booking_curd_e2e import request_context


def test_handle_cookies_in_response(playwright: Playwright):
    request_context=playwright.request.new_context()
    response=request_context.get("https://www.google.com/")

    assert response.status_text=="OK"
    assert response.status==200

    # Extract all teh cookies from the response
    cookies=request_context.storage_state()["cookies"]

    for cookie in cookies:
        print(f"Cookie Name:", {cookie["name"]}, "Cookie Value:", {cookie["value"]}, "Domain:", {cookie["domain"]})

        # Check if 'AEC' cookie is exist
        aec_cookie=None

        for cookie in cookies:
            if cookie["name"]=="AEC":
                aec_cookie=cookie
                break
        assert aec_cookie is not None, "AEC cookie not found in the response"

        # Printing details of 'AEC' Cookie
        print(aec_cookie["name"])
        print(aec_cookie["value"])
        print(aec_cookie["domain"])
        print(aec_cookie["path"])
        print(aec_cookie["expires"])




