# Python 3 program to find the length of the smallest substring with maximum distinct characters
TOTAL_CHARS = 256
# Find maximum distinct characters in given string
def max_chars(text, n):

    # Initialize all count of characters to 0
    count = [0] * TOTAL_CHARS
    # Check for Character count
    for i in range(n):
        count[ord(text[i])] += 1
    max_distinct = 0
    for i in range(TOTAL_CHARS):
        if (count[i] != 0):
            max_distinct += 1
    return max_distinct

def getSubstring(text):
    n = len(text)
    # Find maximum distinct characters in any string
    max_distinct = max_chars(text, n)
    min_len = n
    for i in range(n):
        for j in range(n):
            sub_text = text[i:j]
            sub_length = len(sub_text)
            sub_distinct_char = max_chars(sub_text, sub_length)
            if (sub_length < min_len and max_distinct == sub_distinct_char):
                min_len = sub_length
    return min_len

if __name__ == "__main__":
    text = input("Enter your string:")
    smallest_length = getSubstring(text)
    print(smallest_length)
