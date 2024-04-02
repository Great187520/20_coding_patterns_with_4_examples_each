class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        def abbr(s, index=0):
            n = len(s)

            if n - index <= 3:
                return s[:index+1] + str(n-index-2) + s[-1]
            
        ans = []
        n = len(dict)
        prefix = [0] * n
  
        for word in dict:
            ans.append(abbr(word))

        for i in range(n):
            while True:
                dup_list = []

                for j in range(i+1, n):
                    if ans[j] == ans[i]:
                        dup_list.append(j)

                    if not dup_list:
                        break

                    dup_list.append(i)

                    for k in dup_list:
                        prefix[k] += 1
                        ans[k] = abbr(dict[k], prefix[k])

        return ans
 