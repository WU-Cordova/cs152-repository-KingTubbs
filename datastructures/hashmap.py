import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

def is_prime(number) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT,VT]]] = \
            Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(number_of_buckets)], \
                  data_type=LinkedList)
        self._load_factor_threshold: float = load_factor
        self._count: int = 0
        self._hash_function = custom_hash_function or self._default_hash_function
        self.number_of_buckets = number_of_buckets

    def __getitem__(self, key: KT) -> VT:
        #1 compite the bucket based on key
        bucket_index : int = self._get_bucket_number(key)

        #2 get the bucket chains in that bucket
        bucket_chain: LinkedList[tuple] = self._buckets[bucket_index]

        for (k, v) in bucket_chain: #parenthesis to reference the tuple
            if k == key:
                return v
        
        raise KeyError

    def __setitem__(self, key: KT, value: VT) -> None:        
        #store key and value pair together as a tuple
        
        bucket_index = self._get_bucket_number(key)
        bucket_chain = self._buckets[bucket_index]

        #update key if it exists
        for i, (k, v) in enumerate(bucket_chain):
            # eg. 0, (key, value) ; 1, (key, value)
            if k == key:
                bucket_chain.remove((k,v))
                bucket_chain.append((key, value))
                return
        
        #insert new key if key doesnt exist
        bucket_chain.append((key,value))
        self._count += 1
            
        #resizing
        if self._count / self.number_of_buckets > self._load_factor_threshold:
            self._resize()


    def keys(self) -> Iterator[KT]:
        for key, _ in self.items():
            yield key
        
    def values(self) -> Iterator[VT]:
        for _, value in self.items():
            yield value

    def items(self) -> Iterator[Tuple[KT, VT]]:
        for bucket in self._buckets:
            for (k, v) in bucket:
                yield (k, v)
            
    def __delitem__(self, key: KT) -> None:
        bucket_index = self._get_bucket_number(key)
        bucket_chain = self._buckets[bucket_index]  

        for i, (k, v) in enumerate(bucket_chain):
            # eg. 0, (key, value) ; 1, (key, value)
            if k == key:
                bucket_chain.remove((k,v))
                self._count -= 1
                return 
            
        raise KeyError


    def _get_bucket_number(self, key:KT) -> int: #index
        return self._hash_function(key) % self.number_of_buckets

    def _resize(self) -> None:
        """
        - called when the load factor exceeds the threshold during item insertion
        - doubles the number of buckets up to the next prime number
        - rehashes all existing items into the new buckets
        """
        new_capacity = self.number_of_buckets * 2
        while not is_prime(new_capacity):
            new_capacity += 1

        old_buckets = self._buckets

        self._buckets = Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(new_capacity)], data_type=LinkedList)
        self.number_of_buckets = new_capacity
        self._count = 0  # will be re-added properly by setitem

        for bucket in old_buckets:
            for (k, v) in bucket:
                self[k] = v
    
    def __contains__(self, key: KT) -> bool:
        #1 compite the bucket based on key
        bucket_index : int = self._get_bucket_number(key)

        #2 get the bucket chains in that bucket
        bucket_chain: LinkedList[tuple] = self._buckets[bucket_index]

        #3 is there a typle with the key in it?
        for (k, v) in bucket_chain: #parenthesis to reference the tuple
            if k == key:
                return True
        
        return False
    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        return self.keys()
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashMap):
            return False
        if len(self) != len(other):
            return False
        for key, value in self.items():
            if key not in other or other[key] != value:
                return False
        return True

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)