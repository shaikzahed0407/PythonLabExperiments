import string 
def get_top_10_words(filename): 
    word_freq = {} 
    with open(filename, 'r') as file: 
            for line in file: 
                line = line.translate(str.maketrans('', '', string.punctuation)).lower() 
                words = line.split() 
                 
                for word in words: 
                    word_freq[word] = word_freq.get(word, 0) + 1 
    
    sorted_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True) 
         
    print("Top 10 most frequently appearing words:") 
    for word, freq in sorted_words[:10]: 
            print(f"{word}: {freq}") 
             
file_name = input("Enter the text file name (e.g., 'sample.txt'): ") 
get_top_10_words(file_name)
