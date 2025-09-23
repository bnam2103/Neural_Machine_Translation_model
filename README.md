# NMT French to English Model

This repository contains the training notebook of the Neural Machine Translation (NMT) model  to translate French text to English. It uses a state-of-the-art transformer-based architecture for high-quality translations. This repository includes the fine-tuned model and information on how to use it.

For more information on the model, visit [my Hugging Face Profile](https://huggingface.co/nambn0321/NMT_opus_fr_en).

## Model Overview

- Model Name: NMT_opus_fr_en

- Task: Neural Machine Translation (NMT) from French to English

- Architecture: Transformer-based model MarianMT

- Fine-tuned on: Parallel French-English data from the Opus corpus

## Live Demo

You can try [the French to English translation](https://huggingface.co/spaces/nambn0321/opus_NMT_fr_en) live.

## Model Performance
### **BLEU Scores** (higher is better)
  - **Purpose**: Measures the precision of n-grams (word sequences) in the candidate translation compared to reference translations.
  - **Interpretation**: Higher BLEU scores indicate better word-level overlap with the reference.
  - **Limitations**: Does not account for synonyms or sentence structure.
     
| **Test Set / Model**                         | **Helsinki** | **My Fine-Tuned Model** | **facebook/mbart-large-50-many-to-many-mmt** | **facebook/m2m100_418M** |
|--------------------------------------|--------------|-------------------------|---------------------------------------------|--------------------------|
| **mix of every sources**             | 72.50        | 69.38                   | 68.08                                       | 25.16                    |
| **newsdiscusstest2015-enfr**         | 39.45        | 36.92                   | 37.23                                       | 10.55                    |
| **news-test2008**                    | 27.08        | 24.99                   | 26.49                                       | 7.45                     |
| **newstest2009**                     | 31.11        | 28.50                   | 30.30                                       | 8.14                     |
| **newstest2014-fren**                | 38.99        | 34.72                   | 37.79                                       | 8.37                     |


### **ROUGE-L Scores** (higher is better)
  - **Purpose**: Measures the longest common subsequence (LCS) between the candidate and reference translations.
  - **Interpretation**: Higher ROUGE-L scores indicate better preservation of meaning and content in the translation.
  - **Limitations**: May not fully capture fluency or grammatical correctness.
     
| **Test Set / Model**                        | **Helsinki** | **My Fine-Tuned Model** | **facebook/mbart-large-50-many-to-many-mmt** | **facebook/m2m100_418M** |
|--------------------------------------|--------------|-------------------------|---------------------------------------------|--------------------------|
| **mix of every sources**             | 89.04        | 88.56                   | 86.79                                       | 45.32                    |
| **newsdiscusstest2015-enfr**         | 65.75        | 64.40                   | 63.48                                       | 33.24                    |
| **news-test2008**                    | 54.77        | 53.33                   | 53.85                                       | 25.64                    |
| **newstest2009**                     | 58.25        | 56.44                   | 57.49                                       | 25.65                    |
| **newstest2014-fren**                | 65.97        | 63.82                   | 64.88                                       | 27.76                    |
## Usage
```python
from transformers import pipeline

# Load the NMT model
translator = pipeline(model="nambn0321/NMT_opus_fr_en", task="translation_fr_to_en")

# Translate French text to English
french_text = "Bonjour, comment ça va ?"
english_translation = translator(french_text)

print(english_translation[0]['translation_text'])
```

## Notes

- Evaluation: The model has been evaluated on a French-English translation test set from the Opus corpus.

- Translation Context: The model works best for general, non-specialized language but may require additional fine-tuning for specific domains.
