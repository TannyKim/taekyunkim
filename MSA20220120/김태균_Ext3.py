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
number = 1

for i in stds:
    print("홍길동",number, sum(i.values()), sum(i.values()) / len(stds))
    number = number + 1
    
print(sum(scores1.values())+sum(scores2.values())+sum(scores3.values())+sum(scores4.values()))
print((sum(scores1.values())+sum(scores2.values())+sum(scores3.values())+sum(scores4.values())) / 16)

temp = 0
        
