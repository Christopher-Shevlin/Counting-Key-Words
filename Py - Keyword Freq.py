from collections import Counter
line_text = """test test test test"""

freq = Counter(line_text.split()).most_common()
print(freq)
