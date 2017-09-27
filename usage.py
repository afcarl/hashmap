from hashmap import HashMap

my_dict1 = HashMap(100,probing='quadratic')
my_dict1.set('animal','lion')
print("obj=mydict1, key = animal, value = %s"%my_dict1.get('animal'))

my_dict2 = HashMap(10,'linear')
my_dict2.set('animal','monkey')
print("obj=mydict2, key = animal, value = %s"%my_dict2.get('animal'))