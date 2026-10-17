class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n+1):
            binary_representation_of_i = bin(i)
            num_of_ones = binary_representation_of_i.count("1")
            result.append(num_of_ones)
        return result