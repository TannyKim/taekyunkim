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

for i in stds:
    idvSum = sum(i.values())
    idvAvg = idvSum / len(i)
    allSum.append(idvSum)
    allAvg.append(idvAvg)
    if len(stds) == 4:
        print('홍길동{}의 합계는:'.format(stds.index(i)+1), int(idvSum), "평균은", int(idvAvg))

#전체 합계
data1 = sum(allSum)

#전체평균
data2 = sum(allSum) / (len(allSum) * 4)

#디버깅용 변수 설정
temp = 0
    
    