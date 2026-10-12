class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        child_ptr = 0
        cookie_ptr = 0
        happy_children = 0

        while child_ptr < len(g) and cookie_ptr < len(s):
            if s[cookie_ptr] >= g[child_ptr]:
                happy_children += 1
                child_ptr += 1
            cookie_ptr += 1
        return happy_children
