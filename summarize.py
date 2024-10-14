

from gensim.summarization import summarize

def text_summarization(text, ratio=0.2):
    """
    Summarize the given text using TextRank algorithm.

    Args:
    - text (str): The input text to be summarized.
    - ratio (float): The ratio of sentences in the original text to be included in the summary.
                     Default is 0.2 (20%).

    Returns:
    - summary (str): The summarized text.
    """
    summary = summarize(text, ratio=ratio)
    return summary

# Example text
input_text = """
Put your input text here. This could be a lengthy document, an article, or any other piece of text that you want to summarize.
"""

# Call the text summarization function
summary = text_summarization(input_text)

# Print the summary
print(summary)