from sklearn.externals import joblib
import nltk
nltk.download('movie_reviews')
from nltk.corpus import movie_reviews
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer


negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

negfeats = [" ".join(movie_reviews.words(fileids=[f])) for f in negids]
posfeats = [" ".join(movie_reviews.words(fileids=[f])) for f in posids]

texts = negfeats + posfeats
labels = [0] * len(negfeats) + [1] * len(posfeats)

clf = make_pipeline(CountVectorizer(), LogisticRegression())
clf.fit(texts, labels)

joblib.dump(clf, 'clf.pkl')