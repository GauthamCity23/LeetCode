class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        Steps:

            1) Stored each word as a dictionary
            2) Created a map between dict and word
            3) Looped through and checked for matches

        wordChecker = {}
        seenDictionaries = []
        dictStrMap = []

        for word in strs:
            d = {}
            for letter in word:
                if letter not in d:
                    d[letter] = 1
                else:
                    d[letter] = d[letter] + 1

            if d not in seenDictionaries:
                wordChecker[word] = [word]
                seenDictionaries.append(d)
                dictStrMap.append((d,word))
            else:
                for item in dictStrMap:
                    if item[0] == d:
                        wordChecker[item[1]].append(word)
            
        return list(wordChecker.values())
        '''

        returnDict = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in returnDict:
                returnDict[sortedS] = [s]
            else:
                returnDict[sortedS].append(s)

        return list(returnDict.values())