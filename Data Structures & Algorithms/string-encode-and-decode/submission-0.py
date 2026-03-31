class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            eString = f"{len(string)}#{string}"
            res.append(eString)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        idx = left = 0
        while idx < len(s):
            if s[idx] == "#":
                length = int(s[left:idx])
                idx += 1
                string = s[idx:(length + idx)]
                res.append(string)
                idx += length
                left = idx
            else:
                idx += 1

        return res