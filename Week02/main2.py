from test_utils import gugudan
from test_utils import text_check
from test_utils import word_frequency
from test_utils import password_check
from string_utils import email_change




if __name__ == "__main__":
    number = int(input("1. 구구단 출력 : "))

    gugudan(number)

    text = input("2. 회문 판별 : ")
    check_result = text_check(text)

    print(check_result)

    word = input("3. 단어 빈도 계산 : ")
    word_result = word_frequency(word)

    print(word_result)

    password = input("4. 비밀번호 검증 : ")
    password_result = password_check(password)

    print(password_result)

    name_list = [" GRAPE", "     APpLE  ", "  bANANa    "]
    name_result = []

    for name in name_list:
        name_result.append(email_change(name))

    name_result.sort()
    print("5. 이름 목록 정리 : ", name_result)

# 6. 간단한 메뉴 프로그램
    data_list = []
    while True:
        print("1. 데이터 추가")
        print("2. 데이터 조회")
        print("3. 프로그램 종료")

        choice = input("선택 : ")

        if choice == "1":
            data = input("데이터 추가 : ")
            data_list.append(data)

        elif choice =="2": 
            print("데이터 조회 : ", data_list)

        elif choice =="3":
            print("프로그램 종료")
            break


