import string
text = input("Enter a paragraph:\n")
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
words = cleaned_text.lower().split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

longest = max(words, key=len)

print("\n--- Text Analysis Report ---")
print("Total Words :", len(words))
print("Total Characters :", len(text))
print("Total Sentences :", text.count("."))
print("Longest Word :", longest)

print("\nWord Frequency:")
for word in freq:
    print(word, ":", freq[word])
