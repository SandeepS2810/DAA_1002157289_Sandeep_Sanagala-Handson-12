class DynamicArray:
    def __init__(self):
        # Initialize the capacity of the dynamic array
        self.capacity = 1  
        # Initialize the number of elements in the dynamic array
        self.count = 0      
        # Create storage to hold elements
        self.storage = self.create_storage(self.capacity)

    def create_storage(self, capacity):
        """Create a new storage with the given capacity."""
        return [0] * capacity

    def is_full(self):
        """Check if the dynamic array is full and needs resizing."""
        return self.count == self.capacity

    def resize_storage(self, new_capacity):
        """Resize the dynamic array to the new capacity."""
        new_storage = self.create_storage(new_capacity)
        # Copy elements from the old storage to the new storage
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage
        self.capacity = new_capacity

    def add_element(self, value):
        """Add a new element to the end of the dynamic array."""
        if self.is_full():
            # Double the capacity if the dynamic array is full
            self.resize_storage(self.capacity * 2)
        self.storage[self.count] = value
        self.count += 1

    def get_element(self, index):
        """Get the element at the specified index."""
        if 0 <= index < self.count:
            return self.storage[index]
        else:
            raise IndexError("Index out of range")

    def elements_count(self):
        """Return the number of elements in the dynamic array."""
        return self.count

    def __str__(self):
        """Return a string representation of the dynamic array."""
        return "[" + ", ".join(str(self.storage[i]) for i in range(self.count)) + "]"


# Example usage:
if __name__ == "__main__":
    # Create a new dynamic array
    dynamic_array = DynamicArray()

    # Append elements to the dynamic array
    dynamic_array.add_element(10)
    dynamic_array.add_element(20)
    dynamic_array.add_element(30)
    dynamic_array.add_element(40)

    # Print the dynamic array
    print("Dynamic Array:", dynamic_array)  # Output: Dynamic Array: [10, 20, 30, 40]

    # Get elements by index
    print("Element at index 2:", dynamic_array.get_element(2))  # Output: Element at index 2: 30

    # Accessing the count of elements in the dynamic array
    print("Count of elements in dynamic array:", dynamic_array.elements_count())
