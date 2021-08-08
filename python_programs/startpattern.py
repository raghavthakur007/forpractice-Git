# li =[int(x)  for x in input("Enter the number for comparison :").split(",")]
# print(li)
# print(li[0])
# i = 0
# for i in range(0,len(li)-1):
#     large_value = 0
#     if li[i]>li[i+1]:
#         large_value = li[i]
#     else:
#         large_value = li[i+1]
# """"another """
# max = li[0]
# for i in li :
#     if max <i:
#         max = i
#

# print(large_value)


def threasd_func():
    for i in range(10):
        print("Thread A"+str(i))

def thread2_func():
    for i in range(50):
        print("Thread B"+ str(i))


t1 =threadding.threading(target = Thread thread2_func())
t2 = 