class DocProcess(object):

    @classmethod
    def strip_html(cls, text):
        """
            Delete html tags in text.
            text is String
        """
        new_text = " "
        is_html = False
        for character in text:
            if character == "<":
                is_html = True
            elif character == ">":
                is_html = False
                new_text += " "
            elif is_html is False:
                new_text += character
        return new_text

    @classmethod
    def separate_words(cls, text, min_lenth=3):
        """
            Separate text into words in list.
        """
        splitter = re.compile("\\W+")
        return [s.lower() for s in splitter.split(text) if len(s) > min_lenth]

    @classmethod
    def get_words_frequency(cls, words_list):
        """
            Get frequency of words in words_list.
            return a dict.
        """
        num_words = {}
        for word in words_list:
            num_words[word] = num_words.get(word, 0) + 1
        return num_words