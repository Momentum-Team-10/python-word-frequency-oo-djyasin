import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as text:
        line = text.read()
        print(f"{len(line)} lines in the file.")
#"""calling text rather than line to enable it to form word list instead of line list"""
        for text in line:
            line = line.replace(",", "")
            line = line.replace(".", "")
            line = line.replace("-", "")
            line = line.replace("?", "")
            line = line.replace(":", "")
            line = line.replace("'", "")
            line = line.replace(";", "")
            line = line.replace("/n", "")
            line = line.lower()
            line = line.split(" ")
            print(line)
#"""somehow count words"""
# (file).remove STOP_Words
# Are we trying to get thee exact words from the stop list, OR get the top frequencies


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

""""this calls the file to run"""
file = Path(args.file)
if file.is_file():
    print_word_freq(file)
else:
    print(f"{file} does not exist!")
    exit(1)