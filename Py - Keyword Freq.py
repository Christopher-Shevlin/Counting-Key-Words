
english_stops = set(stopwords.words('english'))
# Retain alphabetic words: alpha_only
alpha_only = [t for t in lower_tokens if t.isalpha()]
# Remove all stop words: no_stops
no_stops = [t for t in alpha_only if t not in english_stops]

from collections import Counter
line_text = """test test test test"""

freq = Counter(line_text.split()).most_common()
print(freq)
