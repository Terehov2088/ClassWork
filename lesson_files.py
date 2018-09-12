import string
import time
# f = open('test.txt', 'r+')
# print(type(f))
# print(f.read(1))
#
#
# f.write('hello')
# print(f.tell())
# f.seek(0)
# f.close

text = open('42.txt').read(100)
print(text)

def shift_char(char, shift):
    if char in string.ascii_letters:
        idx = string.ascii_letters.find(char)
        new_idx = (idx + shift) % len(string.ascii_letters)
        char = string.ascii_letters[new_idx]
    return char

def encoder(char):
    return shift_char(char, +5)

def decoder(char):
    return shift_char(char, -5)

def process_file(filepath_in, filepath_out, processor):
    file_in = open(filepath_in)
    file_out = open(filepath_out, 'w+')

    text = file_in.read()

    for char in text:
        new_char = processor(char)
        file_out.write(new_char)

    file_in.close()
    file_out.close()


process_file('42.txt', '42_enc.txt', encoder)
process_file('42_enc.txt', '42.txt', decoder)


def process_file_v2(filepath_in, filepath_out, processor):
    file_in = open(filepath_in)
    file_out = open(filepath_out, 'w+')

    char = file_in.read(1)
    while char != "": # while char:
        new_char = processor(char)
        file_out.write(new_char)
        char = file_in.read(1)

    file_in.close()
    file_out.close()

process_file_v2('42.txt', '42_enc.txt', encoder)
process_file_v2('42_enc.txt', '42.txt', decoder)


def process_file_v3(filepath_in, filepath_out, processor):
    file_in = open(filepath_in)
    file_out = open(filepath_out, 'w+')

    line = file_in.readline()
    while line != "": # while char:
        for char in line:
            new_char = processor(char)
            file_out.write(new_char)
        line = file_in.readline()


    file_in.close()
    file_out.close()
start_time = time.clock()
process_file_v3('42.txt', '42_enc.txt', encoder)
process_file_v3('42_enc.txt', '42.txt', decoder)
end_time = time.clock()
print("Elapsed ms:", end_time - start_time)