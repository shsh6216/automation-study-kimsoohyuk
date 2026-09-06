import os
from dotenv import load_dotenv

load_dotenv()

login_id = os.getenv("ID")
login_password = os.getenv("PASSWORD")
base_url = os.getenv("URL")

if not login_id:
    print("ID 없음")
elif not login_password:
    print("PASSWORD 없음")
elif not base_url:
    print("URL 없음")
else:
    print("ID:", login_id)
    print("PASSWORD: 미출력")
    print("URL:", base_url)