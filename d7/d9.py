# numbers = input("введите числа через пробел:").split()
# numbers = list(map(int,numbers))
# print(numbers)




# ints_list = [1, 2, 3, 4, 3, 2] 
# ints_list1 = list(set(ints_list)) 
# print(ints_list1) [1, 2, 3, 4, 3, 2]


#  стандартный способ через цикл
# def countVowels(string):
#    vowels = ['a','e','i','o','u']
#    total = 0
#    for s in string:
#       if s in vowels:
#          total = 1
#    return total


a=input('Введите число от 1 до 5: ').split()


b=list(map(int,a))

print(b)
 
print(min(b))

print(max(b))
