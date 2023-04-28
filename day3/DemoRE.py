# DemoRE.py
import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())


# 함정을 추가
# result = re.search("[0-9]*th", "  35th")
# print(result)
# print(result.group())

# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

#----------------------------------
result = re.search("apple", "this is apple")
print(result.group())
result = re.search("\d{4}", "올해는 2023년입니다.")
print(result.group())
result = re.search("\d{5}", "우리동네는 324235")
print(result.group())
