#mapper
    a = []
    for line in sys.stdin:
        a.append(line)
        a.sort(key=lambda x: len(x[4]),reverse=True)
        if len(a) == 11:
            a.pop()
    for line in reversed(a[0:10]):
        writer.writerow(line)
