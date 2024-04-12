class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[x ^ 1 for x in reversed(image)] for image in A]

        """
        for image in A:
            image.reverse()
            for indx in range(len(image)):
                image[indx] ^= 1
        return A
        """