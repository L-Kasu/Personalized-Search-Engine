
def docID(x):
    return x


def intersect(p1,p2):
    answer = []

    pos1, pos2 = 0, 0

    while pos1 < len(p1) and pos2 < len(p2):
        if docID(p1[pos1]) == docID(p2[pos2]):
            answer.append(docID(p1[pos1]))
            pos1 += 1
            pos2 += 1
        elif docID(p1[pos1]) < docID(p2[pos2]):
            pos1 += 1
        else:
            pos2 += 1

    return answer


p1 = [1, 2, 4 ,7 ,9]
p2 = [2, 7, 13, 77]
p3 = [5, 24, 25, 35, 77, 99]


assert intersect(p1,p1) == p1
assert intersect(p3,p3) == p3
assert intersect(p1,p2) == [2,7]
assert intersect(p1,p3) == []
assert intersect(p2,p3) == [77]


print("intersect(", p1, ",", p2, ") =",intersect(p1,p2))
print("intersect(", p1, ",", p3, ") =",intersect(p1,p3))