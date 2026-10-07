class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<=1:
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return (word.upper()==word or word.lower()==word)