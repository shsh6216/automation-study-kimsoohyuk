# 과제 2. 함수 활용 미니 프로젝트

# 구구단 출력
def gugudan(a):
    for i in range(1,11):
        print(a,"x", i,"=", a * i)

# 회문 판별
def text_check(a):
    for i in range(len(a) // 2):
        if a[i]!=a[-1 -i]:
            return "회문이 아닙니다."

    return "회문입니다"

# 단어 빈도 계산
def word_frequency(a):
    words = a.split()
    result = {}

    for word in words:
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1

    return result

# 비밀번호 검증
def password_check(a):
    if len(a) < 8:
        return "비밀번호는 6글자 이상 입력해주세요"

    check_number = False
    check_english = False

    for number in a:
        if number.isdigit():
            check_number = True

        if number.isalpha():
            check_english = True


    if check_number and check_english:
        return "사용 가능한 비밀번호입니다."

    return "비밀번호 형식이 맞지 않습니다."
