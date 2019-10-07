def add_val_to_list(val, this_list=[]):
    this_list.append(val)
    return this_list


print('----print list1----')
list1 = add_val_to_list(321)
print(list1)

print('----print list2----')
list2 = add_val_to_list(123, [])
print(list2)

print('----print list3----')
list3 = add_val_to_list('a')
print(list3)
