class Array:
    def __init__(self, size=0):
        """Initialize a static array with a given size. Supports dynamic resizing."""
        self.size = size
        self.capacity = size
        self.data = [None] * size
        print(f"Array of size {size} created.")

    def __getitem__(self, index):
        """Get the value at the given index."""
        if index >= self.size:
            raise IndexError("Array index out of bounds")
        return self.data[index]

    def __setitem__(self, index, value):
        """Set the value at the given index, with automatic resizing if needed."""
        if index >= self.capacity:
            self._reallocate(index + 1)
        if index >= self.size:
            self.size = index + 1
        self.data[index] = value

    def _reallocate(self, new_capacity):
        """Reallocate the array to increase its capacity (like realloc in C)."""
        print(f"Reallocating array to new capacity: {new_capacity}")
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def malloc(self, new_capacity):
        """Simulates malloc by allocating new memory without initializing."""
        print(f"Allocating memory of size: {new_capacity}")
        self.size = new_capacity
        self.capacity = new_capacity
        self.data = [None] * new_capacity

    def realloc(self, new_size):
        """Reallocate the array to a new size."""
        if new_size > self.capacity:
            self._reallocate(new_size)
        self.size = new_size

    def free(self):
        """Simulate memory deallocation by clearing the array."""
        print("Freeing the array memory.")
        self.data = []
        self.size = 0
        self.capacity = 0

    def __len__(self):
        """Return the current logical size of the array."""
        return self.size

    def __repr__(self):
        """String representation of the array."""
        return f"Array({self.data[:self.size]})"
