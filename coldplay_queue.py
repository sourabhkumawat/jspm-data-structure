# coldplay_ticket_queue.py

class TicketQueue:
    def __init__(self):
        """Initialize an empty ticket queue."""
        self.queue = []

    def is_empty(self):
        """Check if the ticket queue is empty."""
        return len(self.queue) == 0

    def enqueue(self, requester_name):
        """
        Add a ticket request to the end of the queue.
        
        Args:
            requester_name (str): Name of the person requesting a ticket.
        """
        self.queue.append(requester_name)
        print(f"🎟️ Ticket request enqueued for {requester_name}.")

    def dequeue(self):
        """
        Process the next ticket request in the queue.
        
        Returns:
            str or None: The name of the person whose ticket was processed, or None if the queue is empty.
        """
        if not self.is_empty():
            processed_request = self.queue.pop(0)
            print(f"✅ Ticket processed for {processed_request}.")
            return processed_request
        else:
            print("❌ No ticket requests in the queue!")
            return None

    def peek(self):
        """
        Peek at the next ticket request to be processed without removing it.
        
        Returns:
            str or None: The name of the next requester, or None if the queue is empty.
        """
        if not self.is_empty():
            next_request = self.queue[0]
            print(f"🔍 Next ticket to be processed: {next_request}.")
            return next_request
        else:
            print("🔍 No ticket requests in the queue.")
            return None

    def size(self):
        """
        Get the current size of the ticket queue.
        
        Returns:
            int: Number of ticket requests in the queue.
        """
        current_size = len(self.queue)
        print(f"📊 Current queue size: {current_size} ticket request(s).")
        return current_size

    def display_queue(self):
        """Display the current state of the ticket queue."""
        if not self.is_empty():
            print("📝 Current Ticket Queue:")
            for idx, requester in enumerate(self.queue, start=1):
                print(f" {idx}. {requester}")
        else:
            print("📝 The ticket queue is currently empty.")

def main():
    """
    Example usage of the TicketQueue class to manage Coldplay ticket requests.
    """
    # Initialize the ticket queue system
    ticket_system = TicketQueue()
    
    # Display the initial state of the queue
    print("\n--- Coldplay Ticket Queue System ---\n")
    ticket_system.display_queue()
    print()

    # Enqueue ticket requests
    ticket_system.enqueue("Alice")
    ticket_system.enqueue("Bob")
    ticket_system.enqueue("Charlie")
    ticket_system.enqueue("Diana")
    ticket_system.enqueue("Ethan")
    print()

    # Display the queue after enqueuing
    ticket_system.display_queue()
    print()

    # Peek at the next ticket to be processed
    ticket_system.peek()
    print()

    # Check the size of the queue
    ticket_system.size()
    print()

    # Dequeue ticket requests
    ticket_system.dequeue()
    ticket_system.dequeue()
    print()

    # Display the queue after dequeuing
    ticket_system.display_queue()
    print()

    # Peek and check size again
    ticket_system.peek()
    ticket_system.size()
    print()

    # Dequeue remaining tickets
    ticket_system.dequeue()
    ticket_system.dequeue()
    ticket_system.dequeue()  # Attempt to dequeue when queue is empty
    print()

    # Final state of the queue
    ticket_system.display_queue()
    print("\n--- End of Ticket Processing ---\n")

if __name__ == "__main__":
    main()
