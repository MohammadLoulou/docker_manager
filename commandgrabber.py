class CommandGrabber:
    def __init__(self):
        pass

    def send_commands(self, filename, input, output):
        with open(filename, "a") as file:
            file.write(input + "\n")
            file.write(output)
