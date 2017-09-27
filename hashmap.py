class HashMap(object):
	"""
		A hash table class, which can map key strings to values. This can have any size
	    as long as the memory supports. In case of perfect hashing insertion and retrieval
	    using keys is O(1).

	    This class have 2 types of probing i.e linear and quadratic. Linear probing causes
	    clustering thus increasing the chances of collision, whereas quadratic clustering 
	    does not cause clustering and hence less chances of clustering.

	    However in quadratic probing there is a disdvantage. It is possible that all the
	    empty spaces are not searched, so there are two conditions which the table size of
	    quadratic probing must follow in order to ensure hitting of every empty space.
	    1. Be a prime number
	    2. never be more than half full 
	    src = 'https://cathyatseneca.gitbooks.io/data-structures-and-algorithms/tables/quadratic_probing_and_double_hashing.html'
	"""

	def __init__(self, size,probing='quadratic',verbose=True):
		if probing not in ['linear','quadratic']:
			raise ValueError('probing can only be linear or quadratic not %s'%probing)
		self.size = size
		self.probing = probing
		self.ctr = 1
		self.values = [None] * self.size
		self.keys = [None] * self.size
		self.verbose = verbose

	def reset(self):
		self.ctr = 1
		self.values = [None] * self.size
		self.keys = [None] * self.size

	def hash_index(self,key):
		_hash = key.__hash__()
		_idx = _hash & (self.size - 1) # if set to self.size it may return self.size which is out of list index!
		return _idx

	def sanity_check_key(self,key):
		if not isinstance(key,str):
			raise ValueError('Key should be of type string')

	def probe(self,old_idx):
		if self.probing == 'linear':
			new_idx = (old_idx + self.ctr) % self.size
			self.ctr += 1
		if self.probing == 'quadratic':
			new_idx = (old_idx + self.ctr ** 2) % self.size
			self.ctr += 1
		return new_idx

	def set(self,key,value):
		if self.probing == 'quadratic':
			if self.load() > 0.46: 
				if self.verbose:
					print('Overflow!')
				return False
		if self.probing == 'linear':
			if self.load() == 1: 
				if self.verbose:
					print('Overflow!')
				return False
		self.sanity_check_key(key)
		_idx = self.hash_index(key)
		if self.verbose:
			print('for key=%s Hashed_index = %d'%(key,_idx))
		if self.keys[_idx] == None or self.keys[_idx] == key:
			if self.verbose:
				print('set key=%s, value=%s, at _idx=%d'%(key,value,_idx))
			self.keys[_idx] = key
			self.values[_idx] =  value
			return True
		else:
			while(True):
				if self.verbose:
					print('%d already occupied, probing...'%(_idx,))
				_temp_idx = self.probe(_idx)
				if self.verbose:
					print(_temp_idx)
				if self.keys[_temp_idx] == None or self.keys[_temp_idx] == key:
					if self.verbose:
						print('set key=%s, value=%s, at _temp_idx=%d'%(key,value,_temp_idx))
					self.keys[_temp_idx] = key
					self.values[_temp_idx] = value
					self.ctr = 1
					return True


	def get(self,key,return_idx = False):
		if key in self.keys:
			self.sanity_check_key(key)
			_idx = self.hash_index(key)
			if self.verbose:
				print('key=%s, hash_index=%d'%(key,_idx))
			if self.keys[_idx] == key:
				if self.verbose:
					print("(without probing) key = %s found at %d with value %s"%(key,_idx,self.values[_idx]))
				if return_idx:
					return self.values[_idx],_idx
				else:
					return self.values[_idx]
			else:
				while(True):
					_temp_idx = self.probe(_idx)
					if self.verbose:
						print('key=%s probing %d to %d'%(key,_idx,_temp_idx))
					if self.keys[_temp_idx] == key:
						if  self.verbose:
							print("(After probing)key = %s found at %d with value %s"%(key,_temp_idx,self.values[_temp_idx]))
						self.ctr = 1
						if return_idx:
							return self.values[_temp_idx],_temp_idx
						else:
							return self.values[_temp_idx]
		else:
			raise KeyError("could'nt find key! '%s'"%key)

	def delete(self,key):
		_,_idx = self.get(key,return_idx=True)
		self.keys[_idx] = None
		self.values[_idx] = None

	def load(self):
		not_none_values = sum(x is not None for x in self.values)
		return not_none_values / self.size