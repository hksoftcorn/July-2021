class Keyword:
    def __init__(self, word):
        self.word = word
    
    def __len__(self):
        return len(self.word)
    
    def __getitem__(self, index):
        return self.word[index]
    
    def get_word(self):
        return self.word

hi = Keyword('hi')
hello = Keyword('hello')
bye = Keyword('bye')
keywords = [hi, hello, bye]
keywords = sorted(keywords, key=lambda x: len(x))
for keyword in keywords:
    print(keyword.get_word())
keywords = sorted(keywords, key=lambda x: x[1])
for keyword in keywords:
    print(keyword.get_word())
