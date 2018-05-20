data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('這筆資料總共有', len(data), '資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均每筆料有', sum_len / len(data), '字元')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new) ,'筆資料小於100')

