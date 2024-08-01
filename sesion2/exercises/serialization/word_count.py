import pickle
import sys


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


    def read_words(self, fname):
        file = open(fname, 'r')

        for line in file:
            for word in line.split():
                self.add_word(word)

        self.get_word_frequencies()
        
        return self.words, self.count_results
    

    def save_word_count(self, fname):        
        with open(fname, 'wb') as file:
            pickle.dump(self.count_results, file, protocol=pickle.HIGHEST_PROTOCOL)
    

    def load_word_count(self, fname):
        with open(fname, 'rb') as file:
            self.count_results = pickle.load(file)

        return self.count_results


if __name__ == "__main__":
    word_count = WordCount(100)
    
    words, count_results = word_count.read_words(sys.argv[1])
    print(words)
    print(count_results)

    word_count.save_word_count(sys.argv[2])

    print(word_count.load_word_count(sys.argv[2]))