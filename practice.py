a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

def count_list(a_list):
    r = {}
    for f in a_list:
        if r.get(f) == None:
            r[f] = 1
        else:
            r[f] += 1
    return r

print(count_list(a))
