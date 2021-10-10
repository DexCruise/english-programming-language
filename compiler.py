# compiles English to python.
import sys
args = sys.argv

english_file = open(args[-1], "r").read()


quote_tokens = []
for i in zip(english_file, range(len(english_file))):
    if i[0] == '"':
        quote_tokens += [i[1]]

print(quote_tokens)
quotations = []
while quote_tokens:
    start = quote_tokens.pop(0)
    try:
        end = quote_tokens.pop(0)
    except IndexError:
        print("fatal error: no corresponding end quote to the start quote at character number", start + 1)
        exit()
    else:
        quotations += [english_file[start + 1:end:]]
        english_file = \
            english_file[0:start] + "string_" + str(len(quotations) - 1) + english_file[end + 1:len(english_file)]

print("quotations:", quotations)
print("file lexed for quotations:", english_file)

# sentences = '.'.split(english_file)
