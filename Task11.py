# Напишите программу для печати всех уникальных значений в словаре.
my_dict = [{"V": "S001"},
           {"V": "S002"}, 
           {"VI": "S001"}, 
           {"VI": "S005"}, 
           {"VII": "S005"}, 
           {"V": "S005"},
           {"VIII": "S007"}]
# my_list = []
# for i in range(len(my_dict)):
#     my_list += my_dict[i].values()
# print(set(my_list)) Первый способ решения
new_list = []
for item in my_dict:
    for values in item. values():
        new_list.append(values)
        
print(set(new_list))

