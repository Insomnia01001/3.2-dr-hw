# import random
# import string
# users =['Bobur', 'Davron', 'Ilhom']
# upper_words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
#     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
#     'U', 'V', 'W', 'X', 'Y', 'Z']
# lower_words = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
#     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
#     'u', 'v', 'w', 'x', 'y', 'z'
#    ]
# pas_nums = ['1','2','3','4','5','6','7','8','9','0']
# pas_ = ['@','#','$','_','-','&']
# random1=random.choice(upper_words)
# random2= random.choice(lower_words)
# random3= random.choice(pas_nums)
# random4= random.choice(pas_)




# def func1 (text1):
#     dict1 = {}
#     for i in text1:
#       dict1[i]=random1 +random2+random3+random4
#     return dict1
# result1 = func1(text1=users)
# print(result1)
# for j in users:
#      dict1[j]=randomson
# print(dict1)
# import random
# import string

# def generate_passwords(names):
#     password_dict = {}
    
#     for name in names:
#         # 4 ta tasodifiy raqam olish
#         numbers = ''.join(random.choices(string.digits, k=4))
#         # 4 ta tasodifiy harf olish
#         letters = ''.join(random.choices(string.ascii_lowercase, k=4))
#         # Parolni birlashtiramiz
#         password = numbers + letters
#         # Dictionaryga qo'shamiz
#         password_dict[name] = password
    
#     return password_dict

# # Foydalanish
# names_list = ['Bobur', 'Davron', 'Ilhom']
# result = generate_passwords(names_list)
# print(result)


# inp1 = int(input("enter number : "))

# def res(son):
#     yigindi=0
#     if son <=0:
#         print("enter musnat son yani 0+")
#     for i in range(1,son+1):
#         if son %i ==0:
#             yigindi+=i
#     return yigindi
# result1 = res(son=inp1)
# print(result1)



# 3
inp1 = int(input("enter number: "))
def sonlar_func(son):
    boluvchi= []
    if son<=0:
        print("enter musbat son")
    for i in range(1,son+1):
        if son%i==0:
            boluvchi.append(i)
    print(f"{son}ni boluvchilari {len(boluvchi)}ta")
    return boluvchi
result1 = sonlar_func(son=inp1)
print(result1)