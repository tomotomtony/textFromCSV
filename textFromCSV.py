import pandas as pd

# sampledata.txtファイルを"読み込みモード"で開く
file_data = open("file_list.txt", "r")

# 読み込んだテキストファイルを１行ずつ表示
l_empty = []
for line in file_data:
    print(line)
    l_empty.append(line)

print(l_empty)
# 開いたファイルを閉じる
file_data.close()

#arrayForText
arr = [[0 for i in range(3)] for j in range(len(l_empty))]
print(arr)


df = pd.read_csv('test.csv')
#print(df['a'][3])
##########################################

for i in range(len(l_empty)):
    arr[i][0] = l_empty[i]
    arr[i][1] = df['b'][i]
    arr[i][2] = df['c'][i]


print(arr)

###########################################

text = open("testAndcsv.txt", "w")
for i in range(len(arr)):
    text.writelines(str(arr[i][0].strip()) + "\t" + str(arr[i][1]) + "\t" + str(arr[i][2]) + "\n")
    #text.writelines(str(arr[i][0]) + str(arr[i][1]) + str(arr[i][2]))

    #text.write(arr[i][1])
    #text.writelines(arr[i][2])
text.close()
"""
print(df.loc[:,'b':'c'])
print(df.loc[0:7,'b':'c'])       # show all column

"""