from playwright.sync_api import Page, expect

# 1. 가상 환경 생성 .venv\Scripts\activate.ps1  
# 2. 실행 명령어 pytest --headed  

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

    def login_pass(self):
        expect(self.page.get_by_role("button", name="로그아웃")).to_be_visible()

    def login(self):
        self.open_page()
        self.id_input()
        self.pw_input()
        self.login_click()
        self.login_pass()


class Menusearch:
    def __init__(self, page):
        self.page = page

    def menu_input(self, menu_name, target_name=None):
        search = self.page.locator(".form-control.form-control-navbar")

        self.page.locator(".nav-link.search").click()
        search.fill(menu_name)
        search.press("Enter")

        if target_name is None:
            target_name = menu_name

        popup = self.page.locator(".modal-content:visible")

        if popup.is_visible():
            popup.locator('td[role="gridcell"]:nth-child(3)').get_by_text(target_name).click()
            popup.locator(".btn.btn-primary.btn-sm").click()

        menu_title = self.page.locator('a[href="/views/oto/olf/olf010"]').inner_text()
        if menu_title == target_name:
            return True

        return False

# 분실물등록 > 날짜 입력에 어제 날짜 입력
def date_input(page):
    page.locator("#btnStartDate").click()
    page.locator(".daterangepicker:visible").locator('li[data-range-key="어제"]').click()

def test_study(page):
    login = LoginPage(page)
    menu = Menusearch(page)

    login.login()
    menu.menu_input("분실물등록")
    menu.menu_input("골프","골프일마감") #골프일마감 화면 이동
    menu.menu_input("분실물등록") #분실물등록 화면 재이동

    date_input(page)