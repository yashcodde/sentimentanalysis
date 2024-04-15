import string
from collections import Counter
import matplotlib.pyplot as plt

# Read the text file
text = open("read.txt", encoding="utf-8").read()

# Convert to lowercase
lower_case = text.lower()

# Remove punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Split text into words
words = cleaned_text.split()

# Define stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Remove stop words
filtered_words = [word for word in words if word not in stop_words]

# NLP Emotion Algorithm
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.strip().replace(",", '').replace("'", '')
        word, emotion = clear_line.split(':')

        if word in filtered_words:
            emotion_list.append(emotion)

# Count each emotion
emotion_count = Counter(emotion_list)
print(emotion_count)

# Plot the emotions on the graph
fig, ax = plt.subplots()
ax.bar(emotion_count.keys(), emotion_count.values())
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.title('Emotion Analysis')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('emotion_analysis.png')
plt.show()
