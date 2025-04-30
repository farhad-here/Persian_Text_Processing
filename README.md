# 📝 Persian Text Processing with Parsivar

This project demonstrates how to process Persian (Farsi) text using the [Parsivar](https://github.com/ICTRC/Parsivar) NLP library. It includes text normalization, tokenization, stemming, and spell checking, with additional tools to handle proper display of Persian characters.

---

## 🔍 Features

- ✅ **Normalization** – Cleans and standardizes Persian text.
- ✅ **Tokenization** – Splits text into sentences and words.
- ✅ **Stemming** – Converts words to their root forms.
- ✅ **Spell Checking** – Detects and corrects misspellings in Persian.
- ✅ **Display Support** – Uses `arabic_reshaper` and `python-bidi` to fix RTL display issues.

---

## 🧰 Libraries Used

- [`parsivar`](https://github.com/ICTRC/Parsivar) – NLP tools for Persian.
- `arabic_reshaper` – For reshaping characters to correct forms.
- `python-bidi` – Ensures proper display of RTL scripts like Persian.

---

## 📌 How It Works

1. Read Persian text from a `.txt` file.
2. Normalize the text using Parsivar.
3. Tokenize the normalized text into words and sentences.
4. Apply stemming to get root forms of words.
5. Use spell correction on custom input.
6. Display reshaped output for better readability in terminals.

---

## 🚀 Usage

### Install dependencies:

```bash
pip install parsivar arabic_reshaper python-bidi
```

```
pip install -r requirements.txt
```

then in code first we normalize then we tokenize, and after tokenize we stammer and in the end for spell detection you need to download these two files and put it in the this below path:
```
first create a spell folder in this path:
venv\Lib\site-packages\parsivar\resource
```
```
then replace these two file in the spell folder:
- onegram.pckl
- mybigram_lm.pckl
```
#### 🔽<a href='https://www.dropbox.com/scl/fi/4lspgdqw0yym6w2ewhcs7/spell.zip?e=3&file_subpath=%2Fmybigram_lm.pckl&rlkey=fl0moighiw7s46pgorz1xjtg0&dl=0'>Download two files from here</a>

# 🎥preview

![3Capture](https://github.com/user-attachments/assets/c7e53bb6-c552-4e4d-914a-6eba692f4b1d)

# 📳technology
- python
- nltk
- parsivar
- bidi
- arabic_reshaper
