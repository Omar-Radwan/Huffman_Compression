class InputReader:
    def __init__(self, file_name):
        self.buffer = []
        self.file_name = file_name

    def read_meta_data(self):
        file = open("output.txt", "r")
        number_of_codes = int(file.readline(1))
        # print(k)
        huffman_codes = {}
        for line in file:
            if number_of_codes == 0:
                break
            info = line.split(" ")
            key = info[0]
            value = info[1].split('\n')
            huffman_codes[value[0]] = key
            number_of_codes -= 1
        file.close()
        print(huffman_codes)

    def fill_buffer(self):
        pass

    def file_ended(self):
        return False
