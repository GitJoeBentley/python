
PUNC_CHARACTERS = r"!#%&'()*,-./:;?@\_¡§¶·¿:<>" + '"'

class Mystring(str):
    """
        The Mystring class contains a "cleaned-up, lowercase string
        and its hash value
    """

    def __init__(self, s: str):
        self = s.strip(PUNC_CHARACTERS).lower()

    def __hash__(self) -> int:
        key = 1;
        for i in range(self.__len__()):
            if (i % 2):
                key *= ord(self[i]) - 96;
            else:
                key += ord(self[i]) - 96;

        c2 = 0xabcdef0127d4eb4b
        key = (key ^ 59) ^ (key >> 15);
        key = key + (key << 7);
        key = key ^ (key >> 2);
        key = key * c2;
        return (key ^ (key >> 13)) & 0xfffffffffffffff;

    def _remove_punctuation(self):
        # remove 's
        if self[-2:] == "'s":
            self = self[:-2]
            
        # remove leading non-alpha
        if not self[0].isalpha():
            self = self[1:]
            
        # remove trailing non-alpha (twice)
        if not self[-1:].isalpha():
            self = self[:-1]
        if not self[-1:].isalpha():
            self = self[:-1]

        # Force the return type to be Mystring, not str
        return Mystring(self)
