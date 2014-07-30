class LRUCache:
	# @param capacity, an integer
	def __init__(self, capacity):
		self.capacity = capacity      
		self.cache_dict = {}
		self.key_list = []
	cap
	def __str__(self):
		return str(self.cache_dict) 

	# @return an integer
	def get(self, key):
		self.key = key
		if self.key in self.cache_dict:
			self.key_list.remove(self.key)
			self.key_list.append(self.key)    #move the expected value to the tail in the list
			return self.cache_dict[self.key_list[-1]]
		else:
			return -1

	# @param key, an integer
	# @param value, an integer
	# @return nothing
	def set(self, key, value):
		self.key = key
		self.value = value
		if key in self.cache_dict :
			self.cache_dict[key] = value
			self.key_list.remove(key)
			self.key_list.append(self.key)
		else :
			if len(self.key_list) == self.capacity:
				self.cache_dict.pop(self.key_list[0])   
				tem = self.key_list.pop(0)
				self.key_list.append(self.key)
				self.cache_dict[self.key] = self.value
				
