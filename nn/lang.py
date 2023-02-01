import string
from pprint import pprint

vocabulary = sorted(list(set(string.printable)))

str_to_int = {character: index for index, character in enumerate(vocabulary)}
int_to_str = {index: character for index, character in enumerate(vocabulary)}

pprint(str_to_int)
print()
pprint(int_to_str)

# This is a word tokenizer basically.
encode_string_to_int_array = lambda phrase: [str_to_int[character] for character in phrase]
decode_int_array_to_string = lambda int_arr: "".join([int_to_str[index] for index in int_arr])

pprint(encode_string_to_int_array("Foo bar"))
pprint(decode_int_array_to_string(encode_string_to_int_array("Foo bar")))
