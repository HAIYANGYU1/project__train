def afunc(l,fn):
    res = []
    for ele in l:
        if fn(ele):
            res.append(ele)
    return res

def filter(x):
    if x % 2 == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    l = list(range(10))
    print(l)
    res = afunc(l,filter)
    print(res)#[1,3,5,7,9]