# HashMap
This is a challenge assignment given for KPCB fellows engineer programme.
This works similiar to python's dictionaries, java's hashmaps, php's associative arrays etc.
It simply maps the keys to a integer value using a hash function and we can store the value associated with it in that index.
Hashmaps are introduced for quick retrieval and insertion on key,value pairs.
In case of prefect hashing this time is O(1).
However they can be collisions, which are handled by different techiniques. Two of them is linear probing and quadratic probing. These two are implemented in this project.

###### From the code!

A hash table class, which can map string keys to values. This can have any size
	    as long as the memory supports. In case of perfect hashing insertion and retrieval
	    using keys is O(1).
	    
This class have 2 types of probing i.e linear and quadratic. Linear probing causes
	    clustering thus increasing the chances of collision, whereas quadratic clustering 
	    does not cause clustering and hence less chances of clustering.
		
However there is a trade-off, in quadratic probing there is a disdvantage. It is 
	    possible that all the empty spaces are not searched, so there are two conditions 
	    which the table size of quadratic probing must follow in order to ensure hitting 
	    of every empty space.
	    1. Be a prime number (I didn't find it much of a problem though!)
	    2. never be more than half full even by one element (This wasted my one hour! Hence very true!!)
	    src = 'https://cathyatseneca.gitbooks.io/data-structures-and-algorithms/tables/quadratic_probing_and_double_hashing.html'
		
###### CAUTION:
It's advisable to allocate twice the memory required while using quadratic probing
		otherwise it will get stuck in a for loop.

###### Usage:
When using smaller hashmaps i.e size between (1,50) strictly use linear probing,
		else if size is large i.e between (40,memory size) use quadratic probing

## How to use
This can run on any machine with python installed preferably Unix-like machines.
No external dependency is required.
The tests require some of the python stadard library packages.
just import this class into your project by writing.
`from hashmap import Hashmap`
`my_dict = Hashmap(size,probing_type)`

		Initalize a new hashmap

		Inputs:
		- size : size of the hashmap required(It should be twice the size                required while using quadratic probing).
		- probing : It can be of two types 'linear','quadratic'.
		- verbose : A parameter which I used for debugging purposes.

*you are ready to go.*

### Methods available
`my_dict.set(key,value)`

        Maps the provided key with the provided value!
        
		Inputs:
		- key: string to be mapped from
		- value: value to be mapped
		- 
		Returns:
		True: if operation was successful
		False: If unsuccessful

`my_dict.get(key)`

		returns the value of the key

		Inputs:
		- key: string to be mapped from
		- return_idx : Boolean to make it return the index of the value/key

		Returns:
		value, index : if return_idx set to True
		value : if return_idx set to False
		
`my_dict.delete(key):`

		deletes the value of the provided key
		
		Inputs:
		key : the key whose value is to be deleted
		
`my_dict.load()`

		Returns:
		the load on the hashmap i.e total values in hashmap/size

		Can be [0,1] if probing is 'linear'
		Can be [0,1) if probing is 'quadratic'



## TODO
1. ~~Basic hashmap.~~
2. ~~collision handling in get, set and delete.~~
3. ~~update keys with new values.~~
4. ~~add quadratic probing and its tests.~~
5. ~~remove bugs~~



