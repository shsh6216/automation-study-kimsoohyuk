## 1. 실행환경 준비 방법
가상환경을 생성하고 실행합니다.
python -m venv venv
.\venv\Scripts\Activate.ps1

## 2. 필요한 라이브러리 설치
pip install pytest-playwright
playwright install

## 3. 프로그램 실행 방법
chromium : 터미널에서 pytest --browser chromium 명령어를 통해 테스트를 실행할 수 있습니다.
firefox : 터미널에서 pytest --browser firefox 명령어를 통해 테스트를 실행할 수 있습니다.
webkit : 터미널에서 pytest --browser webkit 명령어를 통해 테스트를 실행할 수 있습니다.

## 4. 실패 메시지의 기대값과 실제값
expect(page).to_have_title("큐밋! SW 테스트 프로젝트 아웃소싱 플랫")
E       AssertionError: Page title expected to be '큐밋! SW 테스트 프로젝트 아웃소싱 플랫'
E       Actual value: 큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼 
E       Call log:
E         - Expect "to_have_title" with timeout 5000ms
E           13 × locator resolved to <html lang="" class="content h-screen overflow-y-scroll relative p-0">…</html>
E              - unexpected value "큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼"

## 5. 하드코딩된 URL 개수
3 line에서 URL 1개 하드코딩