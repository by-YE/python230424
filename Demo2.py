# Demo2.py 
# chatGPT 
# 파이썬의 List, Dict, Tuple, Set을 비교하는 코드 작성해줘

# List, Dict, Tuple, Set 생성
my_list = [1, 2, 3, 4, 5]
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_tuple = (1, 2, 3)
my_set = {3, 4, 5, 6}

# List 출력
print("List:")
print("  Length:", len(my_list))
print("  First element:", my_list[0])
print("  Last element:", my_list[-1])
print("  Elements:", my_list)

# Dict 출력
print("Dictionary:")
print("  Length:", len(my_dict))
print("  Value associated with 'a':", my_dict['a'])
print("  Elements:", my_dict)

# Tuple 출력
print("Tuple:")
print("  Length:", len(my_tuple))
print("  First element:", my_tuple[0])
print("  Last element:", my_tuple[-1])
print("  Elements:", my_tuple)

# Set 출력
print("Set:")
print("  Length:", len(my_set))
print("  Elements:", my_set)

# List, Dict, Tuple, Set 각각 반복하기
for element in my_list:
    print("List element:", element)

for key, value in my_dict.items():
    print("Dict element:", key, value)

for element in my_tuple:
    print("Tuple element:", element)

for element in my_set:
    print("Set element:", element)
