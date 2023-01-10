from math import ceil
def minEatingSpeed(piles, h):
        l,r = 1, max(piles)
        min_k = r
        while l <= r:
            k = (r+l) // 2
            hrs = 0
            for pile in piles:
                hrs += ceil(pile/k)
            if hrs <= h:
                min_k = min(k, min_k)
                r = k-1
            else:
                l = k+1
        return min_k
print(minEatingSpeed([3,6,7,11],8))