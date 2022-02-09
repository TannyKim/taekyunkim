# 1.딕셔너리를 이용해서 평균 점수 구하기
scores = {'국어': 95, '영어': 90, '수학': 80, '과학' : 50}

data1 = sum(scores.values()) / len(scores)

# 2.셋을 이용해서 1~100까지 숫자 중에 공배수를 구함: 5와 3의 공배수 구하고, 합집합을 구하기
comMulti5 = {i for i in range(0, 101) if i % 5 == 0}
comMulti3 = {j for j in range(0,101) if j % 3 == 0}

comMulti5W3 = comMulti5 | comMulti3

# 3. 리스트 데이터: 7,5,3,1,-1,-3,-5,-7 출력: range활용할 것
data2 = list(range(7, -8, -2))

# 4. 4번째의 결과를 튜플로 변경(형변환)
data3 = tuple(data2)

#디버깅용 변수 설정
temp = 0
