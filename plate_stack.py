class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add a plate to the top of the tower."""
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove the top plate from the tower."""
        if not self.is_empty():
            removed = self.items.pop()
            print(f"Popped: {removed}")
            return removed
        else:
            print("Cannot pop from an empty stack!")
            return None

    def peek(self):
        """Look at the top plate without removing it."""
        if not self.is_empty():
            print(f"Top plate: {self.items[-1]}")
            return self.items[-1]
        else:
            print("The stack is empty!")
            return None

    def is_empty(self):
        """Check if the tower has any plates."""
        return len(self.items) == 0

    def size(self):
        """Get the number of plates in the tower."""
        return len(self.items)

    def display(self):
        """Display all plates in the tower."""
        print("Current Stack:", self.items)


# Playing with the Stack
if __name__ == "__main__":
    # Create a new stack (tower)
    tower = Stack()

    # Push plates onto the tower
    tower.push("Plate 1")
    tower.push("Plate 2")
    tower.push("Plate 3")
    tower.display()  # Current Stack: ['Plate 1', 'Plate 2', 'Plate 3']

    # Peek at the top plate
    tower.peek()  # Top plate: Plate 3

    # Pop the top plate
    tower.pop()  # Popped: Plate 3
    tower.display()  # Current Stack: ['Plate 1', 'Plate 2']

    # Check if the stack is empty
    print("Is the tower empty?", tower.is_empty())  # Is the tower empty? False

    # Pop remaining plates
    tower.pop()  # Popped: Plate 2
    tower.pop()  # Popped: Plate 1
    tower.pop()  # Cannot pop from an empty stack!
    tower.display()  # Current Stack: []

    # Final check
    print("Is the tower empty now?", tower.is_empty())  # Is the tower empty now? True
