# 📝 NLP Preprocessing Pipeline

A complete NLP preprocessing workflow with separate notebooks for **data fetching** and **preprocessing**, designed for clean, structured, and reproducible text data preparation.

---

## 📌 What is this project?

This project demonstrates an end-to-end NLP preprocessing pipeline:
- Fetch raw text data from an API
- Store it as a CSV (`data/raw_data.csv`)
- Apply text preprocessing in a separate notebook
- Prepare cleaned and vectorized text for downstream ML/NLP tasks

---

## ❓ Why this project?

- Raw textual data is unstructured and noisy.  
- Preprocessing is crucial for building effective ML/NLP models.  
- Separate notebooks for **data fetching** and **preprocessing** make the workflow **modular and reproducible**.

---

## ⚙️ How does it work?

### 🔑 Workflow Steps:
1. **Data Fetching**
   - Fetch data from API in `notebooks/data_fetch.ipynb`  
   - Save as `data/raw_data.csv`

2. **Preprocessing**
   - Load `raw_data.csv` in `notebooks/preprocessing.ipynb`  
   - Perform text cleaning, tokenization, stopword removal, stemming, lemmatization, vectorization  
   - Save cleaned data as `data/processed_data.csv`

3. **Optional: Feature Extraction & ML**
   - Use vectorized data for downstream tasks (classification, clustering, regression)

---

## 📂 Repository Structure

```
NLP-Preprocessing-Movie/
│-- src/
│ └── NLP-preprocessing.ipynb # Notebook: data fetching + preprocessing
│
│-- data/
│ ├── movie.csv # Raw movie dataset
│ └── processed_movie.csv # Preprocessed dataset
│
│-- reports/ # Optional: logs, plots, metrics
│-- requirements.txt # Python dependencies
│-- README.md
│-- .gitignore
```

## 💻Tech Stack

- Python 3.8+
- pandas, numpy
- NLTK / spaCy for text preprocessing
- scikit-learn for vectorization