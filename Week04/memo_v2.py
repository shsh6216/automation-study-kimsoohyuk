import json
import os
from dotenv import load_dotenv

load_dotenv()

memo_file = os.getenv("MEMO", "memos.json")

# 메모 저장
def save_memos(memos):
    with open(memo_file, "w", encoding="utf-8") as file:
        json.dump(memos, file, ensure_ascii=False, indent=4)

def load_memos():
    try:
        with open(memo_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("메모 파일 없음")
        return
    except json.JSONDecodeError:
        print("JSON 형식이 잘못됨")
        return
#======================================
if __name__ == "__main__":
    memos = load_memos()
    
    memo = input("메모 입력 : ")
    memos.append(memo)
    save_memos(memos)
    print("메모 추가 완료")

# 전체 메모 조회
    print("입력된 메모 : ",memos)

# 특정 내용 검색
    search = input("검색할 내용 : ")

    found = False

    for memo in memos:
        if search in memo:
            print(memo)
            found = True

    if not found:
        print("검색 내용 없음")
