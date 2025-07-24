import sys

print("int:", sys.getsizeof(10))
print("float:", sys.getsizeof(10.5))
print("bool:", sys.getsizeof(True))
print("str:", sys.getsizeof("A"))
print("list:", sys.getsizeof([1, 2, 3]))
print("tuple:", sys.getsizeof((1, 2)))
print("dict:", sys.getsizeof({"a": 1}))
print("set:", sys.getsizeof({1, 2}))
print("None:", sys.getsizeof(None))
print("bytes:", sys.getsizeof(b"abc"))
