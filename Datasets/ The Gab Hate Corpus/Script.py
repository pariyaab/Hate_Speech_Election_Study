import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import csv


dataset = pd.read_csv("GabHateCorpus_annotations.tsv", sep="\t")
dataset_name = "GabHateCorpus"
hate_text = dataset[dataset['Hate'] == 1]
dataset = hate_text.drop_duplicates()

text_data = " ".join(dataset['Text'].astype(str).tolist())
stop_words = set(stopwords.words('english'))
words = [word.lower() for word in text_data.split() if word.isalpha() and word.lower() not in stop_words]

# Create a WordCloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(words))

# Display the WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Text Column")
plt.savefig(f"{dataset_name}_word_cloud.png")

# Count word frequencies
word_counts = Counter(words)

sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
output_file = f"{dataset_name}_word_frequencies.csv"
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Word", "Count"])
    writer.writerows(sorted_word_counts)