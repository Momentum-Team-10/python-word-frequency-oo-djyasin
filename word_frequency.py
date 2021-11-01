from typing import Text


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        with open(self.filename) as file:
            strings = file.read()
            return strings
#            raise NotImplementedError("FileReader.read_contents")


class WordList:
    def __init__(self, text):
        self.text = text

    def extract_words(self):
                self.text = self.text.replace(",", "")
                self.text = self.text.replace(".", "")
                self.text = self.text.replace("-", "")
                self.text = self.text.replace("?", "")
                self.text = self.text.replace(":", "")
                self.text = self.text.replace("'", "")
                self.text = self.text.replace(";", "")
                self.text = self.text.replace("\n", "")
                self.text = self.text.lower()
                self.text = self.text.split(" ")
#               print(self.text)
        # raise NotImplementedError("WordList.extract_words")

    def remove_stop_words(self):
        # """
        # Removes all stop words from our word list. Expected to
        # be run after extract_words.
        # """
        for word in self.text:
            if word in STOP_WORDS:
                self.text.remove(word)
                print(self.text)
#         raise NotImplementedError("WordList.remove_stop_words")

    def get_freqs(self):
        # """
        # Returns a data structure of word frequencies that
        # FreqPrinter can handle. Expected to be run after
        # extract_words and remove_stop_words. The data structure
        # could be a dictionary or another type of object.
        # """
        self.text = sorted(self.text, key=self.text.count, reverse=True)        

        print(self.text)
        
    #    raise NotImplementedError("WordList.get_freqs")


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self, freqs):
        final = {}

        for word in self:
            final[word] = self.freqs.count(word)         
        print(final)

            #  raise NotImplementedError("FreqPrinter.print_freqs")


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
