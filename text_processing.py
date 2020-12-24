import spacy

from os import listdir
from os.path import join, isfile


class TextProcessor:
    nlp = spacy.load('en_core_web_sm')

    def __init__(self):
        self.documents = []

        self.vocabulary = []
        self.word2index = {}

    def load_corpus(self, corpus_path):
        for file in listdir(corpus_path):
            file_path = join(corpus_path, file)
            if isfile(file_path):
                print(file_path)
                with open(file_path, 'r') as doc:
                    self.documents.append(TextProcessor.nlp(doc.read()))

    def process_documents(self):
        _vocabulary = set()

        for doc in self.documents:
            # Filter out punctuation and stopwords
            tokens = list(filter(lambda token: not token.is_punct and not token.is_stop, doc))

            # Lemmatization
            tokens = list(map(lambda token: token.lemma_, tokens))

            for token in tokens:
                _vocabulary.add(token)

        for it, token in enumerate(_vocabulary):
            self.vocabulary.append(token.lower())
            self.word2index[token] = it


def main():
    text_processor = TextProcessor()
    text_processor.load_corpus(corpus_path='./corpuses/nuts_and_animals')
    text_processor.process_documents()
    print('Done')


if __name__ == '__main__':
    main()
