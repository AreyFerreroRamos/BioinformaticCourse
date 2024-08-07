def get_freq(lst):
    return lst[1]

class WordCount():
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.words = []
        self.count_results = {}
        self.ordered_words = []


    def add_word(self, word):
        if len(self.words) < self.max_size:
            self.words.append(word)
        else:
            print("Error: You have exceeded the limit of words.")

    def get_word_frequencies(self):
        for word in range(len(self.words)):
            if self.words[word] in self.count_results.keys():
                self.count_results[self.words[word]] += 1
            else:
                self.count_results[self.words[word]] = 1

        return self.count_results
        

    def show_words(self):
        sorted_vals = sorted(self.count_results.items(), key=get_freq, reverse=True)
        self.ordered_words = [val[0] for val in sorted_vals]

        print(self.ordered_words)
    
if __name__ == "__main__":
    word_count = WordCount(10)
    word_count.add_word("poto")
    word_count.add_word("poto")
    word_count.add_word("suculenta")
    word_count.add_word("cactus")
    word_count.add_word("cactus")
    word_count.add_word("poto")
    word_count.add_word("cactus")
    word_count.add_word("cactus")
    word_count.add_word("platanero")
    word_count.add_word("platanero")
    frequencies = word_count.get_word_frequencies()
    print(frequencies)
    word_count.show_words()
    word_count.add_word("aloe")  # Error message