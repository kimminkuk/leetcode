class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empty_bottles = 0
        full_bottles = numBottles
        while numBottles // numExchange:
            full_bottles = (full_bottles + empty_bottles) // numExchange
            empty_bottles = numBottles - (full_bottles * numExchange)
            numBottles = full_bottles + empty_bottles
            drank += full_bottles
        return drank