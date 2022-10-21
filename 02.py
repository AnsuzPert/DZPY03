# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
per1 = input('ВВедите строку чисел: ')
per1 = per1.split()
j = 0
i =-1
per2 =[]
while j < len(per1)/2:
    if  per1[i]==per1[j]:
        per2.append(int(per1[i]))
    else:
        per2.append(int(per1[j])*int(per1[i]))
    j+=1
    i-=1
print(per1)
print(per2)