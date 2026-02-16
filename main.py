class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Check case n = 0
        if n == 0:
            return True
        else:
            # iterate ver each element of the list
            for i in range(len(flowerbed)):
                # if (the value in the actual position is 0) AND ( is the first element OR the value in previous position is 0) AND ( is the last element OR the value in next position is 0)
                if (flowerbed[i] == 0) and (i == 0 or flowerbed[i-1] == 0) and ( i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                    # plant a flower in position i
                    flowerbed[i] = 1
                    # remove one of n (flower was planted)
                    n -= 1
                    # if there is not flower left to plant
                    if n == 0:
                        return True
        # not all flowers were planted
        return False
    
if __name __  == '__main__':
    sol = Solution()
    print(sol.canPlaceFlowers([1,0,0,0,1],1))
    print()
    print(sol.canPlaceFlowers([1,0,0,0,1],2))
