def get_freq(lst):
    return lst[1]

def word_count(lst):
    count_results = {}
    ordered_words = []

    for i in range(len(lst)):
        if lst[i] in count_results.keys():
            count_results[lst[i]] += 1
        else:
            count_results[lst[i]] = 1

    sorted_vals = sorted(count_results.items(), key=get_freq, reverse=True)
    ordered_words = [val[0] for val in sorted_vals]

    return count_results, ordered_words

if __name__ == "__main__":
    lst = ["poto", "platanero", "aloe", "aloe", "aloe", "cactus", "platanero", "poto", "suculenta", "platanero", "aloe", "aloe", "poto", "ficus", "suculenta"]
    
    count_results, ordered_words = word_count(lst)
    print(count_results)
    print(ordered_words)

