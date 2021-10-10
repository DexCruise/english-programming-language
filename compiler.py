# compiles English to python.
import sys

args = sys.argv

english_file = open(args[-1], "r").read()
output = open(args[-1] + ".output.py", "w")

quote_tokens = []
for i in zip(english_file, range(len(english_file))):
    if i[0] == '"':
        quote_tokens += [i[1]]

print("quote tokens:", quote_tokens)
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
            english_file[0:start] + "__quotation__" + str(len(quotations) - 1) + english_file[end + 1:len(english_file)]

print("quotations:", quotations)
print("file lexed for quotations: '" + english_file + "'")

sentences = english_file.split('.')

print("sentences:", sentences)


def parse_sentence_object(object_to_parse: str):
    if "__quotation__" in object_to_parse:
        return quotations[int(object_to_parse.split("__quotation__")[1])]


def execute(func, subject):
    return func(subject)


class Output:
    @staticmethod
    def says(text_to_say: str) -> str:
        return "print('" + text_to_say + "')"


common_nouns = {
    "Output": {
        "says": Output.says
    }
}

output_lines = []
for i in sentences:
    if i == '':
        continue
    words = i.split(' ')
    print("words:", words)

    sentence_subject = words.pop(0)
    sentence_verb = words.pop(0)
    sentence_object = words.pop(0)

    method_to_execute = common_nouns[sentence_subject][sentence_verb]
    output_lines += [execute(method_to_execute, parse_sentence_object(sentence_object))]

output.write('\n'.join(output_lines))