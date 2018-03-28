color = {'apple':'red','banana':'yellow'}
color["apple"] = "green"

for v in color.values():
    print(v)
for k in color.keys():
    print(k)

for k,v in color.items():
    print(k,v)

del color['apple']
print(color)
color.clear()
print(color)
a = {'age':40.5,'job':[1,2,3],'name':{'kim':2,'cho':1}} # 순서는 중요하지 않다.
for i in a.items():
    print(i)

a = [1,2,3]
b=a #얕은 복사
a[0]=38
print(a)
print(b)
print(id(a))
print(id(b))

a = [1,2,3]
b = a[:] #깊은 복사
a[0]=38
print(a)
print(b)
print(id(a))
print(id(b))

def Times(a=10,b=20):  # default 값을 넣을 수 있다.
    return a*b

print(Times(20))

def greet(name):
    return "hello {}".format(name)
greet_someone = greet #변수나 데이터 구조안에 담을 수 있다.
print(greet_someone("Kpu Game Dept"))

def change_name_greet(func): #다른 함수에 인자로 전달 할 수 있다.
    name = "Narae"
    return func(name)

print(change_name_greet(greet))

def greeting(name):
    def greet_message(): #함수안에 함수를 정의할 수 있다.
        return 'hello'
    return "{} {}".format(greet_message(),name)
print(greeting("Kpu Game Dept"))

def uppercase(func):
    def wrapper(name):
        result =func(name)
        return result.upper()
    return wrapper #함수가 다른 함수를 생성할 수 있다. 함수의 반환 값이 될 수 있다.

new_greet = uppercase(greet)
print(new_greet("dddsssafsf"))

def compose_greet_func(name): #내부함수는 외부함수를 접근할 수 있다.
    def get_message():
        return "Hello "+name+"!"
    return get_message

greet = compose_greet_func("KPU GAME DEPT")
print(greet())