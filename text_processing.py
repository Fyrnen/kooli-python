class TextProcessor(object):
    def __init__(self, textfile):
        self.file = textfile
        self.text = ""
        self.d = {}
        self.c_count = 0

    def read_file(self):
        ofile = open(self.file, 'r')
        text = ofile.read()
        self.text = text.lower()

    def count_char(self):
        for c in self.text:
            if 97 <= ord(c) <= 122:
                self.c_count += 1
                if c not in self.d:
                    self.d[c] = 1
                else:
                    self.d[c] += 1
                    
    def analyze(self):
        self.read_file()
        self.count_char()

    def print_text(self):
        print(self.text)

    def print_char(self):
        print("All chars:", self.c_count)
        for i in self.d:
            val = int(self.d.get(i))
            p = (val/self.c_count)*100
            p = round(p, 1)
            print(i + ":", val, str(p) + "%")
            #print(repr(i + ":").rjust(2), repr(val).rjust(3), repr(str(p) + "%").rjust(5))

workText = TextProcessor('text.txt')
workText.analyze()
workText.print_char()
