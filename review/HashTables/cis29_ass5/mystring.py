
PUNC_CHARACTERS = r"!#%&'()*,-./:;?@\_¡§¶·¿:<>" + '"'

class Mystring(str):
    """
        The Mystring class contains a "cleaned-up, lowerc ase string
        and its hash value
    """

    def __init__(self, s):
        self.strip(PUNC_CHARACTERS).lower()
        self._hash = self.__hash__()

    def __hash__(self):
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
        return (key ^ (key >> 13)) & 0xffffffffffffffff;

    #def __eq__(self, other):
    #    return self._str == other

    #def print(self):
    #    print(self._str + ": hash =",self._hash)

    #def __str__(self):
    #    return self._str
    
    def _remove_punctuation(self) -> str:
        # remove 's
        if self[-2:] == "'s":
            self = self[:-2]
        return self
    
    #def __len__(self) -> int:
    #    return self._str.__len__()
