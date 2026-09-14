from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            group_key = "".join(sorted(word))
            groups[group_key].append(word)

        return list(groups.values())