class QuickSelect:
    # Class to implement QuickSelect algorithm

    def partition(self, arr, low, high):
        """Partitions the array and returns the pivot index."""
        pivot = arr[high]  # Choosing the last element as pivot
        i = low  # Pointer for smaller elements
        
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot
                i += 1
        
        arr[i], arr[high] = arr[high], arr[i]  # Swap pivot to correct position
        return i  # Return pivot index

    def quick_select(self, arr, low, high, i):
        """Finds the ith smallest element in the array."""
        if low == high:
            return arr[low]  # If only one element remains, return it
        
        pivot_index = self.partition(arr, low, high)  # Partition the array
        k = pivot_index - low + 1  # Number of elements in left part including pivot
        
        if i == k:
            return arr[pivot_index]  # Found the ith smallest element
        elif i < k:
            return self.quick_select(arr, low, pivot_index - 1, i)  # Recur on left subarray
        else:
            return self.quick_select(arr, pivot_index + 1, high, i - k)  # Recur on right subarray

    def print_array(self, arr):
        """Prints the array."""
        print("Array:", arr)

if __name__ == "__main__":
    qs = QuickSelect()
    
    arr = [18, 7, 5, 14, 4, 27, 26]  # Sample input array
    qs.print_array(arr)  # Print initial array
    
    i = int(input(f"Enter the ith element you want to find (1 <= i <= {len(arr)}): "))  # Get user input
    
    if i < 1 or i > len(arr):
        print(f"Invalid input. Please enter a number between 1 and {len(arr)}.")  # Validate input
    else:
        print(f"The {i}th smallest element is {qs.quick_select(arr, 0, len(arr) - 1, i)}")  # Find and print result

