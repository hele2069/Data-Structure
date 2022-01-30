import LinkedList

x = LinkedList.DLinkedList()

# ---------- empty state
print(x.is_empty())
print(x.get_length())
print(x.search(3))
print(x.travel())
# ---------- inserting
x.insert_head(1)
x.insert_head(6)
x.insert_tail(78)
# ---------- confirming
print(x.is_empty())
print(x.get_length())
print(x.search(3))
print(x.search(78))
print(x.travel())
print(x.remove(3))
print(x.remove(78))
print(x.travel())


