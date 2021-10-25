days= { 'Mon', 'Tue', 'Wed','Thu'}
enum_days = enumerate(days)
# print(list(enum_days))
# print(type(enum_days))
# print(list(enum_days))
# converting it to alist
# print(list(enum_days))
#
# changing the default counter to 5
# enum_days = enumerate(days, 5)
# print(list(enum_days))

# for enum_days in enumerate(days):
#     print(enum_days.index(2))

mylist = [1,2,3,4]
# for i in range(0, len(mylist)):
#     print("Next number is: {}".format(mylist[i-1]))
for x in enumerate(days):
    print(x.index())