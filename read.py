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

#留言平均長度	
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度是: %f' %(sum_len/len(data)))


#篩選留言
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')

print(new[0])
print(new[1])


good = []
for f in data:
	if 'good' in d:
		good.append(d)

print('一共有', len(good), '提到good')
print(good[0])
