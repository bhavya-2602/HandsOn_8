class Stack:
    def __init__(self, size):
        """Initialize the stack with a given size."""
        self.capacity = size  # Maximum capacity of the stack
        self.stack_array = [0] * size  # Array to store stack elements
        self.top = -1  # Index of the top element

    def push(self, x):
        """Push an element onto the stack."""
        if self.top == self.capacity - 1:
            print(f"Pushing {x}:")
            print("Stack is full: true")
            print("Is overflow: true")
            self.display_stack()
            return False  # Stack overflow condition
        
        self.top += 1  # Move top pointer
        self.stack_array[self.top] = x  # Insert element
        print(f"Pushed {x} to the stack.")
        self.display_stack()
        return True

    def pop(self):
        """Pop the top element from the stack."""
        if self.top == -1:
            print("Cannot pop: stack is empty.")
            print("Is underflow: true")
            return False  # Stack underflow condition
        
        print(f"Popped {self.stack_array[self.top]} from the stack.")
        self.top -= 1  # Move top pointer down
        self.display_stack()
        return True

    def peek(self):
        """Return the top element of the stack without removing it."""
        if self.top == -1:
            print("Stack is empty: true")
            return False
        
        print(f"Top element is: {self.stack_array[self.top]}")
        return True

    def display_stack(self):
        """Display the current elements in the stack."""
        if self.top == -1:
            print("Stack is empty.")
        else:
            print("Current stack: ", end="")
            for i in range(self.top + 1):
                print(self.stack_array[i], end=" ")
            print()

if __name__ == "__main__":
    stack = Stack(3)  # Create a stack with capacity 3

    stack.push(27)  # Push elements onto the stack
    stack.push(26)
    stack.push(12)

    stack.push(2)  # Attempt to push when stack is full

    stack.peek()  # Check the top element

    stack.pop()  # Pop elements from the stack
    stack.pop()
    stack.pop()

    stack.pop()  # Attempt to pop when stack is empty

    stack.peek()  # Check the top element when stack is empty

