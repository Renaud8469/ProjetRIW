

def vector_search(query, index):
    size = len(index)
    s = [0]*size
    query = query.replace(",", "").split()
    for word in query:
