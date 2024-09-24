# linked_list_kingdom.py

class Node:
    """
    Represents a single location (node) in the Linked List Kingdom.
    Each node holds a treasure and a pointer to the next node.
    """
    def __init__(self, treasure):
        self.treasure = treasure  # The treasure held by the node
        self.next = None          # Pointer to the next node


class LinkedList:
    """
    Represents the entire Linked List Kingdom.
    Provides methods to add, display, find, insert, and delete treasures.
    """
    def __init__(self):
        self.head = None  # Starting point of the kingdom

    def add_treasure(self, treasure):
        """
        Adds a new treasure to the end of the kingdom.
        """
        new_node = Node(treasure)
        if not self.head:
            self.head = new_node
            print(f"Added first treasure: {new_node.treasure}")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Added treasure: {new_node.treasure}")

    def display_treasures(self):
        """
        Displays all treasures in the kingdom in order.
        """
        treasures = []
        current = self.head
        while current:
            treasures.append(current.treasure)
            current = current.next
        if treasures:
            print("Linked List Kingdom Treasures:", " -> ".join(treasures))
        else:
            print("The Linked List Kingdom has no treasures.")

    def find_treasure(self, treasure):
        """
        Searches for a treasure in the kingdom.
        """
        current = self.head
        while current:
            if current.treasure == treasure:
                print(f"Treasure '{treasure}' found!")
                return current
            current = current.next
        print(f"Treasure '{treasure}' not found.")
        return None

    def insert_after(self, prev_treasure, new_treasure):
        """
        Inserts a new treasure after a specified existing treasure.
        """
        current = self.head
        while current:
            if current.treasure == prev_treasure:
                new_node = Node(new_treasure)
                new_node.next = current.next
                current.next = new_node
                print(f"Inserted '{new_treasure}' after '{prev_treasure}'")
                return
            current = current.next
        print(f"Treasure '{prev_treasure}' not found. Cannot insert '{new_treasure}'.")

    def delete_treasure(self, treasure):
        """
        Deletes a specified treasure from the kingdom.
        """
        current = self.head
        previous = None
        while current:
            if current.treasure == treasure:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f"Deleted treasure: {treasure}")
                return
            previous = current
            current = current.next
        print(f"Treasure '{treasure}' not found. Cannot delete.")

    def reverse_list(self):
        """
        Reverses the order of treasures in the kingdom.
        """
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
        print("Reversed the Linked List Kingdom.")

    def get_length(self):
        """
        Returns the number of treasures in the kingdom.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"The Linked List Kingdom has {count} treasure(s).")
        return count

    def clear_kingdom(self):
        """
        Removes all treasures from the kingdom.
        """
        self.head = None
        print("Cleared all treasures from the Linked List Kingdom.")


def main():
    # Initialize the kingdom
    kingdom = LinkedList()

    print("\n--- Embarking on the Quest: Adding Initial Treasures ---")
    # Add treasures to the kingdom
    kingdom.add_treasure("Ruby Gem")
    kingdom.add_treasure("Golden Crown")
    kingdom.add_treasure("Enchanted Sword")

    print("\n--- Displaying Treasures ---")
    # Display the treasures
    kingdom.display_treasures()

    print("\n--- Searching for a Treasure ---")
    # Search for a treasure
    kingdom.find_treasure("Golden Crown")
    kingdom.find_treasure("Silver Shield")  # This treasure does not exist

    print("\n--- Inserting a New Treasure ---")
    # Insert a new treasure
    kingdom.insert_after("Ruby Gem", "Mystic Orb")
    kingdom.display_treasures()

    print("\n--- Deleting a Treasure ---")
    # Delete a treasure
    kingdom.delete_treasure("Enchanted Sword")
    kingdom.display_treasures()

    print("\n--- Additional Operations ---")
    # Get the length of the kingdom
    kingdom.get_length()

    # Reverse the kingdom
    kingdom.reverse_list()
    kingdom.display_treasures()

    # Clear the kingdom
    kingdom.clear_kingdom()
    kingdom.display_treasures()


if __name__ == "__main__":
    main()
