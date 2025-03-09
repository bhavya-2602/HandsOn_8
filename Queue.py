class Queue:
    def __init__(self, capacity):
        """Initialize the queue with a given capacity."""
        self.capacity = capacity  # Maximum capacity of the queue
        self.queue_array = [0] * capacity  # Array to store queue elements
        self.front = 0  # Front index of the queue
        self.size = 0  # Number of elements in the queue
        self.rear = capacity - 1  # Rear index of the queue

    def enqueue(self, x):
        """Add an element to the rear of the queue."""
        if self.size == self.capacity:
            print(f"Enqueue {x}:")
            print("Queue is full: true")
            print("Is overflow: true")
            self.display_queue()
            return False  # Queue overflow condition
        
        self.rear = (self.rear + 1) % self.capacity  # Circular increment of rear pointer
        self.queue_array[self.rear] = x  # Insert element
        self.size += 1  # Increase size
        print(f"Enqueued {x}")
        self.display_queue()
        return True

    def dequeue(self):
        """Remove the front element from the queue."""
        if self.size == 0:
            print("Cannot dequeue: queue is empty.")
            print("Is underflow: true")
            return False  # Queue underflow condition
        
        print(f"Dequeued {self.queue_array[self.front]}")
        self.front = (self.front + 1) % self.capacity  # Circular increment of front pointer
        self.size -= 1  # Decrease size
        self.display_queue()
        return True

    def peek(self):
        """Return the front element of the queue without removing it."""
        if self.size == 0:
            print("Queue is empty: true")
            return False
        
        print(f"Front element is: {self.queue_array[self.front]}")
        return True

    def display_queue(self):
        """Display the current elements in the queue."""
        if self.size == 0:
            print("Queue is empty.")
            return
        
        print("Current queue: ", end="")
        for i in range(self.size):
            index = (self.front + i) % self.capacity  # Calculate circular index
            print(self.queue_array[index], end=" ")
        print()

if __name__ == "__main__":
    queue = Queue(3)  # Create a queue with capacity 3

    queue.enqueue(27)  # Enqueue elements
    queue.enqueue(26)
    queue.enqueue(12)

    queue.enqueue(2)  # Attempt to enqueue when queue is full

    queue.peek()  # Check the front element

    queue.dequeue()  # Dequeue elements
    queue.dequeue()
    queue.dequeue()

    queue.dequeue()  # Attempt to dequeue when queue is empty

    is_empty = (queue.size == 0)  # Check if the queue is empty
    print(f"Queue is empty: {is_empty}")

