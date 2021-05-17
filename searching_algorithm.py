import inverted_matrix
import pp_file_reader as pp

# gets two postings
# returns a posting
# intersects two postings (only returns numbers contained in both postings)

def intersect(p1,p2):
    answer = []

    pos1, pos2 = 0, 0

    while pos1 < len(p1) and pos2 < len(p2):
        if (p1[pos1]) == (p2[pos2]):
            answer.append((p1[pos1]))
            pos1 += 1
            pos2 += 1
        elif (p1[pos1]) < (p2[pos2]):
            pos1 += 1
        else:
            pos2 += 1

    return answer


# testing
p1 = [1, 2, 4 ,7 ,9]
p2 = [2, 7, 13, 77]
p3 = [5, 24, 25, 35, 77, 99]

assert intersect(p1,p1) == p1
assert intersect(p3,p3) == p3
assert intersect(p1,p2) == [(2),(7)]
assert intersect(p1,p3) == []
assert intersect(p2,p3) == [(77)]


#print("intersect(", p1, ",", p2, ") =",intersect(p1,p2))
#print("intersect(", p1, ",", p3, ") =",intersect(p1,p3))


# gets list of words
# returns list of documentID's
# searches for all documents containing all words in the given list

def and_search(words):
    matrix = inverted_matrix.build_matrix_with_stemming()

    # convert matrix to dictionary
    dict = {}
    for i in range(0, len(matrix)):
        key = matrix[i][0]
        value = matrix[i][1]
        dict[key] = value


    # gather all postings
    postings = []
    for i in range(0, len(words)):
        postings.append(dict[words[i]])

    # intersect all postings (and all searched words)

    documents = postings[0]

    for i in range(1, len(postings)):
        documents = intersect(documents,postings[i])

    return documents
