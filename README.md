Assignment 2 – English to Hindi Translation using an LLM
Overview
In this assignment, I translated English sentences into Hindi using a locally running open-source Large Language Model from Hugging Face. The translated sentences were then evaluated against the original Hindi sentences from the dataset using three standard machine translation metrics: BLEU, CHRF, and TER.
The cleaned dataset generated in Assignment 1 is used as the input for this task.
Requirements
Before running this assignment, make sure that Assignment 1 has been completed successfully. The following file should already be available:
assignment1_dataset_processing/output/cleaned_english_hindi_dataset.xlsx
The translation model will be downloaded automatically the first time the script is executed, so an internet connection is required for the initial setup.
Running the Project
Open the project folder in Visual Studio Code.
Open a new terminal from Terminal → New Terminal.
Run the following command:
bash setup_and_run.sh
This script will:
Create a virtual environment (if needed)
Install all required Python packages
Download the translation model (only on the first run)
Translate the English sentences into Hindi
Calculate BLEU, CHRF, and TER scores
Save all generated outputs automatically
If you prefer, you can also execute the Python script manually after activating the virtual environment.
Output Files
After the script finishes, the following files will be created inside the output folder.
translations.xlsx
This Excel file contains:
English Sentence	Generated Hindi Translation
scores.txt
This file contains:
BLEU Score
CHRF Score
TER Score
Name of the translation model used
Number of sentences evaluated
Running with Different Settings
To run the script manually:
source venv/bin/activate

python3 translate_and_evaluate.py \
    --num-sentences 100 \
    --model Helsinki-NLP/opus-mt-en-hi
You can also experiment with another Hugging Face translation model. For example:
python3 translate_and_evaluate.py \
    --model facebook/nllb-200-distilled-600M
Evaluation Metrics
The quality of the generated translations is measured using three commonly used machine translation metrics.
BLEU
BLEU measures how closely the generated translation matches the reference translation by comparing word sequences. A higher BLEU score generally indicates better translation quality.
CHRF
CHRF compares translations at the character level instead of the word level. Since Hindi is morphologically rich, CHRF often provides a more reliable estimate of translation quality.
TER (Translation Edit Rate)
TER calculates the number of edits required to transform the generated translation into the reference translation. Unlike BLEU and CHRF, a lower TER score indicates better performance.
Model Used
For this assignment, the translation was performed using the Hugging Face model:
Helsinki-NLP/opus-mt-en-hi
This model provides a good balance between translation quality and inference speed, making it suitable for English-to-Hindi machine translation on a local machine.
Notes
The first execution may take a few minutes because the translation model needs to be downloaded.
Once downloaded, the model is cached locally, so future runs will be significantly faster.
Only the first 100 English sentences from the cleaned dataset are translated, as required in the assignment.
