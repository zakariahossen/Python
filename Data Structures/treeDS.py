# Node ক্লাস তৈরি
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []  # চাইল্ড নোড লিস্ট

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print(" " * level * 4 + f"{self.data}")  # লেভেল অনুযায়ী স্পেস
        for child in self.children:
            child.display(level + 1)

# Root Node তৈরি
root = Node("দাদু/দাদি")

# Child Nodes যোগ করা
parent1 = Node("বাবা")
parent2 = Node("চাচা")

root.add_child(parent1)
root.add_child(parent2)

# Sub-Child Nodes যোগ করা
child1 = Node("আমি")
child2 = Node("আমার ভাই")
parent1.add_child(child1)
parent1.add_child(child2)

# ট্রি প্রদর্শন করা
root.display()
