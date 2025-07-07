# 📦 Install the sumy library first by running:
# pip install sumy

from sumy.parsers.plaintext import PlaintextParser   # Used to parse plain text input
from sumy.nlp.tokenizers import Tokenizer            # Used to split text into sentences/words
from sumy.summarizers.lsa import LsaSummarizer       # LSA (Latent Semantic Analysis) summarization technique

def summarize_text(text, sentence_count=2):
    """
    This function takes in a long text and gives you a shorter summary.
    You can control how short the summary is by changing 'sentence_count'.
    """
    
    # Step 1: Convert the raw text into a format that the summarizer can understand
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Step 2: Create the summarizer (you can try other ones like LexRank too!)
    summarizer = LsaSummarizer()

    # Step 3: Generate the summary with the desired number of sentences
    summary = summarizer(parser.document, sentence_count)

    # Step 4: Convert summary sentences into a single string to return
    return " ".join(str(sentence) for sentence in summary)


# 📝 Let's try it out with some sample text
input_text = """
Artificial Intelligence (AI) is transforming industries by enabling machines to learn from data, make decisions, and automate tasks.
From healthcare and finance to transportation and entertainment, AI technologies such as machine learning, natural language processing,
and robotics are improving efficiency and opening new possibilities.
However, challenges such as data privacy, bias, and job displacement must be addressed to ensure ethical and inclusive AI development.
"""

# 👇 You can change sentence_count to get shorter or longer summaries
summary = summarize_text(input_text, sentence_count=2)

# 🖨️ Show the original and summarized text
print("🔹 Original Text:\n")
print(input_text)
print("\n🔸 Summarized Version:\n")
print(summary)
