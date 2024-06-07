import heapq

requests = []

heapq.heappush(requests, (2, 187))
heapq.heappush(requests, (2, 134))
heapq.heappush(requests, (1, 567))
heapq.heappush(requests, (0, 111))
heapq.heappush(requests, (2, 908))
heapq.heappush(requests, (1, 345))
heapq.heappush(requests, (0, 222))

next = heapq.heappop(requests)
print(next)

print(requests)

