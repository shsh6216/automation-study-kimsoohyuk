# 이메일 리스트
Email_list = [" TEST01@GMail.COM    ",
              "   TeST02@NAVER.COM  ",
              "test031234 "]

# 문장 리스트
Text_list = ["안녕하세요 저는 김수혁입니다",
             "테스트 중입니다"]

# 문자열 앞뒤 공백 제거 및 소문자 변환
def email_change(a):
    return a.strip().lower()

# 이메일 형태 확인
def email_check(a):
    domains = ["@gmail.com", "@naver.com"]

    for domain in domains:
        if domain in a:  
            return "이메일입니다."

    return "이메일이 아닙니다."
        

# 이메일 일부 마스킹
def email_masking(a):
    if "@" in a:
        masking = "*" * a.index("@") + a[a.index("@"):]
        return masking

# 문장의 단어 개수 계산
def text_count(a):
    return len(a.split())

# 문자열을 반대로 변환
def text_reverse(a):
    return a[::-1]