class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        n = len(numbers)

        i,j = 0,n-1
        
        while j > i : 
            numbers[i] + numbers[j] == target 

            if numbers[i] + numbers[j] > target: 
                   
                   j -= 1  
            elif numbers[i] + numbers[j] < target: 
                   i += 1
                   
            else:
              return [i+1,j+1] 

        return []      
