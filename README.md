# NMT French to English Model

This repository contains the training notebook of the Neural Machine Translation (NMT) model  to translate French text to English. It uses state-of-the-art transformer-based architecture for high-quality translations. This repository includes the fine-tuned model and information on how to use it.

For more information of the model, visit [my Hugging Face Profile](https://huggingface.co/nambn0321).

## Model Overview

- Model Name: NMT_opus_fr_en

- Task: Neural Machine Translation (NMT) from French to English

- Architecture: Transformer-based model MarianMT

- Fine-tuned on: Parallel French-English data from the Opus corpus

## Live Demo

You can try [the French to English translation](https://huggingface.co/spaces/nambn0321/opus_NMT_fr_en) live.

## Model Performance
input here

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

Evaluation: The model has been evaluated on a French-English translation test set from the Opus corpus.

Translation Context: The model works best for general, non-specialized language but may require additional fine-tuning for specific domains.
