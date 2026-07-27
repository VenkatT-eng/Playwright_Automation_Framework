from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        # ===== Locators =====
        # Using CSS selectors to locate elements on the Login page.
        self.txt_email_address = page.locator('#input-email')
        self.txt_password = page.locator('#input-password')
        self.btn_login = page.locator('input[value="Login"]')
        self.txt_error_message = page.locator('.alert.alert-danger.alert-dismissible')

# ===== Action Methods =====
    # These methods represent user interactions on the Login Page.

    def set_email(self,email:str):
        try:
            self.txt_email_address.fill(email)
        except Exception as e:
            print(f"Exception while entering email: {e}")
            raise

    def set_password(self, password:str):
        try:
            self.txt_password.fill(password)
        except Exception as e:
            print(f" Exception while entering password: {e}")
            raise

    def click_login(self):
        try:
            self.btn_login.click()
        except Exception as e:
            print(f" Exception while clicking on login button:{e}")
            raise

    def login(self, email:str, password:str):
        """
                Perform the complete login operation:
                1. Enter email
                2. Enter password
                3. Click the Login button
                """
        self.set_email(email)
        self.set_password(password)
        self.click_login()

    def get_login_error(self):
        """
                Return the error message element if login fails.
                Example use:
                    error_text = login_page.get_login_error().inner_text()
                """
        try:
            return self.txt_error_message
        except Exception as e:
            print(f"Exception while fetching log error message: {e}")
            return None
