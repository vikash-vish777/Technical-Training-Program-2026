# ============================================================
# 28. QUEUE IMPLEMENTATION USING LIST
# ============================================================

class Queue:

    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.queue_list = []

    # Check queue is full
    def is_full(self):
        if len(self.queue_list) == self.queue_size:
            return True
        else:
            return False

    # Check queue is empty
    def is_empty(self):
        if self.queue_list == []:
            return True
        else:
            return False

    # Add element
    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue_list.append(value)
            print(value, "added to queue")

    # Remove first element
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue_list.pop(0), "removed from queue")

    # Show first element
    def peek_front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Front element =", self.queue_list[0])

    # Delete queue
    def delete_queue(self):
        self.queue_list.clear()
        print("Queue has been deleted")

    # Display queue
    def display_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue =", self.queue_list)


# ============================================================
# QUEUE MENU
# ============================================================

size = int(input("Enter the size of queue: "))

queue_object = Queue(size)

while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek Front")
    print("4. Delete Queue")
    print("5. Display Queue")
    print("6. Is Empty")
    print("7. Is Full")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        value = int(input("Enter the value to enqueue: "))
        queue_object.enqueue(value)

    elif choice == 2:

        queue_object.dequeue()

    elif choice == 3:

        queue_object.peek_front()

    elif choice == 4:

        queue_object.delete_queue()

    elif choice == 5:

        queue_object.display_queue()

    elif choice == 6:

        print("Queue is empty:", queue_object.is_empty())

    elif choice == 7:

        print("Queue is full:", queue_object.is_full())

    elif choice == 8:

        print("Exit")
        break

    else:

        print("Invalid input")