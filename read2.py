data =[]
count = 0

with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		

word_count = {} 
for d in data:
	words = d.split()
	for word in words:
		if word in word_count:
			word_count[word] = word_count[word]+1
		else:
			word_count[word] = 1


for word in word_count:
	print("單字: %s ,出現 %s 次" %(word, word_count[word]))

print('總共有 %s 個單字' % (len(word_count)))


while True:
	word = input('輸入你想查詢的單字')
	if word == 'q':
		break;
	if word in word_count:
		print('%s 出現 %s次' %(word, word_count[word]))
	else:
		print('沒有出現過喔')

print('感謝使用')




