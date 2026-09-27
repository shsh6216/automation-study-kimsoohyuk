from playwright.sync_api import Page, expect

URL = "https://v369.dev.l-walk.com"

def test_title(page:Page):
    page.goto(URL)
    expect(page).to_have_title("큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼")

def test_button(page:Page):
    page.goto(URL)
    expect(page.get_by_role("button", name="회원가입")).to_be_visible()

def test_menu(page:Page):
    page.goto(URL)
    page.get_by_role("button", name="회원가입").click()
    expect(page.get_by_text("회원가입을 위해 정보를 입력해주세요.")).to_be_visible()