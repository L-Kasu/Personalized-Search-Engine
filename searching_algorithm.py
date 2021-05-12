

def intersect(p1,p2):
    answer = []

    pos1, pos2 = 0, 0

    while pos1 <= len(p1) and pos2 <= len(p2):
        if docID(p1[pos1]) == docID(p2[pos2]):
            answer.append(docID(p1))
            pos1 += 1
            pos2 += 1
        elif docID(p1[pos1]) < docID(p2[pos2]):
            pos1 += 1
        else:
            pos2 += 1

    return answer


