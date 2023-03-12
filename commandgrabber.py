class CommandGrabber:
    """
    A class that represents a command grabber (from an input).

    Methods
    -------
    send_commands(self, filename, input, output):
        Writes the input command and its corresponding output to a specified file.

    Attributes
    ----------
    None.
    """

    def send_commands(self, filename, input, output):
        """
        Writes the input command and its corresponding output to a specified file.

        Parameters
        ----------
        filename : str
            The name of the file to write the command and output to.
        input : str
            The command input.
        output : str
            The output of the command.

        Returns
        -------
        None
        """
        with open(filename, "a") as file:
            file.write(input + "\n")
            file.write(output)
