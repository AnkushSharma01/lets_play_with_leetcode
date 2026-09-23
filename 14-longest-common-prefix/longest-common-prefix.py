class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        let_long = strs[0]
        for s in strs:
            while not s.startswith(let_long):
                let_long = let_long[:-1]

                if not let_long:
                    return ""
        return let_long

        