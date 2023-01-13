def isPossible(pos, dist, N, K ):
	count=1
	# place a cow at 1st position
	prev = pos[0]

	for curr_pos in range(1,N):
		curr = pos[curr_pos]
		
		# check if we can place a cow at that position
		if(curr - prev >= dist):
			prev = curr
			count = count+1

	# all the cows are placed
	if(count >= K):
		return True
	return False

N = 5
K = 3
pos = [1,2,8,4,9]

pos.sort()

ans = -1

# maximum element from the position array
max_dist = pos[N-1]

# take a low and high element
low = 1
high = max_dist

while(low <= high):
	mid = low + (high - low) // 2
   
	if(isPossible(pos, mid, N, K)):
		# store the distance in ans, if the arrangement is possible
		ans = mid
		# update the low to search for greater distance
		low = mid+1
	else:
		high = mid-1

print("The largest minimum distance is: " + str(ans))
