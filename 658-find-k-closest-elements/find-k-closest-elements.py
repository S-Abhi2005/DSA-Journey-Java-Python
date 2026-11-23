class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        store = sorted(arr, key=lambda num: (abs(num - x), num))

        return sorted(store[:k])