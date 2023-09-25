# ive just learned kwargs

def plans_for_tomorrow(text, divisor, *args, **kwargs):
    text = text.split(divisor)
    lists = []
    for i, j in args:
        text[i] = kwargs.get(j, lambda x: x)(text[i])
        lists.append(text[i])
    return lists

