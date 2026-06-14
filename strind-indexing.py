word = "hello"

print("first chat [0] =>", word[0])
print("second chat [1] =>", word[1])
print("third chat [2] =>", word[2])
print("fourth chat [3] =>", word[3])
print("fifth chat [4] =>", word[4])

# Negative indexing
print("last chat", word[-1])
print("second last chat", word[-2])
print("third last chat", word[-3])
print("fourth last chat", word[-4])
print("fifth last chat", word[-5])

print("read word [0]", word[0])
word[0] = "3"

result = None
print("result is None:", result is None)