import time

KB_SIZE = 2 ** 10
MB_SIZE = 2 ** 20
DELIMITER = ','
ENCODING = "latin_1"


def fill_choices():
    result = ['\n', '\r']
    for i in range(ord('a'), ord('z') + 1):
        result.append(chr(i))
    # for i in range(ord('A'), ord('Z') + 1):
    #     result.append(chr(i))
    for i in range(ord('0'), ord('9') + 1):
        result.append(chr(i))
    return result


def generate_testcase(length: int):
    s1 = time.time()
    input_file = "input.txt"
    compressed_file = "input_compressed.txt"
    decoded_file = "input_decoded.txt"
    x = []
    # length *= KB_SIZE
    choices = fill_choices()
    for i in range(length):
        y = random.choice(choices)
        x.append(str(y))
    f = open(input_file, "w", newline='', encoding=ENCODING)
    f.write("".join(x))
    f.close()
    encoder = Encoder(input_file)
    encoder.encode()
    decoder = Decoder(compressed_file)
    decoder.decode()
    print(f'Generated case in: {(time.time() - s1)}')
    return (filecmp.cmp(input_file, decoded_file, shallow=False))


def test_till_failure():
    ans = generate_testcase(100)
    while ans:
        ans = generate_testcase(100)


