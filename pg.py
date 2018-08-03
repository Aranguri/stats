from pprint import pprint
import re

class PG:
    def __init__(self):
        self.words = self.read()
        self.two_words = self.two_words_gen()

    def read(self):
        f = open('pg.txt', 'r')
        text = f.read()
        text = text.replace('\n', ' ')
        text = text.replace('-', ' ')
        text = text.replace('\'re', ' are')
        text = text.replace('\'s', ' is')
        text = text.replace('\'m', ' am')
        text = text.replace('\'ll', ' will')
        text = text.replace('won\'t', 'will not')
        text = text.replace('n\'t', ' not')
        text = text.replace('\'ve', ' have')
        text = text.replace('\'d', ' would')

        text = text.replace('—', ' — ')
        text = text.replace('.', ' .')
        text = text.replace(',', ' ,')
        text = text.replace(':', ' :')
        text = text.replace(';', ' ;')
        text = text.replace('?', ' ?')
        text = text.replace('!', ' !')
        text = re.sub(r'\[[0-9]+\]', '', text)
        text = re.sub(r'[[0-9]+', '', text)
        words = text.split(' ')
        return [self.normalize(word) for word in words]

    def normalize(self, word):
        word = word.lower()
        '''
        word = word.replace('.', '')
        word = word.replace(',', '')
        word = word.replace('"', '')
        word = word.replace(':', '')
        word = word.replace(';', '')
        word = word.replace('?', '')
        word = word.replace('!', '')
        '''
        word = word.replace('(', '')
        word = word.replace(')', '')
        word = word.replace('--', '')
        return word

    def density(self, words):
        distribution = {}
        for word in words:
            if word not in distribution.keys():
                distribution[word] = 1
            else:
                distribution[word] += 1
        sorted_distribution = sorted(distribution.items(), key=lambda kv: kv[1])

        new_distribution = []
        total_words = 0
        for word, value in sorted_distribution:
            if value > 5:
                total_words += value
                new_distribution.append((word, value))

        new_distribution = [(w, v / total_words) for w, v in new_distribution]

    def two_words_gen(self):
        two_words = {}

        for word1, word2 in zip(self.words, self.words[1:]):
            if word1 not in two_words.keys():
                two_words[word1] = {word2: 1}
            else:
                if word2 not in two_words[word1]:
                    two_words[word1][word2] = 1
                else:
                    two_words[word1][word2] += 1

        for key in two_words.keys():
            total_value = 0
            for key2, value2 in two_words[key].items():
                total_value += value2
            for key2, value2 in two_words[key].items():
                two_words[key][key2] = value2 / total_value
        return two_words

    def distFn(self, word):
        return self.two_words[word]

'''
there is a more efficient way to store the two_words things (something like a graph.) Think about that'
'''
