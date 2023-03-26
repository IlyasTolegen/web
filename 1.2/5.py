def boring_prefix(a):
    n = len(a)
    for l in range(n, 1, -1):
        counts = {}
        for i in range(l):
            counts[a[i]] = counts.get(a[i], 0) + 1
        values = list(counts.values())
        if len(set(values)) == 1:
            return l
        elif len(set(values)) == 2:
            max_count = max(values)
            min_count = min(values)
            if values.count(max_count) == 1 and max_count - min_count == 1:
                return l
    return 2
number = int(input())
listt = input().split()
print(boring_prefix(listt))