import json

try:
    fileName = open("datalab\\mydata.json", mode="rb")
    tempData = json.load(fileName)
    reusltData1 = tempData["name"]
    reusltData2 = tempData["age"]
    reusltData3 = tempData["address"]
    reusltData4 = tempData["email"]
    reusltData5 = tempData["empcheck"]
except IndexError as idxEr:
    error = str(idxEr)
except Exception as idxEr:
    error = str(idxEr)
finally:
    print(reusltData1, reusltData2, reusltData3, reusltData4, reusltData5)
    fileName.close()

jsonData1 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }

#한글이 이상함
try:
    fileName1 = open("datalab\\mydata2.json", mode="w")
    json.dump(jsonData1, fileName1, ensure_ascii= False)
except Exception as error:
    print("오류 : " + error)
else:
    fileName1.close()
    
#한글을 완벽히 처리
try:
    fileName2 = open("datalab\\mydata3.json", mode="w", encoding="utf-8")
    json.dump(jsonData1, fileName2, ensure_ascii= False)
finally:
    fileName2.close()

# 한글이 문제가 있음
try:
    fileName3 = open("datalab\\mydata4.json", mode="w")
    json.dump(jsonData1, fileName3, ensure_ascii= False, indent = 4)
finally:
    fileName3.close()

# 한글을 완벽히 처리  
try:
    fileName4 = open("datalab\\mydata5.json", mode="w", encoding="utf-8")
    json.dump(jsonData1, fileName4, ensure_ascii= False, indent = 4)
finally:
    fileName4.close()

#디버깅 변수 선언함(임시)
temp = 0