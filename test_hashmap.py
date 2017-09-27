import unittest
from hashmap import HashMap
import random
import math
import string

class test_hashmap(unittest.TestCase):
    """
    Test class for class Hashmap

    In all the quadratic probing tests unexpected errors can occur, for example
    if size of hashmap is small even one element can fill up a significant amount
    of size of the hashmap. Therefore I didn't use loop testing in quadratic probing
    it was causing random errors! 
    """


    def setUp(self):
        size = math.floor(random.random() * 30) + 30 # minimum size 15 to avoid coflicts with line 26
        self._dict = HashMap(size,probing='quadratic',verbose=False)

    def test_hash_index(self):
        idx = self._dict.hash_index('divyansh')
        verify = 'divyansh'.__hash__() & (self._dict.size - 1)  # __hash__ returns different hashes for different python runs
        self.assertEqual(idx,verify)

    def test_sanity_check_key(self):
        self.assertRaises(ValueError,self._dict.sanity_check_key,23) # passed any number to raise exception
        self.assertRaises(ValueError,self._dict.sanity_check_key,[2,3,4]) # passed a list to raise exception
        self.assertRaises(ValueError,self._dict.sanity_check_key,('asd','asd')) # passed a tuple to raise exception

    def test_probe_linear(self):
        self._dict.probing = 'linear'
        num = self._dict.probe(5)
        self.assertEqual(num,6)
        self._dict.ctr = 1
        num = self._dict.probe(self._dict.size + 3)
        self.assertEqual(num,4)

    def test_probe_quadratic(self):
        self._dict.probing = 'quadratic'
        self.assertEqual(self._dict.probe(5),6)
        self.assertEqual(self._dict.probe(6),10)
        self.assertEqual(self._dict.probe(1),10)
        self._dict.reset()
        self.assertEqual(self._dict.probe(self._dict.size -1),0)
        self.assertEqual(self._dict.probe(self._dict.size - 1),3)


    def test_set_quadratic(self):
        self.assertEqual(self._dict.set('animal','monkey'),True)
        self.assertEqual(self._dict.set('animal','lion'),True)
        self.assertRaises(ValueError,self._dict.set,23,'twenty_three')

    def test_set_linear(self):
        self._dict.probing = 'linear'
        self.assertEqual(self._dict.set('animal','monkey'),True)
        self.assertEqual(self._dict.set('animal','lion'),True)
        self.assertRaises(ValueError,self._dict.set,23,'twenty_three')
        self._dict.reset()
        for i in range(self._dict.size):
            self.assertEqual(self._dict.set('animal' + str(i),'monkey' + str(i)),True)
        self.assertEqual(self._dict.load(),1)
        self.assertEqual(self._dict.set('one_more_key_to_cause_overflow','monkey_n'),False)


    def test_get_quadratic(self):
        self.probing = 'quadratic'
        self.assertEqual(self._dict.set('animal' + str(3),'monkey' + str(3)),True)
        self.assertEqual(self._dict.get('animal' + str(3)),'monkey' + str(3))
        self.assertRaises(KeyError,self._dict.get,'bird')

    def test_get_linear(self):
        self._dict.probing = 'linear'
        for i in range(self._dict.size):
            self.assertEqual(self._dict.set('animal' + str(i),'monkey' + str(i)),True)
        for i in reversed(range(self._dict.size)):
            self.assertEqual(self._dict.get('animal' + str(i)),'monkey' + str(i))
        self.assertRaises(KeyError,self._dict.get,'bird')

    def test_delete_quadratic(self):
        self._dict.probing = 'quadratic'
        self._dict.set('animal','monkey')
        self._dict.delete('animal')
        self.assertRaises(KeyError,self._dict.get,'animal')

    def test_delete_linear(self):
        self._dict.probing = 'linear'
        self._dict.set('animal','monkey')
        self._dict.delete('animal')
        for i in range(self._dict.size):
            self.assertEqual(self._dict.set('animal' + str(i),'monkey' + str(i)),True)
        for i in reversed(range(self._dict.size)):
            self.assertEqual(self._dict.delete('animal' + str(i)),None)
            self.assertRaises(KeyError,self._dict.delete,'animal' + str(i))
        self.assertRaises(KeyError,self._dict.get,'animal')

    def test_load_quadratic(self):
        self.probing = 'quadratic'
        itr = math.floor(random.random() * self._dict.size/2 + 5)
        for i in range(itr):
            random_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
            self._dict.set(random_key,'monkey' + str(i))
        load_value = self._dict.load()
        self.assertLessEqual(load_value,0.6)

    def test_load_linear(self):
        self.probing = 'linear'
        itr = math.floor(random.random() * self._dict.size + 5)
        for i in range(itr):
            random_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
            self._dict.set(random_key,'monkey' + str(i))
        load_value = self._dict.load()
        self.assertLessEqual(load_value,1)



if __name__ == '__main__':
    unittest.main()
