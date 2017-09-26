import unittest
from hashmap import HashMap
import random
import math
import string

class test_hashmap(unittest.TestCase):


    def setUp(self):
        size = math.floor(random.random() * 100) + 5 # minimum size 5
        self._dict = HashMap(size)

    def test_hash_index(self):
        idx = self._dict.hash_index('divyansh')
        verify = 'divyansh'.__hash__() & (self._dict.size - 1)  # __hash__ returns different hashes for different python runs
        self.assertEqual(idx,verify)

    def test_sanity_check_key(self):
        self.assertRaises(ValueError,self._dict.sanity_check_key,23) # passed any number to raise exception
        self.assertRaises(ValueError,self._dict.sanity_check_key,[2,3,4]) # passed a list to raise exception
        self.assertRaises(ValueError,self._dict.sanity_check_key,('asd','asd')) # passed a tuple to raise exception

    def test_set(self):
        bool_true = self._dict.set('animal','monkey')
        bool_false = self._dict.set('animal','lion',verbose=False)
        self.assertEqual(bool_true,True)
        self.assertEqual(bool_false,False)
        self.assertRaises(ValueError,self._dict.set,23,'done!')

    def test_get(self):
        self._dict.set('animal','monkey')
        value = self._dict.get('animal')
        value_none = self._dict.get('bird')
        self.assertEqual(value,'monkey')
        self.assertEqual(value_none,None)

    def test_delete(self):
        self._dict.set('animal','monkey')
        self._dict.delete('animal')
        value = self._dict.get('animal')
        self.assertEqual(value,None)
        self.assertRaises(KeyError,self._dict.delete,'animal')

    def test_load(self):
        itr = math.floor(random.random() * self._dict.size)
        for i in range(itr):
            random_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
            self._dict.set(random_key,'monkey' + str(i),verbose=False)
        load_value = self._dict.load()
        self.assertLessEqual(load_value,1)



if __name__ == '__main__':
    unittest.main()
