
def get_list():
    return response.json(dict(mylist=['alpha', 'beta', 'gamma', 'delta']))

def get_another_list():
    return response.json({'mylist': ['gamma', 'iota', 'zeta']})
