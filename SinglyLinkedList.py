class SinglyLinkedList:
    def __init__(self, capacity):
        """Initializes the linked list with a fixed capacity."""
        self.capacity = capacity
        self.data_array = [0] * capacity  # Stores node values
        self.next_array = [-1] * capacity  # Stores next node indices
        self.head = -1  # Points to the head node
        self.size = 0  # Tracks the number of elements

    def insert_at_head(self, value):
        """Inserts a new node at the head of the linked list."""
        if self.size == self.capacity:
            print(f"Insert {value}:")
            print("List is full: true")
            print("Is overflow: true")
            self.display()
            return False
        new_node = self.size  # New node index
        self.data_array[new_node] = value  # Store value in array
        self.next_array[new_node] = self.head  # Link new node to previous head
        self.head = new_node  # Update head pointer
        self.size += 1  # Increase size
        print(f"Inserted {value}")
        self.display()
        return True

    def remove_from_head(self):
        """Removes the head node from the linked list."""
        if self.head == -1:
            print("Cannot remove: linked list is empty.")
            print("Is underflow: true")
            return False
        removed_value = self.data_array[self.head]  # Get value of head node
        self.head = self.next_array[self.head]  # Update head pointer
        self.size -= 1  # Decrease size
        print(f"Removed {removed_value}")
        self.display()
        return True

    def peek(self):
        """Returns the value at the head of the linked list."""
        if self.head == -1:
            print("Cannot peek: linked list is empty.")
            return False
        print(f"Peek: {self.data_array[self.head]}")
        return True

    def display(self):
        """Displays the elements of the linked list."""
        if self.head == -1:
            print("Linked List: Empty : true")
            return
        current = self.head
        print("Linked List: ", end="")
        while current != -1:
            print(self.data_array[current], end=" ")
            current = self.next_array[current]  # Move to next node
        print(": true")

    def is_empty(self):
        """Checks if the linked list is empty."""
        empty = (self.size == 0)
        print(f"List is empty: {empty}")
        return empty

if __name__ == "__main__":
    list = SinglyLinkedList(3)  # Create a linked list with capacity 3

    list.insert_at_head(27)
    list.insert_at_head(26)
    list.insert_at_head(12)

    list.insert_at_head(2)  # Attempt to insert when full

    list.peek()  # Peek at head value

    list.remove_from_head()
    list.remove_from_head()
    list.remove_from_head()

    list.remove_from_head()  # Attempt to remove when empty

    list.is_empty()  # Check if list is empty

    if list.is_empty():
        print("Final state: Linked list is empty: true")
    else:
        print("Final state: Linked list is empty: false")

