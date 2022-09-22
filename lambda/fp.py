a = map(lambda x: x*2, [2,3])
print(tuple(a))

b = map(str, [1, 2])
print(tuple(b))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

first_it = [2, 3]
second_it = [4, 2, 6, 7]

print(list(map(lambda x: x*2, first_it)))

print(list(map(pow, first_it, second_it)))

print(list(map(lambda x,y: x-y, first_it, second_it)))

print(list(filter(lambda x: x>5, second_it)))

def f(a, b, c):
   return a + b + c
print(list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300])))