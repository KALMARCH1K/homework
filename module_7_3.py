class WordsFinder:
    def __init__(self, *names):
        self.file_names = [name for name in names]

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name,'r',encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:

                        line = line.replace(symbol,'')
                    words += line.split()
            all_words[file_name] = words
        return all_words
    def find(self, word):
        places = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                places[key] = value.index(word.lower()) + 1

        return places

    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count

        return counters



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) 
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

