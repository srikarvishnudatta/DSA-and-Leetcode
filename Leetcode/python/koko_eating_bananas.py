import math


def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        while l<=r:
            k = (l+r)//2

            target_sum = 0
            for pile in piles:
                target_sum += math.ceil(float(pile)/k)
            if target_sum <= h:
                res = k
                r = k-1
            else:
                l = k+1
        return res