from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8') #읽는건 여기
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")#없으면 sorry
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


path = Path('alice.txt')
count_words(path)