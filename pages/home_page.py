from playwright.sync_api import Page, expect

class HomePage:

    def __init__(self, page:Page):

        self.page=page

        # ===== Locators =====
        # Using Playwright's 'locator' method to identify UI elements
        self.lnk_my_account = page.locator('span:has-text("My Account")')
        self.lnk_register = page.locator('a:has-text("Register")')
        self.lnk_login = page.locator('a:has-text("Login")')
        self.txt_search_box = page.locator('input[placeholder="Search"]')
        self.btn_search = page.locator('#search button[type="button"]')


    def get_home_page_title(self) ->str:
        title=self.page.title()
        return title

    def click_my_account(self):
        try:
            self.lnk_my_account.click()
        except Exception as e:
            print(f"Exception while clicking 'My Account':{e}")
            raise

    def click_register(self):
        try:
            self.lnk_register.click()
        except Exception as e:
            print( f"Exception while clicking 'Register': {e}")
            raise

    def click_login(self):
        try:
            self.lnk_login.click()
        except Exception as e:
            print(f"Exception while clicking 'Login': {e}")
            raise

    def enter_product_name(self, product_name:str):
        try:
            self.txt_search_box.fill(product_name)
        except Exception as e:
            print(f" Exception while entering product name: {e}")
            raise

    def click_search(self):
        try:
            self.btn_search.click()
        except Exception as e:
            print(f"Exception while click search button: {e}")
            raise

