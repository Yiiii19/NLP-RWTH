import numpy as np
from matplotlib import pyplot as plt
import time
start = time.time()


def SenWorCal():
	global sen_count
	global wor_count
	for line in Lines:
		# line = line.strip('\n')
		print(line)
		# print("biu!")
		# line = line[1]
		# split_sen = line.split()

		for ch in line:
			if ( ch in chardigit ):
				wor_count += 1
				# print(wor_count)

			# if ( ch == ' ' or ch == '\n' ):
			if ( ch == ' ' ):
				sen_count += 1

				if ( wor_count != 0 ):
					wor_result.append(wor_count)
					wor_count = 0


			if (ch == '\n'):
				# sen_count += 1
				sen_result.append(sen_count)
				sen_count = 0
# only use '\n' to decide a sentence or not

				# for pun in split_sen:
					# if ( pun == "." or pun == "?" or pun == "!"):
						# sen_result.append(sen_count)
						# sen_count = 0
	return [sen_result, wor_result]



f = open('Europarl.txt', 'r', encoding = 'utf8')
# f = open('test.txt', 'r', encoding = 'utf8')
Lines = f.readlines()
f.close()

chardigit='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
sen_result = list()
wor_result = list()
sen_count = 0
wor_count = 0

[sen_result, wor_result] = SenWorCal()

mid = time.time()
print('Mid time:', mid - start)
# print(sen_result)
print("Sen Max:", np.max(sen_result))
print("Wor Max:", np.max(wor_result))

# Mean and var of sentence length
s_sum = 0
w_sum = 0
for i in range(len(sen_result)):
	s_sum += sen_result[i]
s_mean = s_sum / len(sen_result)

s_sum = 0
for i in range(len(sen_result)):
	s_sum += (sen_result[i] - s_mean) * (sen_result[i] - s_mean)
s_var = s_sum / len(sen_result)

# Mean and var of word length

for j in range(len(wor_result)):
	w_sum += wor_result[j]
w_mean = w_sum / len(wor_result)

w_sum = 0
for i in range(len(wor_result)):
	w_sum += (wor_result[j] - w_mean) * (wor_result[j] - w_mean)
w_var = w_sum / len(wor_result)



print("Mean of sentance length: ", s_mean)
print("Variance of sentance length: ", s_var)
print("Mean of word length: ", w_mean)
print("Variance of word length: ", w_var)

end = time.time()
print("End time: ", end - start)


# 2.ex
s_bins = np.arange(0, 10000, 1)
w_bins = np.arange(0, 300, 1)

plt.xlim([min(sen_result)-2, max(sen_result)+2])
plt.hist(sen_result, bins = s_bins)
plt.xlabel('Sentence length')
plt.ylabel("Count")
plt.title('Distribution of sentence length')
plt.grid(True)
plt.annotate('max length', xy=(1002, 10), xytext=(500, 6000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.show()

plt.xlim([min(wor_result)-2, max(wor_result)+2])
plt.hist(wor_result, bins = w_bins)
plt.xlabel('Word length')
plt.ylabel("Count")
plt.title('Distribution of word length')
plt.grid(True)
plt.show()



