
from mosestokenizer import MosesTokenizer


def process_text(fname):
    txt = ''
    tokenize = MosesTokenizer('en')
    with open(fname) as file_in:
        for line in file_in:
            if len(line) > 2:
                line = line.replace("።", ".").replace("፣", ",").replace("፥", ":").replace("፤", ";").replace("፦", "-").replace("፡", " ").replace("፧", "?")
                tok_sent = ' '.join(tokenize(line))
                txt += tok_sent.replace(".", "።").replace(",", "፣").replace(":", "፥").replace(";", "፤").replace("-", "፦") + '\n'
    file_in.close()
    return txt


def main():
    infile = ""
    outfile = ""

    print('Tokenizing', infile,'...')

    txt = process_text("")

    file_out = open("", 'w')
    file_out.write(txt)
    file_out.close()


if __name__ == '__main__':
    main()
