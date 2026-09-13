import json
import sys

# 메모 저장
def save_memos(memos):
    with open("memos.json", "w", encoding="utf-8") as file:
        json.dump(memos, file, ensure_ascii=False, indent=4)

def load_memos():
    try:
        with open("memos.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("추가한 메모 없음")
        return []
    except json.JSONDecodeError:
        print("JSON 형식이 잘못됨")
        return []
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
            print("검색한 내용과 일치하는 메모 : ", memo)
            found = True

    if not found:
        print("검색 내용 없음")
