import json

# 이메일 목록 파일 읽기
def read_test_name(filename):
    try:
        with open(filename, "r") as file:
            test_names = file.readlines()

        new_test_name = []

        for test_name in test_names:
            new_test_name.append(test_name.strip())

        return new_test_name

    except FileNotFoundError:
            print("입력 파일이 존재하지 않음")
            return []


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

    with open("summary.json", "w") as file:
        json.dump(result, file, indent=4)

    