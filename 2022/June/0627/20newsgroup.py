from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import RidgeClassifier
from sklearn.model_selection import train_test_split
import re
from bs4 import BeautifulSoup
news20 = datasets.fetch_20newsgroups()



print(len(news20['data']))
print(news20['target'][0])
print(news20['target_names'])
print(news20['data'][0])

def text_cleaning(text):
    '''
    Cleans text into a basic form for NLP. Operations include the following:-
    1. Remove special charecters like &, #, etc
    2. Removes extra spaces
    3. Removes embedded URL links
    4. Removes HTML tags
    5. Removes emojis
    
    text - Text piece to be cleaned.
    '''
    template = re.compile(r'https?://\S+|www\.\S+') #Removes website links
    text = template.sub(r'', text)
    
    soup = BeautifulSoup(text, 'lxml') #Removes HTML tags
    only_text = soup.get_text()
    text = only_text
    
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    
    text = re.sub(r"[^a-zA-Z\d]", " ", text) #Remove special Charecters
    text = re.sub(' +', ' ', text) #Remove Extra Spaces
    text = text.strip()
    text=text.lower()# remove spaces at the beginning and at the end of string
    #text=TextBlob(text).correct()

    return text

texts = news20['data']
texts = list(map(text_cleaning, texts))
y = news20['target']

vectorizer = TfidfVectorizer(ngram_range=(3 ,5), max_df=0.5, min_df=3, analyzer = 'char_wb')
X = vectorizer.fit_transform(texts)
print('vectorize done')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

RC = RidgeClassifier()
RC.fit(X_train, y_train)
print('fit done')
y_pred = RC.predict(X_test)
print('acc:',sum(y_pred==y_test)/len(y_test))