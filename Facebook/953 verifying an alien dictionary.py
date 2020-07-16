# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            if word1 == word2:
                continue
            if len(word1) > len(word2):
                if word1.startswith(word2):
                    return False
            for j in range(min(len(word1), len(word2))):
                if order_index.get(word1[j]) < order_index.get(word2[j]):
                    break
                elif order_index.get(word1[j]) == order_index.get(word2[j]):
                    continue
                else:
                    return False
        return True




