# list comprehension

# names = ["nurbek", "atay", "ermek", "nargiza", "bakyt"]
# capital = []
# for name in names:                                                # 1 method
#     capital.append(name.capitalize())
# print(capital)


# names = ["nurbek", "atay", "ermek", "nargiza", "bakyt", "ermek"]          # 2 method
# capitalize_names = [name.capitalize() for name in names]

# print(capitalize_names)



# nums = range(10)
# squared_nums = [num + num for num in nums]                # сам лист комрехеншин
# print(list(nums))
# print(squared_nums)


# лист компрехеншн с помощью тернарного оператора
# users = ['Bakyt', 'Amantay', 'Atabek', 'The best', ' Syimyk']
# users_that_know_iterator = [user for user in users if user == 'Amantay']
# print(users_that_know_iterator)

# nums = [1, 2, 3, -4, 3, -6, 0, -1, 5, 8, 3]
# positive = [num for num in nums if num >= 0]
# odd_nums = [num for num in nums if num % 2 != 0 or num < 0]
# print(odd_nums)

# nums = range(100)
# numss = [num for num in nums if num % 5 == 0 or num % 3 == 0]
# print(numss)

# a = range(1, 10)
# b = a
# for num in a:
#     for num2 in b:
#         print(x*y, end = '\t')
#     print()
    
# numss = [num * num2 for num2 in b for num in a]
# print(numss)


# nums = [f'even num {num}' if num % 2 == 0 else f'odd num {num}' for num in range(20)]
# print(nums)
