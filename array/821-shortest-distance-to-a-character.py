class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # N = len(s)
        # left, right, output = [None]*N,[None]*N, [None]*N

        # temp = float("inf")
        # for i in range(N):
        #     if s[i] == c:
        #         temp = 0
        #     left[i] = temp
        #     temp += 1
        # for i in range(N-1, -1, -1):
        #     if s[i] == c:
        #         temp = 0
        #     right[i] = temp
        #     temp += 1
        # for i in range(N):
        #     output[i] = min(left[i], right[i])
        # return output
        # result array to store the shortest distances
        result = []
    
    # iterate through the string
        for i in range(len(s)):
        # initialize the shortest distance as a large number
            shortest_distance = float('inf')
        # iterate through the string again to find the nearest occurrence of the character
            for j in range(len(s)):
                if s[j] == c:
                # update the shortest distance if a nearer occurrence is found
                    shortest_distance = min(shortest_distance, abs(i - j))
        # append the shortest distance to the result array
            result.append(shortest_distance)
    
        return result