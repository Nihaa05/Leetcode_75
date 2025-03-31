class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        v=[]
        i =0

        while i<len(arr):
            cnt = 1
            while i+1 <len(arr) and arr[i]==arr[i+1]:
                cnt += 1
                i += 1
            if cnt in v:
                return False
            else:
                v.append(cnt)
            i+=1
        return True
