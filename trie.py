
class TrieNode:
	def __init__(self,value):
		self.value = value
		self.sons = {}
		self.num = 1
		self.isLeaf = True
	def addWordsNum(self):
		self.num += 1
	
class TrieTree:
	def __init__(self):
		self.root = TrieNode('')
		self.root.num = 0
	def insertWords(self,words):
		wLen = len(words)
		tNode = self.root
		for i in range(wLen):
			value = words[i]
			sons = tNode.sons
			tNode.isLeaf = False
			if not sons.has_key(value):
				sonNode = TrieNode(value)
				tNode.sons[value] = sonNode
				tNode = sonNode
			else:
				sonNode = sons[value]
				sonNode.addWordsNum()
				tNode = sonNode
	def countPre(self,words):
		tNode = self.root
		wLen = len(words)
		for i in range(wLen):
			value = words[i]
			sons = tNode.sons
			if not sons.has_key(value):
				return 0
			else:
				tNode = sons[value]
		return tNode.num

while True:
    try:
		x = int(raw_input())
		a = TrieTree()
		ind = 0
		for i in range(x):
			words = raw_input()
			a.insertWords(words)
		y = int(raw_input())
		wordsList = [None]*y
		for i in range(y):
			words = raw_input()
			wordsList[i] = words
		for words in wordsList:
			print a.countPre(words)
    except EOFError:
        break
	