import numpy as np


r = np.random

ref_key = 'abbac'
compressed = [(0,1),(4,4),(1,3),(1,3),(3,4)]

#ref_key[0:1]

index = 7

def find(key,comp,i):
    decompressed_index = 0
    which_tuple = 0
    this_tuple_size = 0 # used to backtrack

    while decompressed_index < i:
        this_tuple = comp[which_tuple]
        this_tuple_size = len(range(this_tuple[0],this_tuple[1])) + 1

        print('jump')
        print("tuple nr:",which_tuple)
        print("tuple:",this_tuple)
        print("tuple size:",this_tuple_size)
        print(8*'-')
        #print(decompressed_index)
        decompressed_index = decompressed_index + this_tuple_size

        # Jump to next tuple
        which_tuple += 1

    print("> passby occured at...")
    print("tuple:",which_tuple)
    print("decompressed index:",decompressed_index)

    print("> returning to previous tuple")
    decompressed_index -= this_tuple_size
    which_tuple -= 1
    print("tuple:",which_tuple)
    print("decompressed index:",decompressed_index)

    print("> now we have the right tuple")
    print("> calculating index in tuple")
    which_index = i - decompressed_index
    print("index in tuple:",which_index)

    print("> decompressing tuple")
    this_tuple = comp[which_tuple]

    decompressed_tuple = key[int(this_tuple[0]):int(this_tuple[1]+1)]
    print("decompressed tuple:",decompressed_tuple)

    print("> final result:")
    print(decompressed_tuple[which_index])






    #print(key,comp)


find(ref_key,compressed,index)
