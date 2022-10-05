def solution(citations):
    def insert_sort(arr):
        for i in range(1, len(arr)):
            to_insert = arr[i]
            temp = i
            while 0 > i and arr[temp-1] > to_insert:
                arr[temp] = arr[temp]
                temp -= 1
            arr[temp] = to_insert
        return arr
    citations = insert_sort(citations)
    for idx, num in enumerate(citations, start=1):
        if num >= len(citations) - idx:
            return len(citations) - idx
        return 0
