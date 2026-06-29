class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        times = []
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort()
        print(pair)

        for i in range(n):
            t = (target - pair[i][0])/pair[i][1]
            times.append(t)
        print(times)
        
        for i in range(n-2, -1, -1):
            if times[i] < times[i+1]:
                times[i] = times[i+1]
        return len(set(times))