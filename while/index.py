# i = 0
# while i <= 10:
#     if i % 2 == 1: break
#     print(i)
#     i+=1

# while int(input('Enter number: ')) > 0: pass

# for i in range(5):
# #     if int(input('Enter number: ')) < 0: break

# print('Now you will be asked 2 numbers and these will be divide and you will see the answer')
# a = int(input('Enter number: '))
# b = int(input('Enter number. Note that you can not enter 0: '))
# if b == 0:
#     i = 1
#     while True:
#         if i > 3:
#              print('you stupid asshole. dont you know math')
#         else: print('please enter non-zero value')
#         b = int(input('Enter number.  Note that you can not enter 0: '))
#         if b != 0:
#             print(a / b)
#             break
#         i+=1
# else: print(a / b)    

a = int(input('Enter number: '))
while True:
    b = int(input('Enter number. Note that you can not enter 0: '))
    try: 
        print(a / b)
        break
    except:
         print('please enter non-zero value')