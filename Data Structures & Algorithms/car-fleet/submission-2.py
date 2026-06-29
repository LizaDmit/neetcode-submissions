class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        n = len(position)
        stack = []
  
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort()


        for i in range(n):
            pair[i] = (target - pair[i][0])/pair[i][1]

            

        for i in range(n-1, -1, -1):
            if i != n-1:
                if pair[i] < pair[i+1]:
                        pair[i] = pair[i+1]
                
            if pair[i] not in stack:
                stack.append(pair[i])

        

        return len(stack)