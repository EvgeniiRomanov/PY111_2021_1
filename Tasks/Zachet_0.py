# Ищем доминирующую функцию
a = len(arr) – 1       # O(1)
out = list()           # O()
while a > 0:           # O(logN)
    out.append(arr[a]) # O(1) * O(1)
    a = a // 1.7
out.merge_sort()       # O(n log n)

O(1) + O(1) + O(logN) + O(N*logN) -> NlogN