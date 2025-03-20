class Solution:
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] < arr[largest]:
            largest = left
        if right < n and arr[right] < arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, i)
    
    def heappop(self, arr):
        n = len(arr)
        if n == 0:
            return None
        
        root = arr[0]
        arr[0] = arr[n-1]
        arr.pop()            
        self.heapify(arr, len(arr), 0)
        
        return root    
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for _ in range(n)]
        for i in range(n):
            for j in range(len(nums)//2-1, -1, -1):
                self.heapify(nums, len(nums), j)  
            if i % 2 == 0:
                ans[i+1] = self.heappop(nums)
            else:
                ans[i-1] = self.heappop(nums)
            
        return ans                    