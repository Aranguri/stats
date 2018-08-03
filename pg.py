from pprint import pprint
import re

class Extracter:
    def __init__(self, file):
        self.file = file
        self.words = self.read()
        self.two_words = self.two_words_gen(1)

    def read(self):
        f = open(self.file, 'r')
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

        text = text.replace('’re', ' are')
        text = text.replace('’s', ' is')
        text = text.replace('’m', ' am')
        text = text.replace('’ll', ' will')
        text = text.replace('won’t', 'will not')
        text = text.replace('n’t', ' not')
        text = text.replace('’ve', ' have')
        text = text.replace('’d', ' would')

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

    def density(self):
        distribution = {}
        for word in self.words:
            if word not in distribution.keys():
                distribution[word] = 1
            else:
                distribution[word] += 1
        sorted_distribution = sorted(distribution.items(), key=lambda kv: kv[1])

        new_distribution = []
        total_words = 0
        for word, value in sorted_distribution:
            if value >= 4:
                total_words += value
                new_distribution.append((word, value))

        return {w: v / total_words for w, v in new_distribution[:1423]}

    def two_words_gen(self, separation):
        two_words = {}

        for word1, word2 in zip(self.words, self.words[separation:]):
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
        return self.two_words[0][word]

    def distFn2(self, word):
        weights = [.5, .26, .13, .06, .03, 0.013, 0.007]

        return self.two_words[i][word]

pg = Extracter('pg.txt')
zero = Extracter('0to1.txt')

print (len(pg.density()))
print (len(zero.density()))

'''
there is a more efficient way to store the two_words things (something like a graph.) Think about that'
'''
