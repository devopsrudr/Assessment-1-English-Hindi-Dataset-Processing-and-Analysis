# Assignment 1 — English–Hindi Dataset Processing and Analysis

## Steps

1. **Get the raw data** (skip if `../data/eng.txt` and `../data/hin.txt`
   already exist):
   - Log in at https://huggingface.co/join
   - Visit https://huggingface.co/datasets/ainlpml/english-hindi and click
     **"Agree and access repository"** (it's a gated dataset)
   - Create a Read token: https://huggingface.co/settings/tokens
   - Paste the token into the `.env` file in this folder
   - Run:
     ```bash
     pip install -r requirements.txt
     python download_dataset.py
     ```
   This downloads `eng.txt` and `hin.txt` (10,000 aligned sentence pairs)
   into `../data/`.

2. **Process and filter the dataset:**
   ```bash
   python process_dataset.py
   ```

## What the processing script does
- Loads the 10,000 aligned English/Hindi sentence pairs.
- Computes word count for every sentence (whitespace-token count, works for
  both English and Devanagari script).
- **Filter 1:** keeps only pairs where both English and Hindi word counts
  fall within **5–50**.
- **Filter 2:** of those, keeps only pairs where the word-count difference
  (English − Hindi) falls within **-10 to +10**.
- Writes `output/cleaned_english_hindi_dataset.xlsx` with columns:
  - English Sentence
  - Hindi Sentence
  - Word Count (English) — *live formula*, recalculates if you edit the sentence
  - Word Count (Hindi) — *live formula*
  - Difference (Eng − Hindi) — *live formula*

## Result
From 10,000 raw pairs → **8,214 pairs** survive both filters.

## Note on the raw data
`../data/eng.txt` and `../data/hin.txt` are **not committed to git** (see
`.gitignore`) because the source dataset is gated — redistributing it
directly isn't appropriate. Anyone reproducing this project should run
`download_dataset.py` themselves after agreeing to the dataset's terms.
The final **cleaned Excel output**, which is what the assignment asks you to
submit, **is** committed.
