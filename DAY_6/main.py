def message_decoder(bits: int):

    with open("input", "r") as file:
        content = file.read()
        for i in range(0, len(content), 1):
            packet = set(content[i:i+bits])
            if len(packet) == bits:
                print(i+bits)
                break


if __name__ == "__main__":
    # task 1
    message_decoder(4)
    # task 2
    message_decoder(14)
