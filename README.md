# Assignment 2 — Translation with an LLM (local, open-source)

Translates 100 English sentences (from Assignment 1's cleaned dataset) into
Hindi using a local Hugging Face MT model, then scores the translations
against the dataset's own Hindi sentences using BLEU, CHRF, and TER.

## Prerequisites
- You must have already run Assignment 1
  (`assignment1_dataset_processing/process_dataset.py`) so that
  `assignment1_dataset_processing/output/cleaned_english_hindi_dataset.xlsx`
  exists.
- Internet access (to download the translation model the first time).

## Steps (VS Code)

1. Open this folder (`assignment2_translation`) in VS Code, or open the whole
   project root — either works since paths are resolved relative to the
   script's own location.

2. Open a terminal (`Terminal > New Terminal`) and run:
   ```bash
   bash setup_and_run.sh
   ```
   This creates a virtual environment, installs everything (`transformers`,
   `torch`, `sacrebleu`, etc.), and runs the translation + scoring script
   with default settings (100 sentences, `Helsinki-NLP/opus-mt-en-hi` model).

   *(Alternative: press `Cmd+Shift+B` — runs the same task.)*

3. Wait for it to finish. On CPU, translating 100 short sentences with this
   model typically takes well under a minute (after the one-time model
   download).

## Output
- `output/translations.xlsx` — Column A: original English sentence,
  Column B: model-generated Hindi translation.
- `output/scores.txt` — BLEU, CHRF, and TER scores, plus which model was
  used and how many sentences were evaluated.

## Customizing
Run with different options directly:
```bash
source venv/bin/activate
python3 translate_and_evaluate.py --num-sentences 100 --model Helsinki-NLP/opus-mt-en-hi
```

To try a different (possibly higher-quality) model, e.g. NLLB-200:
```bash
python3 translate_and_evaluate.py --model facebook/nllb-200-distilled-600M
```
Note: some models on Hugging Face require you to click "Agree" on their page
and use an access token (same process as Assignment 1) — `opus-mt-en-hi` does
**not** require this, it's fully open.

## Metrics explained
- **BLEU** (0–100, higher is better): n-gram precision overlap with the
  reference translation.
- **CHRF** (0–100, higher is better): character n-gram F-score; tends to
  correlate better with human judgment for morphologically rich languages
  like Hindi.
- **TER** (Translation Edit Rate, lower is better, can exceed 100): the
  percentage of edits needed to turn the model output into the reference.
