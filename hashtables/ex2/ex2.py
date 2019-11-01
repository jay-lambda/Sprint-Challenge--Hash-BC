#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # insert all the tickets into the hastable with the source as key and destination as value
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
    
    # ticket destination will retrieve the destination value based off the source key
    ticket_destination = hash_table_retrieve(hashtable, "NONE")
    
    # loop over every flight
    for i in range(0, length):
        # add the destination to the route
        route[i] = ticket_destination
        # replace the source key in ticket destination with the destination value
        ticket_destination = hash_table_retrieve(hashtable, ticket_destination)
    
    # print(route)
    return route

# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# # expected = ["PDX", "DCA", "NONE"]
# result = reconstruct_trip(tickets, 3)
