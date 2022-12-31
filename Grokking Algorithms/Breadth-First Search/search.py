# ------------------------ Graph Creation (Hash Table) ----------------------- #
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# ------------------------------ Queue Creation ------------------------------ #

from collections import deque # Queue
search_queue = deque() # Queue initialization
search_queue += graph["you"] # Adds all of your neighbors to the search queue

# ---------------------------------------------------------------------------- #
#                        Breadth-First Search Functions                        #
# ---------------------------------------------------------------------------- #

def person_is_seller(name):
    return name[-1] == "m"

# Without Checking
def breadth_first_search_no_checks(person): 
    while search_queue: # While the queue isn't empty ...
        person = search_queue.popleft() # ... grabs the first person off the queue
        if person_is_seller(person): # Checks whether the person is a mango seller
            print(f"{person} is a mango seller!") # Yes, they’re a mango seller.
            return True
        else: # No, they aren’t. Add all of this person's friends to the search queue.
            search_queue += graph[person]
    return False # If you reached here, no one in the queue was a mango seller

# --------------------- Algorithm Avoiding Infinite Loops -------------------- #

# With checking
def breadth_first_search(person):
    search_queue = deque()
    search_queue += graph[person]
    searched = [] # This array is how you keep track of which people you’ve searched before
    while search_queue:
        person = search_queue.popleft()
        if not person in searched: # Only search this person if you haven’t already searched them.
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person) # Marks this person as searched
    return False