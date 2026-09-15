class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_list = []
        for word in strs:
            strs_list.append(str(len(word)))
            strs_list.append('#')
            strs_list.append(word)
        return "".join(strs_list)

    def decode(self, s: str) -> List[str]:
        result_strs = []
        begin = 0

        while begin < len(s):
            end = begin
            while s[end] != '#':
                end += 1
            length = int(s[begin:end])
            begin = end + 1
            end = begin + length
            result_strs.append(s[begin:end])
            begin = end
        return result_strs