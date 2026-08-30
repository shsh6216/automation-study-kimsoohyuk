import json
import sys

# 메모 저장
def save_memos(memos):
    with open("memos.json", "w") as file:
        json.dump(memos, file, indent=4)

#======================================
if __name__ == "__main__":
    memos = []
    
    memo = input("메모 입력 : ")
    memos.append(memo)
    save_memos(memos)
    print("메모 추가 완료")

# 전체 메모 조회
    for memo in memos:
        print(memo)

# 특정 내용 검색
    search = input("검색할 내용 : ")

    for memo in memos:
        if search in memo:
            print(memo)
