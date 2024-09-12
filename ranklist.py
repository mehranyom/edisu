def sort_mat(mat):
    size = len(mat)
    rank = 1
    for i in range(size):
        max_index = i  
        for j in range(i + 1, size):
            if mat[j][1] > mat[max_index][1]:
                max_index = j
        mat[max_index].insert(0, rank)
        (mat[i], mat[max_index]) = (mat[max_index], mat[i])
        rank += 1

def extract_torino_data():
    with open("torino.txt", "r") as infile:
        data = list()
        for line in infile:
            _, sid, _, point, isee, _ = line.split()
            point = point.replace(",", ".")
            isee = isee.replace(".", "")
            isee = isee.replace(",", ".")
            data.append([sid, float(point), float(isee)])
        sort_mat(data)
        
        headers = ["Rank", "SID", "Score", "ISEE"]
        data.insert(0, headers)
    return data       
