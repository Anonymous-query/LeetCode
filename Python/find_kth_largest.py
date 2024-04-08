from heapq import heappop, heappush

def find_kth_largest_value(nums: list, k: int) -> int:
    heap = []
    for num in nums:
        heappush(heap, num)
        if len(heap) > k:
            heappop(heap)

    return heap[0]

if __name__ == "__main__":
    nums = [2,5,3,5,7,4,6]
    k=2
    result = find_kth_largest_value(nums, k)
    print(f"result: {k} -> {result}")