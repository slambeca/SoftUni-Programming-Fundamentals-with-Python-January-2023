import re

text = input()    # Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

result = re.findall(pattern, text)

print(" ".join(result))    # Peter Smith Lily Everett