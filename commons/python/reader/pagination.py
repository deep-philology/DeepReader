def paginate(it):
    lst = list(it)

    if lst:
        prev2 = lst[0]
        prev1 = lst[1] if len(lst) > 1 else None
        yield None, prev2, prev1
        for item in lst[2:]:
            yield prev2, prev1, item
            prev2 = prev1
            prev1 = item
        if prev1:
            yield prev2, prev1, None
