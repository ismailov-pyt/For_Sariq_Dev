from uzwords import words
def findMatches(word,words):
	words.remove(word)
	word = sorted(word)
	for lisso in words[1:]:
		for harf in lisso:			
			if word.count(harf) != list(lisso).count(harf) and word.count(harf)<list(lisso).count(harf):
				words.remove(lisso)
				break
			if harf not in (word):
				words.remove(lisso)
				break
	print(words[1:])	     
findMatches('аберрацион',words)

