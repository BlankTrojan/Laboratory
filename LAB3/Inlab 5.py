def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


HashTable = [[] for _ in range(10)]


def Hashing(keyvalue):
    return keyvalue % len(HashTable)



def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


insert(HashTable, 12, 'Lifes and works of Rizal')
insert(HashTable, 25, 'Fundamental of Electronics Circuits')
insert(HashTable, 20, 'Purposive Communication')
insert(HashTable, 9, 'Contemporary World')
insert(HashTable, 21, 'Software Design')
insert(HashTable, 21, 'Engineering Economics')

display_hash(HashTable)