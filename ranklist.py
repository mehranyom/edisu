def sort_mat(mat):
    size = len(mat)
    for i in range(size):
        max_index = i  
        for j in range(i + 1, size):
            if mat[j][1] > mat[max_index][1]:
                max_index = j
        (mat[i], mat[max_index]) = (mat[max_index], mat[i])
        
def rank_in_uni(data):
    check = list()
    for item in data:
        uni = item[-2]
        if uni in check:
            pass
        else:
            rank_uni = 1
            for row in data:
                if row[-2] == uni:
                    row.insert(0, rank_uni)
                    rank_uni += 1
            check.append(uni)

def rank_in_degree(data):
    check = list()
    for item in data:
        degree = item[-1]
        if degree in check:
            pass
        else:
            rank_degree = 1
            for row in data:
                if row[-1] == degree:
                    row.insert(0, rank_degree)
                    rank_degree += 1
            check.append(degree)

def rank_in_uni_degree(data):
    check = list()
    for item in data:
        degree = item[-1]
        uni = item[-2]
        if (degree, uni) in check:
            pass
        else:
            rank_uni_degree = 1
            for row in data:
                if row[-1] == degree and row[-2] == uni:
                    row.insert(0, rank_uni_degree)
                    rank_uni_degree += 1
            check.append((degree, uni))
            
def extract_torino_data():
    with open("ranking_cat.txt", "r") as infile:
        data = list()
        for line in infile:
            line = line.rstrip()
            NoValue = len(line.split(" "))
            if NoValue != 6:
                university, degree = line.split(" ")
            else:
                _, sid, _, point, isee, _ = line.split()
                point = point.replace(",", ".")
                isee = isee.replace(".", "")
                isee = isee.replace(",", ".")
                data.append([sid, float(point), float(isee), university, degree])
    sort_mat(data)
    rank_in_uni(data)
    rank_in_degree(data)
    rank_in_uni_degree(data)
    rank = 1
    for row in data:
        row.insert(0, rank)
        rank += 1
    headers = ["Overall_Rank", "Rank_Uni_Degree", "Rank_Degree", "Rank_Uni", "SID", "Score", "ISEE", "University", "Degree"]
    data.insert(0, headers)

    return data