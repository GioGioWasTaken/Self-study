#trying to fill knowledge gaps I have in basic python commands

#Lists: list.extend, list.copy, list.  list[i]=x,  list[1:] etc etc, list.insert, list.remove

#list1=[5,4,3]
#list2=[2,1,0]
#print(list1.extend(list2))

#Functions: You can add parameters inside a function. Example down below
#def say_hello(name):
#    print(f"Hello {name}")
#say_hello('Mike')

#functions: return statements.
#i= int(input('Enter the number you want cubed here: '))
#def squared_number(num):
#    return num * num
#print(squared_number(i))

#tuples: same as a list but the data CANNOT be changed, it is immutable.
# They are generally used for data that doesn't need to be changed, like coordinates for example
#mil_base_1=(40,400)

def find_biggest_num():
    take_nums=str(input("Please give me your numbers: "))
    nums_list_string=take_nums.split(', ')
    nums_list=[]
    for num in nums_list_string:
        num=int(num)
        nums_list.append(num)
    print('Nums list=',nums_list)
    print(type(nums_list[0]))
    list=[0]
    for a in nums_list:
        if a>list[0]:
            list.clear()
            list.append(a)
    print(list[0])

find_biggest_num()
