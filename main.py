import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
from files import get_file_data


pos_scores = []
neg_scores = []
dates = [data[0] for data in get_file_data()]

for filename in get_file_data():
    with open(f"diary/{filename[1]}", "r") as file:
        part = file.read()
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(part)
        pos_scores.append(scores["pos"])
        neg_scores.append(scores["neg"])

st.title("Diary Tone")

st.subheader("Positivity")
figure = px.line(x=dates, y=pos_scores, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")
figure = px.line(x=dates, y=neg_scores, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure)