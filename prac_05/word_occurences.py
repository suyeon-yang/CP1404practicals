
words_to_counts = {}
input_text = input("Enter a string: ")
words = input_text.split()

for word in words:
    word_count = (words_to_counts.get(word, 0))
    words_to_counts[word] = word_count + 1

words = list(words_to_counts.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, words_to_counts[word]))

