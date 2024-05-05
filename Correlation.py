import pandas as pd
# Labeled Data
labeled_data = {
    'text': ["This is a positive news article about technology.",
             "There is a negative sentiment in this article about finance.",
             "The article discusses neutral information about politics."],
    'label': [1, 0, 1]
}

labeled_df = pd.DataFrame(labeled_data)
labeled_df.to_csv('labeled_data.csv', index=False)

# Unlabeled Data
unlabeled_data = {
    'text': ["New article discussing recent developments in healthcare.",
             "Analysis of the current economic situation.",
             "Exploration of environmental issues and solutions."]
}

unlabeled_df = pd.DataFrame(unlabeled_data)
unlabeled_df.to_csv('unlabeled_data.csv', index=False)

# Stock Data
stock_data = {
    'date': ["2024-01-01", "2024-01-02", "2024-01-03"],
    'open': [100, 105, 110],
    'close': [105, 110, 108]
}

stock_df = pd.DataFrame(stock_data)
stock_df.to_csv('stock_data.csv', index=False)


def load_unlabeled_data(file_path):
    # Load the data from a CSV file
    data = pd.read_csv(file_path)
    return data

def load_labeled_data(file_path):
    # Load the data from a CSV file
    data = pd.read_csv(file_path)

    return data

from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the labeled dataset of news articles
data = load_labeled_data('labeled_data.csv')

# Extract the features from the text data using a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Train an SVM model on the labeled data
svm_model = svm.SVC(kernel='linear', probability=True)
svm_model.fit(vectorizer.fit_transform(data['text']), data['label'])

# Use the trained SVM model to classify new, unlabeled news articles

new_articles = load_unlabeled_data('unlabeled_data.csv')

predictions = svm_model.predict_proba(vectorizer.transform(load_unlabeled_data('unlabeled_data.csv')['text']))
sentiment_scores = predictions[:, 1] - predictions[:, 0]

#Returns
stock_data=pd.read_csv('stock_data.csv')
returns = (stock_data['close'] - stock_data['open']) / stock_data['open']

import numpy as np

# Calculate the Pearson correlation coefficient
correlation = np.corrcoef(returns, sentiment_scores)[0, 1]
print("Pearson correlation coefficient: ", correlation)
