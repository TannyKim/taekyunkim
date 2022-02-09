# 4개 과목의 합계(전체 합계, 개인 합계) + 평균 (개인평균 / 전체 평균)
# 홍길동1 '국어' : 95, '영어' : 90, '수학' : 80, '과학': 50
# 홍길동2 '국어' : 100, '영어' : 50, '수학' : 90, '과학': 90
# 홍길동3 '국어' : 99, '영어' : 60, '수학' : 100, '과학': 40
# 홍길동4 '국어' : 55, '영어' : 80, '수학' : 80, '과학': 60

scores1 = {'국어' : 95, '영어' : 90, '수학' : 80, '과학': 50}
scores2 = {'국어' : 100, '영어' : 50, '수학' : 90, '과학': 90}
scores3 = {'국어' : 99, '영어' : 60, '수학' : 100, '과학': 40}
scores4 = {'국어' : 55, '영어' : 80, '수학' : 80, '과학': 60}

stds = [scores1, scores2, scores3, scores4]
allSum = []
allAvg = []

number = 0

while number < 4:
    idvSum = sum(stds[number].values())
    idvAvg = idvSum / len(stds)
    allSum.append(idvSum)
    allAvg.append(idvAvg)
    print("홍길동", number, "의 합계:", idvSum, "의 평균:", idvAvg)
    number = number + 1
    if number == 4:
        data1 = sum(allSum)
        data2 = sum(allSum) / (len(allSum) * 4)
        break

dataAllSum= data1 #전체합계
dataAllAvg = data2 #전체평균

#디버깅용 데이터 설정
temp = 0