class HashMap(object):
	"""docstring for HashMap"""
	def __init__(self, size):
		self.size = size
		self.values = [None] * self.size
		self.keys = []

	def hash_index(self,key):
		_hash = key.__hash__()
		_idx = _hash & (self.size - 1) # if set to self.size it may return self.size which is out of list index!
		return _idx

	def sanity_check_key(self,key):
		if not isinstance(key,str):
			raise ValueError('Key should be of type string')

	def set(self,key,value,verbose=True):
		self.sanity_check_key(key)
		_idx = self.hash_index(key)
		if self.values[_idx] == None:
			self.keys.append(key)
			self.values[_idx] =  value
			return True
		else:
			if verbose:
				print('Collision! Cannot use this <{}> as key'.format(key))
			return False
			# raise KeyError('Collision! Cannot use this "{}" as key'.format(key))

	def get(self,key):
		if key in self.keys:
			self.sanity_check_key(key)
			_idx = self.hash_index(key)
			return self.values[_idx]
		else:
			return None

	def delete(self,key):
		self.sanity_check_key(key)
		if key in self.keys:
			_idx = self.hash_index(key)
			self.values[_idx] = None
			self.keys.remove(key)
		else:
			raise KeyError('Key not in the HashMap')

	def load(self):
		not_none_values = sum(x is not None for x in self.values)
		return not_none_values / self.size


if __name__ == '__main__':
	my_dict = HashMap(25)
	my_dict.set('W1',5)
	my_dict.set('W2',5)
	my_dict.set('W3',5)
	my_dict.set('W4',5)
	my_dict.set('b1',5)
	my_dict.set('b2',5)
	my_dict.set('b3',5)
	my_dict.set('b4',5)
	print(my_dict.keys)
