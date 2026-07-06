# English–Hindi Dataset Processing and Machine Translation

This repository contains my solutions for the English–Hindi Dataset Processing and Translation assessment. The project is divided into two parts:

- **Assignment 1:** Dataset processing and filtering
- **Assignment 2:** English to Hindi translation using a Hugging Face language model and evaluation using standard machine translation metrics.

The implementation is entirely done in Python and is designed to be simple, modular, and easy to reproduce.

---

# Project Structure

```
.
├── assignment1_dataset_processing/
│   ├── process_dataset.py
│   ├── download_dataset.py
│   ├── requirements.txt
│   ├── README.md
│   └── output/
│       └── cleaned_english_hindi_dataset.xlsx
│
├── assignment2_translation/
│   ├── translate_and_evaluate.py
│   ├── setup_and_run.sh
│   ├── requirements.txt
│   ├── README.md
│   └── output/
│       ├── translations.xlsx
│       └── scores.txt
│
├── data/
│
└── README.md
```

---

# Assignment 1 – Dataset Processing

The first part of the project focuses on preparing a clean English–Hindi parallel dataset.

The processing pipeline performs the following steps:

- Loads the English and Hindi sentence pairs
- Calculates the word count for both languages
- Keeps only sentence pairs where:
  - English sentence length is between **5 and 50 words**
  - Hindi sentence length is between **5 and 50 words**
- Computes the word count difference between English and Hindi
- Retains only sentence pairs where the difference lies between **-10 and +10**
- Exports the cleaned dataset to an Excel file

### Output

```
assignment1_dataset_processing/output/
└── cleaned_english_hindi_dataset.xlsx
```

The Excel file contains the following columns:

- English Sentence
- Hindi Sentence
- Word Count (English)
- Word Count (Hindi)
- Difference (English − Hindi)

---

# Assignment 2 – Machine Translation

The second assignment translates English sentences into Hindi using a Hugging Face translation model.

For this project I used:

```
Helsinki-NLP/opus-mt-en-hi
```

The script translates the first **100 English sentences** from the cleaned dataset and compares the generated translations with the reference Hindi sentences.

The translation quality is evaluated using:

- BLEU
- CHRF
- TER (Translation Edit Rate)

---

# Output

```
assignment2_translation/output/

translations.xlsx
scores.txt
```

### translations.xlsx

Contains:

- Original English Sentence
- Model Generated Hindi Translation

### scores.txt

Contains:

- BLEU Score
- CHRF Score
- TER Score
- Model Name
- Number of Sentences Evaluated

---

# Installation

Clone the repository

```bash
git clone https://github.com/devopsrudr/Assessment-1-English-Hindi-Dataset-Processing-and-Analysis

cd English-Hindi-Translation-Assessment
```

---

# Install Dependencies

For Assignment 1

```bash
cd assignment1_dataset_processing

pip install -r requirements.txt
```

For Assignment 2

```bash
cd assignment2_translation

pip install -r requirements.txt
```

---

# Running Assignment 1

Download the dataset (only once if required)

```bash
python download_dataset.py
```

Process the dataset

```bash
python process_dataset.py
```

---

# Running Assignment 2

Run the complete translation pipeline

```bash
bash setup_and_run.sh
```

or manually

```bash
python translate_and_evaluate.py
```

---

# Evaluation Metrics

### BLEU

Measures how closely the generated translation matches the reference translation based on n-gram overlap.

Higher score indicates better translation quality.

### CHRF

Evaluates translations using character-level n-grams.

It generally performs well for morphologically rich languages such as Hindi.

Higher score is better.

### TER

Translation Edit Rate measures how many edits are required to transform the generated translation into the reference translation.

Lower score indicates better performance.

---

# Technologies Used

- Python 3
- Pandas
- Hugging Face Datasets
- Hugging Face Transformers
- PyTorch
- SacreBLEU
- OpenPyXL

---

# Notes

- The translation model is downloaded automatically the first time the script is executed.
- After the initial download, all future runs use the locally cached model.
- The raw dataset is not included in this repository because it is distributed under Hugging Face's access policy. Please download it separately before running the scripts.

---

# Author

**Rudra Banerjee**

This repository was created as part of an English–Hindi Dataset Processing and Machine Translation assessment.future runs will be significantly faster.
Only the first 100 English sentences from the cleaned dataset are translated, as required in the assignment.
