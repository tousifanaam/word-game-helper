#!/usr/bin/env python
# Program for nailing wordgames

import string
alphabet_list_l = list(string.ascii_lowercase)
alphabet_list_u = list(string.ascii_uppercase)
base_10 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]

words = []
file = open('word_list.txt')
for word in file:
    clean_word = word.strip('\n')
    words.append(''.join(clean_word))

print("Vocab count:  " + str(len(words)))

while True:
	print()
	while True:
		start = input("Starting Alphabet:  ")
		if start == 'quit':
			exit()
		test = list(start)
		if len(test) > 0:
			if len(test) == 1 and test[0] in alphabet_list_l or test[0] in alphabet_list_u:
				break
			else:
				print("ERR. Try again.\n")
		else:
			print("ERR. Try again.\n")

	while True:
		total = input("Total Characters:  ")
		if total == 'quit':
			exit()
		test = list(total)
		if len(test) > 0:
			check_total = 0
			for i in test:
				if i in base_10:
					check_total += 1
			if len(test) == check_total:
				break
			else:
				print("ERR. Try again.\n")
		else:
			print("ERR. Try again.\n")

	total = int(total)
	check = 0
	success = 0
	for i in words:
		a = list(i)
		if a[0] == start.lower() or a[0] == start.upper():
			if ' ' not in a:
				if len(a) >= total:
					print(i)
					success = 1
					check += 1
		if check == 25:
			break
	if success == 0:
		print('░░░ Nothing Found! ░░░')