# DictionaryOfString.py
# Dictionary(사전): 키(Key)와 값(Value)의 쌍으로 컬렉션을 관리
nickNames = { "Taeyo": "태오" }
nickNames["RedPlus"] = "레드플러스"
print(nickNames)
print(nickNames["Taeyo"])

redplus = {}
redplus["fname"] = '용준'
redplus["lname"] = '박'
print(redplus)

itist = { "fname": '상훈', 'lname': "한"}
print(itist)

people = [ redplus, itist ]
people.append({ 'fanme': '태영', 'lname': '김'})
print(people)
print(people[0:2])
