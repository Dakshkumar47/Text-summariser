# Text Summarizer Using TextRank (PageRank Variant)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![GitHub stars](https://img.shields.io/github/stars/Dakshkumar47/Text-summariser.svg?style=social&label=Star&maxAge=2592000)](https://github.com/Dakshkumar47/Text-summariser/stargazers/)

## Project Overview
This project implements an extractive text summarizer using the TextRank algorithm (a graph-based ranking method inspired by PageRank) with cosine similarity for sentence scoring. Built with Python, NLTK for preprocessing (tokenization, stopword removal), and scikit-learn for vectorization and similarity computation. It generates concise summaries from long articles, preserving key information.

Part of my NLP journey, this tool demonstrates text preprocessing, graph-based NLP, and similarity metrics. Developed as a B.Tech AI & ML project at Rao Pahlad Singh Institute.

## Features
- **Preprocessing**: Tokenization, sentence splitting, stopword removal using NLTK.
- **Vectorization**: TF-IDF or word embeddings for sentence representations.
- **Ranking**: Builds a similarity graph and applies TextRank to score sentences.
- **Summary Generation**: Extracts top-ranked sentences for the summary.
- **Customizable**: Adjust summary length (e.g., top 5-10 sentences).

## Repository Structure
- `summarizer.py`: Main script for the summarization pipeline.
- `example_article.txt`: Sample input text for testing.
- `README.md`: This file.
- (Add more files like notebooks if needed.)

## Requirements
- Python 3.8+
- Libraries: `nltk`, `scikit-learn`, `numpy`

Install via:
bash
pip install nltk scikit-learn numpy


##**Download NLTK data:**
import nltk
nltk.download('punkt')
nltk.download('stopwords')

**Example code snippet:**
import nltk
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
# ... (full code in summarizer.py)
stop_words = stopwords.words('english')
vectorizer = TfidfVectorizer()
sentence_vectors = vectorizer.fit_transform(sentences)
sim_matrix = cosine_similarity(sentence_vectors)
# Build graph and apply PageRank...
