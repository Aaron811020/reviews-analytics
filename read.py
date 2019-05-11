#讀取檔案
#總共一百萬筆
data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總動有', len(data), '筆資料')

