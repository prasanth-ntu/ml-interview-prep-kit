class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Thoughts
        --------
        Naive approach
        Count the number of elements in both s and t into a dictionary as k, v pair. Then, compare the count for union of unique elements in s and t. If all match, then anagram, else, not an anagram

        Pseudocode
        -----------


        Complexity
        ----------
        Time Complexity: O(m+n) = O(k) 
        Space Complexity: O(26) if only english lower case


        LeetCode Submission Result
        --------------------------
        Accepted
        54 / 54 testcases passed


        """
                                                        # Time complexity
        d_s = {}
        d_t = {}
        unique_letters = set(s).union(set(t)) # O(n+m) - Iterate through both strings, s and t

        for letter in s:                                # O(n) - Iterate through s
            d_s[letter] = d_s.get(letter, 0) + 1

        for letter in t:                                # O(m) - Iterate through t 
            d_t[letter] = d_t.get(letter, 0) + 1

        for k in unique_letters:                        # O(k) - Iterate through 'k' unique characters at most (where, k=26 for lowercase english letters)
            if d_s.get(k, None) != d_t.get(k, None):    # O(1) - For each .get() cakkk
                return False

        return True

    def isAnagram_v2(self, s: str, t: str) -> bool:
        """
        Thoughts
        --------
        [Note] Took hints
        1. Redundant Work
            You're creating a unique_letters set by iterating through both strings. Then you iterate through both strings again to build your dictionaries. Is this set actually necessary?
            What would happen if you just compared d_s == d_t directly in Python? 
            That would still work

        2 . Early Exit Opportunity
            Before doing any counting work, is there a quick check that could immediately tell you two strings cannot be anagrams? Think about the fundamental property of anagrams.

        3. Space Optimization
            You're using two dictionaries (d_s and d_t). Could you achieve the same result with just one dictionary?
            Hint: What if you increment for one string and decrement for the other?
            Thought about it during inital version, but was too lazy to think and implement it


        Pseudocode
        -----------


        Complexity
        ----------
        Time Complexity: O(m+n) = O(k)
        Space Complexity: O(1) # Theoretically, as there are ~150K unicode characters


        LeetCode Submission Result
        --------------------------
        Accepted
        54 / 54 testcases passed
        """

        # Early exit
        if len(s) != len(t): 
            return False

        d = {}
    
        for letter in s:                                # O(n) - Iterate through s
            d[letter] = d.get(letter, 0) + 1

        for letter in t:                                # O(m) - Iterate through t 
            d[letter] = d.get(letter, 0) - 1

        #print (s, t, d, d.values())

        # Handles empty inputs
        if d == {}: 
            return True                 

        return set(d.values()) == set([0])

    def isAnagram_v2b(self, s: str, t: str) -> bool:
        """
        Thoughts
        --------
        [Note] Took hints

        1. One small note on your v2: the final check set(d.values()) == set([0]) works, but consider—could you simplify it to all(v == 0 for v in d.values())? Or even better, since you already have the early length check, think about whether you even need to check all values... 🤔

        Pseudocode
        -----------


        Complexity
        ----------
        Time Complexity: O(m+n) = O(k)
        Space Complexity: O(1) # Theoretically, as there are ~150K unicode characters


        LeetCode Submission Result
        --------------------------
        Accepted
        54 / 54 testcases passed
        """

        # Early exit
        if len(s) != len(t): 
            return False

        d = {}
    
        for letter in s:                                # O(n) - Iterate through s
            d[letter] = d.get(letter, 0) + 1

        for letter in t:                                # O(m) - Iterate through t 
            d[letter] = d.get(letter, 0) - 1

        #print (s, t, d, d.values())            

        # all returns True even if the iterable is empty
        return all(v == 0 for v in d.values())

    def isAnagram_v3(self, s: str, t: str) -> bool:
        """
        Thoughts
        --------
        [Note] Took hints

        1. Python's Standard Library
        Are you aware of collections.Counter? How might that simplify your code?
        There's also an even more "Pythonic" one-liner approach—what would that look like?

        Pseudocode
        -----------


        Complexity
        ----------
        Time Complexity: O(m+n)
        Space Complexity: 


        LeetCode Submission Result
        --------------------------
        
        """

        from collections import Counter

        return Counter(s) == Counter(t)

    def isAnagram_v4(self, s: str, t: str) -> bool:
        """
        Thoughts
        --------
        [Note] Took hints

        Sorting approach - simpler but less efficient.
        If two strings are anagrams, their sorted versions will be identical.

        Pseudocode
        -----------
        1. Sort both strings
        2. Compare the sorted results

        Complexity
        ----------
        Time Complexity: O(m log m + n log n) - dominated by sorting
        Space Complexity: O(m + n) - sorted() creates new lists regardless of character distribution

        Trade-off vs Counter:
        - Counter: O(n) time, O(k) space where k = unique chars (bounded by alphabet size)
        - Sorted: O(n log n) time, O(n) space always
        - For repetitive strings like "aaaa...", Counter uses O(1) space while sorted uses O(n)

        LeetCode Submission Result
        --------------------------
        Accepted
        54 / 54 testcases passed
        """

        return sorted(s) == sorted(t)

# Test cases
if __name__ == "__main__":
    s = Solution()

    # Example 1: Valid anagram
    assert s.isAnagram_v2b("anagram", "nagaram") == True

    # Example 2: Not an anagram
    assert s.isAnagram_v2b("rat", "car") == False

    # Same single character
    assert s.isAnagram_v2b("a", "a") == True

    # Different lengths
    assert s.isAnagram_v2b("ab", "a") == False

    # Different lengths
    assert s.isAnagram_v2b("a", "ab") == False

    # Duplicate content
    assert s.isAnagram_v2b("aa", "a") == False

    # Empty strings
    assert s.isAnagram_v2b("", "") == True

    # Unicode: Valid anagram (Chinese characters)
    assert s.isAnagram_v2b("你好世界", "世界你好") == True

    # Unicode: Not an anagram (different characters)
    assert s.isAnagram_v2b("你好", "世界") == False

    # Unicode: Mixed with duplicates
    assert s.isAnagram_v2b("café", "éfac") == True

    # Unicode: Emojis
    assert s.isAnagram_v2b("😀🎉", "🎉😀") == True

    print("All tests passed!")