import streamlit as st
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV

import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential, load_model
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils.np_utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping

st.title('Classifying Political Misinformation')
st.markdown('<style>h1{text-align: center; color: white;}</style>', unsafe_allow_html=True)
st.header("Please Enter Your News Article Below:")
st.markdown('<style>h2{text-align: center; color: white;}</style>', unsafe_allow_html=True)

st.sidebar.title("Visualizations")
st.sidebar.header("Please select below:")
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#fffffe, #615f85);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

page_bg_img = '''
<style>
body {
background-image: url("https://wallpapertag.com/wallpaper/full/6/3/8/865741-american-flag-backgrounds-1920x1200-for-phone.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

model = load_model('./Models/lstm_model.h5')

def to_words(text):
    ps = PorterStemmer()
    corpus = []
    letters = re.sub('[^a-zA-Z]', ' ',text)
    words = letters.lower().split()
    meaningful_words = [ps.stem(w) for w in words if not w in stopwords.words('english')]
    final = ' '.join(meaningful_words)
    corpus.append(final)
    return corpus

vocab_size = round(20000*1.3)

def convert_input(user_input):
    onehot = [one_hot(val,vocab_size)for val in to_words(user_input)]
    padded_onehot = pad_sequences(onehot,padding='pre',maxlen=2935)
    return padded_onehot

user_input = st.text_area("")

if user_input !="":
    processed_text = convert_input(user_input)
    final_text = np.array(processed_text)
    prediction = model.predict(final_text)
    if prediction.item() > 0.7:
        st.markdown("## Real News")
        st.markdown(prediction.item())
    elif prediction.item() > 0.5:
        st.markdown("## Likely Real News")
        st.markdown(prediction.item())
    elif prediction.item() > 0.3:
        st.markdown("## Likely Fake News")
        st.markdown(prediction.item())
    else:
        st.markdown("## Fake News")
        st.markdown(prediction.item())
else:
    st.markdown('## Nothing Here - Please Enter an Article')
