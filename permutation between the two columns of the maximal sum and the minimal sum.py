
Matrix=[[1,-3,4, 0 ,9],
        [0,-9,7, 10,11],
        [2, 5,8,-11,45],
        [7, 4,12,-6,-5]]

def per(matrix):
    min=max=None
    for i in range(len(matrix[0])):
        sum=0
        for  j in range(len(matrix)):
            sum += matrix[j][i]
        if max==None:max=min=sum
        else:
            if sum>max:max=i
            if sum<min:min=i
    for i in range(len(matrix)):
        matrix[i][min],matrix[i][max]=matrix[i][max],matrix[i][min]
    return matrix

    
print(per(Matrix))