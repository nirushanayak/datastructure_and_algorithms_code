
def palindromeString(word):
    max = 1
    high = low = start = 0
    for i in range(1,len(word)):
        # for even length palindrome
        low=i-1
        high=i
        while low>=0 and high<len(word) and word[low]==word[high]:
            if high-low+1> max:
                max= high-low+1
                start=low
            low=low-1
            high=high+1

        #for odd length palidrome
        low=i-1
        high=i+1
        while low>=0 and high<len(word) and word[low]==word[high]:
            if high-low+1> max:
                max= high-low+1
                start=low
            low=low-1
            high=high+1
    return word[start:start+max]

test_case=int(input())
for i in range(test_case):
    word=input()
    print(palindromeString(word))

