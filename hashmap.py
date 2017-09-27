class HashMap(object):
	"""docstring for HashMap"""

	def __init__(self, size,probing='linear'):
		self.size = size
		self.probing = probing
		self.ctr = 1
		self.values = [None] * self.size
		self.keys = [None] * self.size

	def reset(self):
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
			self.ctr = 1
			new_idx = (old_idx + self.ctr) % self.size 
		if self.probing == 'quadratic':
			new_idx = (old_idx + self.ctr ** 2) % self.size
			self.ctr += 1
		return new_idx

	def set(self,key,value,verbose=True):
		if len([x for x in self.keys if x is not None]) == self.size:
			if verbose:
				print('Overflow!')
			return False
		self.sanity_check_key(key)
		_idx = self.hash_index(key)
		if self.keys[_idx] == None or self.keys[_idx] == key:
			self.keys[_idx] = key
			self.values[_idx] =  value
			return True
		else:
			while(True):
				_idx = self.probe(_idx)
				if self.keys[_idx] == None or self.keys[_idx] == key:
					self.keys[_idx] = key
					self.values[_idx] = value
					return True


	def get(self,key):
		if key in self.keys:
			self.sanity_check_key(key)
			_idx = self.hash_index(key)
			if self.keys[_idx] == key:
				return self.values[_idx]
			else:
				while(True):
					_idx = self.probe(_idx)
					if self.keys[_idx] == key:
						return self.values[_idx]
		else:
			raise KeyError("could'nt find key!")

	def delete(self,key):
		if key in self.keys:
			self.sanity_check_key(key)
			_idx = self.hash_index(key)
			if self.keys[_idx] == key:
				self.keys[_idx] = None
				self.values[_idx] = None
			else:
				while(True):
					_idx = self.probe(_idx)
					if self.keys[_idx] == key:
						self.keys[_idx] = None
						self.values[_idx] = None
						return
		else:
			raise KeyError("could'nt find key!")

	def load(self):
		not_none_values = sum(x is not None for x in self.values)
		return not_none_values / self.size
