class Solution:

    def encode(self, strs: List[str]) -> str:
        separator = '#'
        encoded_string = "".join(str(len(word)) +separator  + word for word in strs)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_string = []
        separator = '#'
        i = 0

        while  i < len(s):
            j = s.find("#",i)
            length = int(s[i:j])

            word_start = j+1
            word_end = word_start + length

            word = s[word_start:word_end]
            decoded_string.append(word)

            i = word_end

        
        return decoded_string 