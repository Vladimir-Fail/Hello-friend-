print("\t\t----LAB 1 var 8-----\n")

def Crate_List (): #number 1
    return [i for i in range(45, 7, -3)]

def Create_Set_from_list(List): #number 2
    result = set()
    for item in List:
        if (item>=0 and item<=10): 
            result.add(item)
        
        if (len(result) == 11): 
            break

    return result
    

def Create_List_from_dict(Dict): #number 3
    List = list(Dict.values())
    return List

def Find_equals(ListA, ListB): #number 4 '''попробовать сделать через фильтр'''
    flag = True
    i = 0
    while(flag and i<len(ListA)):

        j= 0
        while (flag and j < len(ListB)):
            if (ListB[j] == ListA[i]):
                flag = False
            j+=1
        
        i+=1
    return (not flag)

'''def Find_equals_filter(ListA, ListB):
    #newlist = list(filter()
    return newlist'''

def Find_area(ListA, ListB): #number 5 
    dlina = len(ListA) 
    
    #составляем множество
    Area = set()
    for i in range(dlina):
        Area.add(ListA[i]*ListB[i])
   

    #ищем медиану
    alist = sorted(list(Area)) #нужна отсортированная выборка
    if (len(alist) % 2 == 0): #четное значение элементов
        median = (alist[(len(alist)//2) - 1] + alist[ (len(alist)//2)] ) / 2
    else:
        median = alist[len(alist)//2]
    
    #удалить лишнее из множества
    
    '''из задания: " Найти площади этих прямоугольников и записать в множество. Найти медиану площадей и удалить все значения из списка 
    меньше неё" 
    сначала нужно создать сет а потом удалить из списка? будем считать что просят оставить множество'''

    Area = set(filter( lambda x: x>= median , Area))

    #найти отношение суммы полученного сет на длину входного списка
    areasumm = 0
    for item in Area:
        areasumm+= item
    
    return areasumm/len(ListA)
    
def Clear_dict(Dict): #number 6
    #найти min and max
    
    dictvalues = list(Dict.keys())
    Min = min(dictvalues)
    Max = max(dictvalues)

    #найти среднее и очистить (использовать фильтр)
    average = (Min+ Max)/2
    remainkeys = filter(lambda x: x>= average , Dict)
    newdic = {key: Dict[key] for key in remainkeys}
    return newdic
    
def Date_from_seconds(seconds): #number 7 
    '''day = 86 400 sec,  hour = 3600sec , min = 60 sec'''
    days = seconds//86400
    seconds-=(86400*days)

    hours = seconds//3600
    seconds-=(3600*hours)

    minutes = seconds//60
    seconds-= (60*minutes)
    return days , hours , minutes, seconds



'''for number 1'''
NewList = Crate_List()
print('#1 ', NewList)

'''for number 2'''
print('\n#2 result = ', Create_Set_from_list(NewList))


''' for number 3'''
dic = {x: (x+2)**3 for x in range(5, 0, -1)}
list2 = Create_List_from_dict(dic)
print('\n#3 ', list2)
print('sorted list' , sorted(list2))


'''for number 4'''
List1 = [x for x in range(9)]
List2 = [y for y in range(5, 13)]
print('\n#4 list1:', List1, "\nlist2:", List2)
print("result = ", Find_equals(List1, List2))


'''for number 5'''
List3 = [x for x in range(1, 60, 3)]
List4 = [x for x in range(60, 1, -3)]
result5 = Find_area(List3, List4)
print('\n#5 result = ', result5)


'''for number 6'''
dict6 = {x: str(x**2) for x in range(30, 10, -2)}
dict7 = Clear_dict(dict6)
print('\n#6 исходный dict = ', dict6, '\nresult = ', dict7)


'''for number 7'''
seconds = 86400
d,h,m,s = Date_from_seconds(seconds)
print('\n#7 current date = ' , f'{d}/{h}/{m}/{s}')









