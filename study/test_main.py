from playwright.sync_api import Page, expect

# WGMS 계정
account = {
    "id" : "shsh6216",
    "pw" : "tngur12!"}

# 골프장 : 이포CC
WGMS_URL = "https://ipocc.dev.holeinonecloud.com/auth/login"

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open_page(self):
        self.page.goto(WGMS_URL)
        
    def id_input(self):
        self.page.locator("#userId").fill(account["id"])
        
    def pw_input(self):
        self.page.locator("#password").fill(account["pw"])
        
    def login_click(self):
        self.page.locator(".Login_input").click()

    def login(self):
        self.open_page()
        self.id_input()
        self.pw_input()
        self.login_click()


class Menusearch:
    def __init__(self, page):
        self.page = page

    def menu_input(self, menu_name):
        self.page.locator(".nav-link.search").click()
        self.page.locator(".form-control.form-control-navbar").fill(menu_name)
        self.page.keyboard.press("Enter")


# 분실물등록 화면 이동
def test_lost_registration(page):
    login = LoginPage(page)
    menu = Menusearch(page)

    login.login()
    menu.menu_input("분실물등록")
