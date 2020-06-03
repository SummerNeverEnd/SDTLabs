class Text(object):

    def __init__(self):
        self.text = ""

    def get_text_from_file(self, _n_o_f="input.txt"):
        self.text = ""
        with open(_n_o_f, "r") as f:
            for i in f.read().strip():
                self.text += i

    def get_text_from_console(self):
        self.text = ""
        self.text = input()

    def append_text_from_file(self, _n_o_f="input.txt"):
        self.text += " "
        with open(_n_o_f, "r") as f:
            for i in f.read().strip():
                self.text += i

    def append_text_from_console(self):
        self.text = self.text + " " + input()

    def print_text(self):
        print(self.text)

    def set_text_from_arg(self, string):
        self.text = string

    def get_text(self):
        return self.text

    def set_text_to_file(self, _n_o_f="output.txt"):
        with open(_n_o_f, "w") as f:
            f.write(self.text)

class Editor(object):

    @staticmethod
    def find_and_replace(text, word, replacement):
        text.text = text.text.replace(word, replacement)


class Analyzer(object):

    def __init__(self, text_):

        self.text = text_

    def avg_word_length(self):
        counter = 0
        summary = 0
        for i in self.text.text.split():
            counter += 1
            summary += len(i)
        return float(summary) / float(counter)

    def max_len(self):
        max_len = 0
        for i in self.text.text.split():
            max_len = max(max_len, len(i))
        return max_len


if __name__ == "__main__":
    someText = Text()
    someText.get_text_from_console()
    someText.print_text()
    someText.append_text_from_console()
    someText.print_text()
    Editor.find_and_replace(someText, "to", "TO")
    someText.print_text()
    someText.get_text_from_file()
    someText.print_text()
    someText.append_text_from_file("update.txt")
    Editor.find_and_replace(someText, "work", "WORK")
    someText.print_text()
    analyzer = Analyzer(someText)
    someText.set_text_from_arg("a bb ccc")
    someText.set_text_to_file()
    print(analyzer.avg_word_length())

