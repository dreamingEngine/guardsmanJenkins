def loadPhraseBook(filename):
	phrasebook = {}
	phrases = open(filename, "r")
	for line in phrases:
		str1, str2 = line.split("/")
		phrasebook[str1] = str2
	print(str(phrasebook))
	print(phrasebook["heresy"])
	phrases.close()

loadPhraseBook('test')