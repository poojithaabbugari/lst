#l = [1,False,"honey",19.9]
#print(len(l))


'''change list items'''

#1.change item value,an item in the list are replaced by another item
#p = ["india","usa","australia"]
#p[1] = "japan"
#print(p)
#output : ['india', 'japan', 'australia']


#2.change a range of item values
#p = ["india","usa","australia","uk","germany"]
#p[2:4] = ["japan","spain"]
#print(p)
#output : ['india', 'usa', 'japan', 'spain', 'germany']
#p[1:2] = ["swizerland","nepal"]
#print(p)
#output is ['india','swizerland','nepal','australia','uk','germany']
#p[1:3] = ["israel"]
#print(p)
#output is ['india','israel','uk','germany']

#insert,we can add items at any place in the list
#p = ["india","usa","australia","uk","germany"]
#p.insert(1,'israel')
#print(p)
#output : ["india","usa","australia","uk","germany"]

#3.Add list items
#append items ,items are added  only at the end of list
#p = ["india","usa","australia","uk","germany"]
#p.append("israel")
#print(p)
#['india','usa','australia','uk','germany','israel']

#extend list method,to append elements from another list to the current list,elements are added at the end of the list,we can add tuple,set,dictionary to the list
#s = [201,202,203,204]
#h = [4,5,6,7]
#s.extend(h)
#print(s)
#output is [201, 202, 203, 204, 4, 5, 6, 7]
#s = [201,202,203,204]
#h = (4,5,6,7) tuple
#s.extend(h)
#print(s)
#output is [201, 202, 203, 204, 4, 5, 6, 7]
#s = [201,202,203,204]
#h = {4,5,6,7}
#s.extend(h)
#print(s)
#output is [201, 202, 203, 204, 4, 5, 6, 7]

"""s = [201,202,203,204]
h = {"shravya":4,"sindhu":5,"sneha":6,"likitha":7}
s.extend(h)
print(s)"""


#4.remove list items
#Remove,cannot empty a list — it only removes one specific element at a time.
#r = ["doremon","nobitha","shezuka","dekisugi","sunio","jiyan","doremi"]
#r.remove("dekisugi")
#print(r)
#output is ['doremon', 'nobitha', 'shezuka', 'sunio', 'jiyan', 'doremi']
#r = ["doremon","nobitha","shezuka","dekisugi","sunio","jiyan","doremi","dekisugi"]
#r.remove("dekisugi")
#print(r),if the list has duplicate item(dekusugi) then 1st item(dekisugi)is removed,another duplicate(dekisugi)item remains in the list
#['doremon', 'nobitha', 'shezuka', 'sunio', 'jiyan', 'doremi', 'dekisugi']

#pop,by using pop method we can remove items at any index
#a = ['hi',"hello",'namaskaram','vanakam']
#a.pop(0)
#print(a)
#output :['hello', 'namaskaram', 'vanakam']
#a = ['hi',"hello",'namaskaram','vanakam']
#a.pop(),if we don't specify the index(pop(1),it will remove only last element)
#print(a)
#output:['hi', 'hello', 'namaskaram']

#delete,it is a keyword,it can delete the whole list,removes the item at specified index
#v = ["neem",'alovera',"eucalyptus"]
#del v[1]
#print(v)
#output : ['neem', 'eucalyptus']
#v = ["neem",'alovera',"eucalyptus"]
#del v ,we don't get any output becoz the entire list is deleted

#clear,The clear() method empties the list.
#y = ["jackma","sundharpichai","jeff bezos","elonmusk"]
#y.clear()
#print(y)
#the output is [],(it displays empty list,without content)


#5.loop lists
#You can loop through the list items by using a for loop:
#y = ["mr.beast","nirmalpillai","abhishek"]
#for x in y:
#   print(x)
#output is
# mr.beast
#nirmalpillai
#abhishek

#Loop Through the Index Numbers
#a = ["apple", "banana", "cherry"]
#for i in range(len(a)):
# print(a[i])
#output is apple
#banana
 #cherry
