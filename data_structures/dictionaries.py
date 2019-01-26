#this will be about hashing/dictionaries

class Hass:

	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self, key, data):
		hashvalue = self.hashfunction(key, len(self.slots))
#empty slot
		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
#replacement
		else:
			if self.slots [hashvalue] == key:
			 self.data[hashvalue] = data
			else:
				next_slot = self.rehash(hashvalue, len(self.slots))
				while self.slots[nextslot] is not None and self.slots[nextslot] is not key:
					nextslot = self.rehash(nextslot, len(self.slots))
				
				if self.slots[nextslot] == None:
					self.slots[nextslot] = key
					self.data[nextslots] = data
				else:
					self.data[nextslot] = data



	def hass_function(self, key, size):
		return key%size

	def rehash(self, oldhash, size):
		return (oldhash+1)%size


H = Hass()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

