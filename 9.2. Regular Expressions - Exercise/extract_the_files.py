import re

valid_urls = []

pattern = r"(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"
# pattern = r"www\.[a-zA-Z0-9-\.]+\.[a-z]+"

line = input()

while line:
    matches = re.search(pattern, line)

    if matches:
        valid_urls.append(matches.group(0))

    line = input()

for url in valid_urls:
    print(url)

# Variant 2
# import re
#
# links = []
#
# pattern = r"(www\.[A-Za-z\d\-]+(\.[a-z]+)+)"
#
# while True:
#     line = input()
#
#     if not line:
#         break
#
#     matches = re.findall(pattern, line)
#     links.extend([m[0] for m in matches])
#
# for link in links:
#     print(link)