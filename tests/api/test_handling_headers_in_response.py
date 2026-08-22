from playwright.sync_api import Playwright

def test_handle_headers(playwright: Playwright):
    request_context=playwright.request.new_context()
    response=request_context.get("https://tutorialsninja.com/demo/)")

    assert response.status_text=="OK"
    assert response.status==200

    headers=response.headers

    for key, value in headers.items():
        print(f"{key}: {value}")



    #validate specific headers values
    assert "text/html" in headers.get("content-type")
    assert "gzip" in headers.get("content-encoding")


    #validate specific header presence
    assert "keep-alive" in headers.get("connection")
    assert "OCSESSID" in headers.get("set-cookie")


    assert "date" in headers
    assert "content-length" in headers

