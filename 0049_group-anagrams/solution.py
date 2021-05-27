from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            k = sorted(set(i))
            # d.setdefault("".join(k), []).append(i)
            d.setdefault(tuple(k), []).append(i)
        return list(d.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        """由于互为字母异位词的两个字符串包含的字母相同，因此两个字符串中的相同字母出现的次数一定是相同的，故可以将每个字母出现的次数使用字符串表示，作为哈希表的键。
        由于字符串只包含小写字母，因此对于每个字符串，可以使用长度为 2626 的数组记录每个字母出现的次数。
        """
        mp = {}
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp.setdefault(tuple(counts), []).append(st)
        return list(mp.values())
