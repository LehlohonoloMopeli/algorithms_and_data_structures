def anagram(word1, word2):
    """
    This function checks whether two words are anagrams of each other.
    """

    # Check the length of the words
    if len(word1) != len(word2):
        return False

    # Sort the words alphabetically
    word1 = sorted(word1)
    word2 = sorted(word2)

    # Iterate over all the letters and check if they are the same
    return all(word1[i] == word2[i] for i in range(len(word1)))

    
if __name__ == "__main__":
    
    print(anagram("dog", "god"))
    print(anagram("fluster", "restful"))
    print(anagram("algo", "gold"))
