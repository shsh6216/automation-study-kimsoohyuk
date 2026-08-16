member1 = {
    "이름" : "A",
    "나이" : 30,
    "지역" : "서울"
}

member2 = {
    "이름" : "B",
    "나이" : 28,
    "지역" : "부산"
}

member3 = {
    "이름" : "C",
    "나이" : 33,
    "지역" : "인천"
}

print('이름 : ', member1['이름'],'| 나이 : ', member1["나이"], '| 지역 : ', member1["지역"])
print('이름 : ', member2['이름'],'| 나이 : ', member2["나이"], '| 지역 : ', member2["지역"])
print('이름 : ', member3['이름'],'| 나이 : ', member3["나이"], '| 지역 : ', member3["지역"])

members = [member1, member2, member3]

for member in members:
    if member["나이"] >=30:
        print('30세 이상 회원 : ', member["이름"])