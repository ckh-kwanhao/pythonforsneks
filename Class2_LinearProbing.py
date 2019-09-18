class HashTable:
    def __init__(self,size):
        self.size = size
        self.keyarr = self.size * [None]
        self.data = self.size * [None]

    def __str__(self):
        return str(self.data)

    def add(self, key, data):
        hashval = self.hashfunc(key, len(self.data))

        if self.keyarr[hashval] == None:
            self.keyarr[hashval] = key
            self.data[hashval] = data
        else:
            if self.keyarr[hashval] == key:
                self.data[hashval] = data  # replace
            else:
                nextkey = self.rehash(hashval, len(self.keyarr))
                while self.keyarr[nextkey] != None and self.keyarr[nextkey] != key:
                    nextkey = self.rehash(nextkey, len(self.keyarr))

                if self.keyarr[nextkey] == None:
                    self.keyarr[nextkey] = key
                    self.data[nextkey] = data
                else:
                    self.data[nextkey] = data

        def hashfunc(self, key, size):
            return key % size

        def rehash(self, oldhash, size):
            return (oldhash + 1) % size
