import pandas as pd

DF = pd.read_excel('Aeroflot.xlsx')
df = DF.values.tolist()
matrix = []
for i in range(len(df)):
    sup_list = []
    for j in range(len(df[i]) - 1):
        sup_list.append(df[i][j + 1])
    matrix.append(sup_list)

c_list = []
c_sum = 0
for cur_city in matrix:
    d_i = 0
    w_sum = 0
    c_i = 0
    tri_sum = 0
    for sup in cur_city:
        if sup:
            d_i += 1
        w_sum += sup
    if d_i == 1:
        c_i = 1
    elif d_i >= 2:
        for i in range(len(cur_city) - 1):
            if cur_city[i] > 0:
                for j in range(i + 1, len(cur_city)):
                    if cur_city[j] > 0 and matrix[i][j] > 0:
                        tri_sum += cur_city[i] + cur_city[j]
        c_i = tri_sum / ((d_i - 1) * w_sum)
    c_list.append(c_i)
    c_sum += c_i
c_sum /= len(matrix)
print(c_sum)

