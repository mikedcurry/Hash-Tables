# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # hash the thing
        hash_index = self._hash_mod(key)

        # If nothing is at the hash_index create a new thingy there
        if self.storage[hash_index] is None:
            self.storage[hash_index] = LinkedPair(key, value)

        # else, COLLISION something must already be there -- make a chain
        else:
            #print('Warning: something is already there')
            new_guy = LinkedPair(key, value)
            new_guy.next = self.storage[hash_index]
            self.storage[hash_index] = new_guy


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        #hash the thing
        hash_index = self._hash_mod(key)
        thing = self.storage[hash_index]
        prev_thing = None

        #cycle through linked list
        while thing:
            # if it's not the right thing, swap things & move on
            if thing.key != key:
                thing, prev_thing = thing.next, thing
            
            # Otherwise the key is either right or doesn't exist
            else:
                # If key IS right...
                if thing.key == key:
                    # and if there is a prev_thing
                    if prev_thing:
                        # then make prev_thing the thing.
                        prev_thing.next = thing.next
                    # otherwise we must be at the begining of the chain...
                    else:
                        # so make the thing None
                        self.storage[hash_index] = None
                    
                    return

        print('Warning: key not found')


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_index = self._hash_mod(key)
        thing = self.storage[hash_index]

        while thing:
            if thing.key == key:
                return thing.value
            else:
                thing = thing.next

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old = self.storage

        self.capacity *= 2
        self.storage = [None] * self.capacity

        for thing in old:
            while thing:
                self.insert(thing.key, thing.value)
                thing = thing.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
