import tempfile
import os.path


class File:

    def __init__(self, filename):
        self.filename = filename
        self.PathFile = os.path.join(tempfile.gettempdir(), filename)
        if os.path.exists(self.PathFile) is False:
            with open(self.PathFile, 'tw') as file:
                pass

    def write(self, text):
        with open(self.PathFile, 'tw') as file:
            file.write(text)
            return len(text)

    def read(self):
        with open(self.PathFile, 'tr') as file:
            return file.read()

    def __str__(self):
        return self.PathFile

    def __add__(self, other):
        temp = tempfile.NamedTemporaryFile(prefix='pp', delete=False)
        file = File(temp.name)
        file.write(self.read() + other.read())
        return file

    def __getitem__(self, line):
        lines = self.read().split('\n')
        if lines[-1] == '':
            lines.pop(-1)
        if len(lines) != 1:
            for i in range(len(lines)):
                lines[i] += '\n'
        return lines[line]
