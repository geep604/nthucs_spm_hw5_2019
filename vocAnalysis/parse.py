# Author: Yu-Rong
# if you haven't installed nltk, execute this line to install nltk
#import os
#os.system("python3 -m pip install nltk")

import nltk

'''
Usage: 
	1. return the token count of an article 
	2. digit tokens should be removed, e.g, 1, 2, 3, 4,... 100, 101)
	3. all tokens will be transformed to lower case
	4. all punctuations will be removed [".", ":", ",", "?", "``", "''", "“", "’", "”", "!"]
Parameters:
	article -> the string of the article
Return type: dict()
'''
def word_frequency(article):
	tokens = []
	punc = [".", ":", ",", "?", "``", "''", "“", "’", "”", "!"]
	d = dict()
	sorted_wordcount = dict()
	tokens = nltk.word_tokenize(article)
	for token in tokens:
		# all token will be transformed to lower case
		token = token.lower()
		if token in punc:
			continue

		if token not in d:
			d[token] = 1
		else:
			d[token] = d[token] +1

	# sort the dictionary
	for w in sorted(d, key=d.get, reverse=True):
		sorted_wordcount[w] = d[w]
	return sorted_wordcount


'''
Usage: 
	1. return the ngram count of an article (should be sorted)
	2. all tokens will be transformed to lower case
	3. all punctuations will be removed [".", ":", ",", "?", "``", "''", "“", "’", "”", "!"]
Parameters:
	article -> the string of the article
	n -> 2 for bigram, 3 for tri-gram, ...
Return type: dict()
'''
def ngram_frequency(article, n)
	article = article.lower()
	token_list = nltk.word_tokenize(article)
	ngram_list = []
	d = dict()
	sorted_ngramcount = dict()
	punc = [".", ":", ",", "?", "``", "''", "“", "’", "”", "!"]

	for index, token in enumerate(token_list):
		ngram = ""
		for i in range(n):
			# filter out the punctuations and digits
			if (token_list[index+i] in punc) or token_list[index+i].isdigit():
				ngram = ""
				break
			elif (index+i) >= len(token_list):
				break
			else:
				ngram += (token_list[index+i]+' ')
		if ngram == "":
			continue
		ngram_list.append(ngram)

	# calculate the count of ngram without sorting
	for ngram in ngram_list:
		if ngram not in d:
			d[ngram] = 1
		else:
			d[ngram] = d[ngram] +1

	# sort the dictionary of ngram
	for w in sorted(d, key=d.get, reverse=True):
		sorted_ngramcount[w] = d[w]

	return d

'''
Usage: plot the bar graph of word count
Parameters:
	wordcount -> the dictionary of word count
	word_width -> the word width for the graph
	bar_max_width -> the longest bar width of the graph
	mode -> 0 for token, 1 for bigram, 2 for trigram
'''
def plot_bar_graph(wordcount, mode):
	if mode == 0:
		bar_max_width = 95
	elif mode == 1:
		bar_max_width = 85
	elif mode == 2:
		bar_max_width = 75
	elif mode == 3:
		bar_max_width = 65

	# it's how many rows you want to plot
	rows_to_plot = 20
	totalCount = 0
	percentWord = dict()
	max_percent = 0
	for word in list(wordcount.keys()):
		totalCount += wordcount[word]
	
	for word in list(wordcount.keys()):
		percentWord[word] = (wordcount[word]/totalCount)*100
	
	max_percent = max(percentWord.values())

	for word in list(percentWord.keys())[:rows_to_plot]:
		if mode == 0:
			print('{:>15}'.format(word+':'), end=' ')
		elif mode == 1:
			print('{:>25}'.format(word+':'), end=' ')
		elif mode == 2:
			print('{:>35}'.format(word+':'), end=' ')
		print('|'+'='*int(bar_max_width*(percentWord[word]/max_percent))+'|',end=' ')
		print(str(round(percentWord[word],2))+'%', '('+ wordcount[word] +')')


'''
command can be two types:
	1. "the _"
	2. "_ the"
'''
def search_bigram(bigram_count, command):
	target_bigram = dict()
	command = command.split()

	if len(command) == 2:
		if (command[0] = "_" and command[1] == "_") or (command[0] != "_" and command[1] != "_"):
			print("bad command1...")
			return
		else:
			if command[0] == "_":
				target_index = 0
			elif command[1] == "_":
				target_index = 1
			target = command[target_index]
			for bigram in bigram_count.keys():
				bigram_list = bigram.split(' ')
				if bigram_list[target_index] != target:
					continue
				elif bigram_list[target_index] == target:
					target_bigram[bigram] = bigram_count[bigram]
			return target_bigram
	else:
		print("bad command2...")
		return


command = ""
filename = "The Scarlet Letter.txt"
print("reading data..." + " (" + filename + ")")
f = open(filename)
article = f.read()
print("Command :")
print("(show token/show bigram/show trigram/exit)")

while(command != "exit"):
	command = input(">> ")
	if command == "show token":
		wordcount = word_frequency(article)
		print("Token distribution:")
		plot_bar_graph(wordcount, 0)
	elif command == "show bigram":
		bigram_count = ngram_frequency(article, 2)
		print("Bigram distribution:")
		plot_bar_graph(bigram_count, 1)
	elif command == "show trigram":
		trigram_count = ngram_frequency(article, 3)
		print("Trigram distribution:")
		plot_bar_graph(trigram_count, 0)
	elif command == "search bigram":
		search_command = input("please give a correlation you want to search : ")
		bigram_count = ngram_frequency(article, 2)
		target_bigram = search_bigram(bigram_count, search_command)
		plot_bar_graph(target_bigram, 1)
	elif command == "exit":
		print("bye~")
		break;
	else:
		print("'"+command+"'", "command not found")
		print("Command :")
		print("(show token/show bigram/show trigram/search bigram/exit)")