x = 3-4j #복소수
print(x.imag) #허수부
print(x.real) #실수부
print(x.conjugate()) #켤레복소수
print(type (2**31))# 2의 31제곱
#type binding - 파이썬의 경우는 동적으로 타입이 바뀐다. dynamic type binding c의 경우 한번 타입을 선언하면 바꾸기 위해서는 캐스팅이 필요함.
# 단점 - 타입을 혼동하기 쉬움.
r = 2
circle_area = 3.14*(r**2)
x=3
y=4
triangle_area = x*y/2
print(circle_area,triangle_area)
#평소에는 튜플이나 세트로 값을 저장만 해놓고 있다가 값을 다룰 떄 리스트로 바꿔서 다룬다.
#파이썬은 스크립트 언어라서 실행할 때 자료형을 결정한다. 그래서 자료형이 자유롭다.
d = dict(a=1,b=3,c=5)
print(d)
print(d['b']) #액세스할때 키를 주어야 한다.
