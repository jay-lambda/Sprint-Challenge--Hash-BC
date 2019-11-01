#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(0, length):
        # print("key: ", weights[i])
        # print("value: ", i)

        # HTI takes in (hash_table, key, value)
        hash_table_insert(ht, weights[i], i)

    for i in range(0, length):
        # Since we want the sum of two values to equal the limit, and we know the one of the values as well
        # as the sum, we can do Value1 + ? = Sum --> Sum - Value1 = ?
        search = hash_table_retrieve(ht, (limit - weights[i]))
        if search is not None:
            # If Value 2 is bigger than Value 1, put Value 2 in front.
            if search > i:
                print((search, i))
                return (search, i)
            else:
                # If Value 2 is smaller than Value 1, put Value 2 behind.
                print((i, search))
                return (i, search)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights_3 = [4, 6, 10, 15, 16]
get_indices_of_item_weights(weights_3, 5, 21)



# [4, 6, 10, 15, 16]

# 21-4 = 17
# 21-6 = 15 !!
# 21-10 = 11
# 21-15 = 6 !!
# 21-16 = 5