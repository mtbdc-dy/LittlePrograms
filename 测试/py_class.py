class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m_dict = dict()

    def buildDict(self, d):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for words in d:
            if len(words) not in self.m_dict.keys():
                self.m_dict[len(words)] = [words]
            else:
                self.m_dict[len(words)].append(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        l = self.m_dict[len(word)]
        for words in l:
            count = 0
            for i, c in enumerate(words):
                if c == word[i]:
                    count += 1

            if count == len(word) - 1:
                return True
        return False


if __name__ == '__main__':
    obj = MagicDictionary()
    obj.buildDict()
    param_2 = obj.search()