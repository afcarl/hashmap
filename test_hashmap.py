import unittest
from hashmap import HashMap
import random
import math
import string

class test_hashmap(unittest.TestCase):


    def setUp(self):
        size = math.floor(random.random() * 100) + 10 # minimum size 10 to avoid coflicts with line 26
        self._dict = HashMap(size)

    def test_hash_index(self):
        idx = self._dict.hash_index('divyansh')
        verify = 'divyansh'.__hash__() & (self._dict.size - 1)  # __hash__ returns different hashes for different python runs
        self.assertEqual(idx,verify)

    def test_sanity_check_key(self):
        self.assertRaises(ValueError,self._dict.sanity_check_key,23) # passed any number to raise exception
        self.assertRaises(ValueError,self._dict.sanity_check_key,[2,3,4]) # passed a list to raise exception
        self.assertRaises(ValueError,self._dict.sanity_check_key,('asd','asd')) # passed a tuple to raise exception

    def test_probe(self):
        num = self._dict.probe(5)
        self.assertEqual(num,6)
        num = self._dict.probe(self._dict.size + 3)
        self.assertEqual(num,0)

    def test_set(self):
        self.assertEqual(self._dict.set('animal','monkey'),True)
        self.assertEqual(self._dict.set('animal','lion'),True)
        self.assertRaises(ValueError,self._dict.set,23,'done!')
        self._dict.reset()
        for i in range(self._dict.size):
            self.assertEqual(self._dict.set('animal' + str(i),'monkey' + str(i)),True)
        self.assertEqual(self._dict.load(),1)
        self.assertEqual(self._dict.set('one_more_key_to_cause_overflow','monkey_n',False),False)


    def test_get(self):
        for i in range(self._dict.size):
            self._dict.set('animal' + str(i),'monkey' + str(i))
            self.assertEqual(self._dict.get('animal' + str(i)),'monkey' + str(i))
        self.assertRaises(KeyError,self._dict.get,'bird')

    def test_delete(self):
        self._dict.set('animal','monkey')
        self._dict.delete('animal')
        for i in range(self._dict.size):
            self.assertEqual(self._dict.set('animal' + str(i),'monkey' + str(i)),True)
        for i in reversed(range(self._dict.size)):
            self.assertEqual(self._dict.delete('animal' + str(i)),None)
            self.assertRaises(KeyError,self._dict.delete,'animal' + str(i))
        self.assertRaises(KeyError,self._dict.get,'animal')

    def test_load(self):
        itr = math.floor(random.random() * self._dict.size + 5)
        for i in range(itr):
            random_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
            self._dict.set(random_key,'monkey' + str(i),verbose=False)
        load_value = self._dict.load()
        self.assertLessEqual(load_value,1)


if __name__ == '__main__':
    unittest.main()
