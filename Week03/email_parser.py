import json

# 이메일 목록 파일 읽기
def read_email(filename):
    try:
        with open(filename, "r") as file:
            emails = file.readlines()

        new_emails = []

        for email in emails:
            new_emails.append(email.strip())

        return new_emails

    except FileNotFoundError:
        print("입력 파일이 존재하지 않음")
        return []

# 정상적인 이메일과 잘못된 데이터 구분
def check_email(email):
    if "@" not in email:
        return False
    return True

# 정상 이메일의 아이디와 도메인 분리
    parts = email.split("@")

#======================================
if __name__ == "__main__":

    emails = read_email("emails.txt")

    valid_emails = []
    invalid_emails = []
    domain_count = {}

    for email in emails:

        if check_email(email):

            # 아이디와 도메인 나누기
            parts = email.split("@")

            user_id = parts[0]
            domain = parts[1]

            valid_emails.append({
                "email": email,
                "id": user_id,
                "domain": domain
            })

            # 도메인별 이메일 개수 계산
            if domain in domain_count:
                domain_count[domain] = domain_count[domain] + 1
            else:
                domain_count[domain] = 1

        else:
            invalid_emails.append(email)

    print("정상 이메일:", valid_emails)
    print("잘못된 이메일:", invalid_emails)
    print("도메인 개수:", domain_count)


    # 분석 결과를 JSON 파일로 저장
    result = {
        "valid_emails": valid_emails,
        "invalid_emails": invalid_emails,
        "domain_count": domain_count
    }

    with open("parsed_emails.json", "w") as file:
        json.dump(result, file, indent=4)

    print("JSON 저장 완료")
