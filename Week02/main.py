from string_utils import Email_list
from string_utils import Text_list
from string_utils import email_change
from string_utils import email_check
from string_utils import email_masking
from string_utils import text_count
from string_utils import text_reverse

if __name__ == "__main__":
    for email in Email_list:
        A1 = email_change(email)
        A2 = email_check(A1)
        A3 = email_masking(A1)

        print('문자열 앞뒤 공백 제거 및 소문자 변환 : ',A1)
        print('이메일 형태 확인 : ',A2)
        print('이메일 일부 마스킹 : ', A3)

    for Text in Text_list:
        A4 = text_count(Text)
        A5 = text_reverse(Text)

        print('문장의 단어 개수 계산 : ', A4, '개')
        print('문자열을 반대로 변환 : ', A5)