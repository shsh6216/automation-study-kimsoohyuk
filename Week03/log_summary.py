import json

# 이메일 목록 파일 읽기
def read_test_name(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            test_names = file.readlines()

        new_test_name = []

        for test_name in test_names:
            test_name = test_name.strip()

            if test_name:
                new_test_name.append(test_name)

        return new_test_name

    except FileNotFoundError:
            print("존재하지 않는 파일입니다.")
            exit()


#======================================
if __name__ == "__main__":
    test_names = read_test_name("test_log.txt")

    total_count = 0
    pass_count = 0
    fail_count = 0
    fail_tests = []

    for test in test_names:
        parts = test.split(",")

        Date = parts[0].strip()
        Test_name = parts[1].strip()
        result = parts[2].strip()

        if len(parts) != 3:
            print("잘못된 데이터 : ", test)
            continue
        if Date == "" or Test_name == "" or result == "":
            print("잘못된 데이터 :", test)
            continue
        if result != "PASS" and result != "FAIL":
            print("잘못된 데이터 :", test)
            continue

        total_count = total_count + 1

        if result == "PASS":
            pass_count = pass_count + 1

        elif result == "FAIL":
            fail_count = fail_count + 1
            fail_tests.append(Test_name)

    success_rate = pass_count / total_count * 100

    print("전체 테스트 수 : ", total_count)
    print("PASS 개수 :", pass_count)
    print("FAIL 개수 : ", fail_count)
    print("테스트 성공률 : ", success_rate, "%")
    print("실패한 테스트 : ", fail_tests)

    result = {
        "total_count": total_count,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "success_rate": success_rate,
        "fail_tests": fail_tests
    }

    with open("summary.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)