# # #List
# thislist=["apple",True,"apple",10,24.50]
# print(type(thislist))
# thislist.append(True)
# print(thislist[0])
# print(thislist[2])
# thislist.pop()
# thislist.clear()
# # thislist.remove(24.5)
# thislist.reverse()
# index_list=thislist.index(24.5)
# count_list=thislist.count("apple")
# print(index_list)
# thislist.extend(['pineapple','pens',33])
# print(count_list)
# print(thislist)

# #Tuples
# my_tuple=('melons','pear',3.23,False,67,'pear')
# # print(my_tuple)
# # print(type(my_tuple))
# count_tuple=my_tuple.count('pear')
# index_tuple=my_tuple.index(3.23)
# # print(count_tuple)
# # no1=(2,4,6)
# # no2=(1,3,5)
# # num=no1+no2
# # print(num)
# # print(index_tuple)

# #Dictionary
# my_dict={'pear':3,'apple':2,'orange':5,'AC':True,'name':'Dave'}
# # print(type(my_dict))
# # print(my_dict['AC'])
# # my_dict['tomatoes']=13 #to add a new entry to a dictionary
# # my_dict['orange']=8
# # my_dict.pop('orange')
# # del my_dict['AC']
# print(my_dict(3))


student={'person1':'Mjay',
         'person2': {'name':'kaddy','age':17,'course':{'Python':'Begin','HTML':3}},
        'person3':{'name':'dave','course':'Python'} }
print(student['person2']['course']['Python'])
print(student['person2'][3])