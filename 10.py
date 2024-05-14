import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

texts = [
    "This is a positive review.",
    "Great movie! I loved it.",
    "Poor quality. Disappointed.",
    "Awesome product, highly recommended."
]

labels = np.array([1, 1, 0, 1]) 
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()

X_train_counts = vectorizer.fit_transform(X_train)

X_test_counts = vectorizer.transform(X_test)

clf = MultinomialNB()

clf.fit(X_train_counts, y_train)

y_pred = clf.predict(X_test_counts)

accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.4f}")
print("\nPredicted Labels vs. Actual Labels:")
for pred_label, true_label, text in zip(y_pred, y_test, X_test):
    sentiment = "Positive" if pred_label == 1 else "Negative"
    true_sentiment = "Positive" if true_label == 1 else "Negative"
    print(f"Text: {text} | Predicted Sentiment: {sentiment} | Actual Sentiment: {true_sentiment}")
new_text = "This product exceeded my expectations. I'm very satisfied with it!"
new_text_counts = vectorizer.transform([new_text])

predicted_sentiment = clf.predict(new_text_counts)[0]
sentiment_label = "Positive" if predicted_sentiment == 1 else "Negative"
print(f"The predicted sentiment of the text '{new_text}' is: {sentiment_label}")
