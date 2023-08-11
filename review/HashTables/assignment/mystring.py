from config import hash_table_size


class Mystring(str):
    """
        The Mystring class contains a "cleaned-up, lowercase string
        and its hash value
    """

    def __hash__(self) -> int:
        key = 1
        for i in range(len(self)):
            if (i % 2):
                key *= ord(self[i]) - 96
            else:
                key += ord(self[i]) - 96

        c2 = 0xabcdef0127d4eb4b
        key = (key ^ 59) ^ (key >> 15)
        key = key + (key << 7)
        key = key ^ (key >> 2)
        key = key * c2
        return ((key ^ (key >> 13)) & 0xfffffffffffffff) % hash_table_size
    
    def _remove_punctuation(self):
        temp = self.lower()
        if temp[-2:] == "'s":
            temp = temp[:-2]
            
        # remove leading non-alpha
        if len(temp) and not temp[0].isalpha():
            temp = temp[1:]
            
        # remove trailing non-alpha (twice)
        if not temp[-1:].isalpha():
            temp = temp[:-1]
        if not temp[-1:].isalpha():
            temp = temp[:-1]
            
        return Mystring(temp)
