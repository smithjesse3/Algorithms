def longestPalindromeSubsequence(str):
    n = len(str)
    0 <= len(str) <= 200
    #array that stores lengths of palindromes for  substreings
    dp = [[0 for i in range(n)] for j in range(n)]
    #list stores start and end indices
    ans = [0,0]
    #loop checks if adjacent characters in string are same. then updates dp and ans
    for i in range(len(str)-1):
        if str[i] == str[i +1]:
            dp[i][i+1] = True
            ans = [i, i + 1]
    #loop that fills the rest of dp by checking if same character as current if yes update
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if str[i] == str[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    i, j = 0, n - 1
    res = [''] * n
    #constructs longest palindrome subseq if start end char same then adds to res
    while i <= j:
        if str[i] == str[j]:
            res[i] = res[j] = str[i]
            i += 1
            j -= 1
        #if not same moves start or end inward
        elif dp[i + 1][j] > dp[i][j -1]:
            i += 1
        else:
            j -= 1
    return ''.join(res).strip()

print(longestPalindromeSubsequence("banana")) # This should return "anana"
print(longestPalindromeSubsequence("character")) # This should return "carac"
print(longestPalindromeSubsequence("racecar")) #return racecar
print(longestPalindromeSubsequence("roblox")) #return obo

def printNeatly(text, max):
    words = text.split()
    n = len(words)
    #arrray that stores extra spaces at end of each line
    extras = [[0 for _ in range(n)] for _ in range(n)]
    #stores minimum cost of arranging words from 1 to i
    line = [0 for _ in range(n)]
    #array that stores index of word that ends first line in optimal arrangement from 1 to i
    p = [0 for _ in range(n)]
    #loops that calculates extra spaces at the end of each line with different word arrangement
    for i in range(n):
        extras[i][i] = max - len(words[i])
        for j in range(i + 1, n):
            extras[i][j] = extras[i][j - 1] - len(words[j]) - 1
    #loops that calculate minimum cost and arrangement of words
    for i in range(n):
        for j in range(i, n):
            if extras[i][j] < 0:
                extras[i][j] = float('inf')
            else:
                extras[i][j] = pow(extras[i][j], 3)
    #loops that calculate minimum cost and arrangement of words
    for j in range(n):
        line[j] = extras[0][j]
        if extras[0][j] != float('inf'):
            p[j] = 0
        for i in range(1, j + 1):
            if extras[i][j] != float('inf') and (line[i - 1] + extras[i][j] < line[j]):
                line[j] = line[i - 1] + extras[i][j]
                p[j] = i
    #prints words in optimal order
    print_lines(words, p, n - 1)

#creates recursive function that prints words in optimal order
def print_lines(words, p, n):
    k = 0 if p[n] == 0 else print_lines(words, p, p[n] - 1)
    print(' '.join(words[k:n + 1]))
    return n + 1


printNeatly("Dynamic programming is not that difficult.", 15)
# The above should print 4 lines as below:
#
# Dynamic
# programming
# is not that
# difficult.
printNeatly("Algorithm is my favorite subject.", 16)
# The above should print 3 lines as below:
#
# Algorithm is
# my favorite
# subject.
printNeatly("The fox jumps over the dog", 10)
#prints 3 lines
#The fox
#jumps over
#the dog