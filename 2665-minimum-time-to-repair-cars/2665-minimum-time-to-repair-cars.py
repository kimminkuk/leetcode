class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        allow_max = cars * cars * min(ranks)
        left, right = 0, allow_max
        while left < right:
            mid = (left + right) // 2
            repaired_car = 0
            for idx, rank in enumerate(ranks):
                cur_repair_car = int(math.sqrt(mid // rank))
                repaired_car += cur_repair_car
            if repaired_car >= cars:
                right = mid
            elif repaired_car < cars:
                left = mid+1
            
        return left