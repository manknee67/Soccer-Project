def read_file(filename):
    infile = open(filename)
    text = infile.read()
    infile.close()
    return text
text = read_file("world_cup_data_4.txt")
split_text = text.split()
print (split_text)
print(split_text[12])
