def longest_substring(s):
  output = ""
  for i in range(len(s)):
    for j in range(i+1, len(s)+1):
      if len(set(s[i:j])) == j-i:
        if len(s[i:j]) > len(output):
          output = s[i:j]
  return output
print(longest_substring("abbbbacc"))

