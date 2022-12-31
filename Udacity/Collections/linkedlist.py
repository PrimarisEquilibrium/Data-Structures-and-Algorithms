"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        
        count = 1
        current = self.head
        while current:
            if current == position:
                return current
            else:
                current = current.next
                count += 1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        current = self.head
        count = 1
        if position == 1:
            new_element.next = self.head.next
            self.head = new_element
        else:
            while current:
                if count == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                else:
                    current = current.next
                    count += 1
    
    def delete(self, value):
        """Delete the first node with a given value."""
        
        current = self.head
        # If initial node value is equal to value delete it
        if current.value == value:
            # Delete a node by setting it to its next node thus erasing it
            self.head = current.next
        else:
            # If the initial node is not equal to value
            # run the loop while current.next is not None (end)
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                else:
                    current = current.next