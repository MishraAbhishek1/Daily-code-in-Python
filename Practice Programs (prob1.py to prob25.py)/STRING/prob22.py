# prob22.py - Word frequency in sentence
sentence = "apple 4 4 4 apple orange banana apple orange"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)