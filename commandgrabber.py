class CommandGrabber:
    def __init__(self):
        pass

    def send_commands(self, filename, input, output):
        with open(filename, "w") as file:
            file.write(input)
            file.write("\n")
            file.write(str(output))
