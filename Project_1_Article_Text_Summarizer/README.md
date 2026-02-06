# Article Text Summarizer using NLP

## Project Overview
This project implements a simple **Article Text Summarization System** using **Natural Language Processing (NLP)** techniques. The system takes a lengthy article as input and generates a concise summary by extracting the most important sentences from the text.

The project demonstrates how basic NLP techniques can be applied to reduce large amounts of textual data into meaningful summaries.

## Objective
The objective of this project is to understand and implement **extractive text summarization**, where important sentences are selected directly from the original article based on their relevance.

## Technologies Used
- Python  
- Natural Language Processing (NLP)  
- NLTK (Natural Language Toolkit)  

## Project Structure
article_summarizer_nlp/
│
├── summarizer.py
├── sample_text.txt
└── README.md

## Working of the System
1. The input article is read from a text file.
2. Text preprocessing is performed, including:
   - Tokenization
   - Stopword removal
   - Sentence segmentation
3. Word frequency analysis is used to identify important words.
4. Each sentence is scored based on the frequency of important words.
5. Top-ranked sentences are selected to form the final summary.

## How to Run the Project
1. Install Python on your system.
2. Install the required library using:pip install nltk
3. Run the Python script:python summarizer.py


## Input
- A text file (`sample_text.txt`) containing a lengthy article.

## Output
- The original text is displayed.
- A concise summary is generated and printed in the terminal.

## Type of Summarization
- **Extractive Text Summarization**

## Limitations
- The system does not generate new sentences.
- Summary quality depends on word frequency and sentence structure.
- It works best for well-structured articles.

## Conclusion
This project provides a practical understanding of NLP-based text summarization. It demonstrates how simple preprocessing and statistical techniques can be used to extract key information from large textual content.

