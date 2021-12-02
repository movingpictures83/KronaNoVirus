import sys

class KronaNoVirusPlugin:
    def input(self, filename):
        self.infile = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
        outfile = open(filename, 'w')
        viralKingdoms = ['unclassified bacterial viruses', 'Duplodnaviria']
        for line in self.infile:
            contents = line.strip().split('\t')
            if (len(contents) > 3 and contents[3] not in viralKingdoms):
                outfile.write(line)

