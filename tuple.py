t1={1,2,3} # set 
t2=(1,2,4) # tuple
t4=()      # empty tuple
t3={}      #dictionary

print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))

#What is a tuple?
# A tuple is an ordered and immutable collection of items in Python.
# ✅ Ordered → Elements keep their insertion order.
# ✅ Immutable → You cannot add, remove, or modify elements after the tuple is created.
# ✅ Allows duplicate values.
# ✅ Can store different data types.

# Why Use a Tuple?
# Use a tuple when:
# The data should not change.
# You want slightly better performance than a list.
# You need to use the collection as a dictionary key (if its elements are hashable).

# 2. Tuple vs List ⭐⭐⭐⭐⭐
# This is one of the most frequently asked questions.
# Know the differences:
# Mutable vs Immutable
# Syntax
# Performance
# Memory usage
# Use cases

# Mutable vs Immutable
# List → Mutable
# A list can be changed after it is created.