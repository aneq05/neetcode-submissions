class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)

        for start in sorted(counter):
            while counter[start] > 0:
                for num in range(start, start+groupSize):
                    if counter[num] == 0:
                        return False
                    counter[num] -= 1

        return True
