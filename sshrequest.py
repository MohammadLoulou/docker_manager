import datafetcher
import paramiko
from commandgrabber import CommandGrabber


class SshRequest:
    """
    A class for executing commands on remote Docker containers via SSH.

    Attributes:
        None.

    Methods:
        main(): Executes commands on remote Docker containers using SSH connection.
    """

    def main(self):
        """
        Executes commands on remote Docker containers using SSH connection.

        This method establishes an SSH connection with a Docker container, retrieves the command to execute from the user,
        and then executes the command on the remote container. The output of the command is also saved to a file.

        Args:
            self: The object instance.

        Returns:
            None.
        """

        fetcher = datafetcher.DataFetcher()
        grabber = CommandGrabber()
        dict = fetcher.getJson("config.json")
        cmd = ""
        cmd_park = input("Type exit to quit, what park do you want to select? ")
        while cmd != "exit":
            cmd = input("Type a command : ")
            if cmd == "change_park":
                cmd_park = input("Type a command ")
                continue
            for container in dict:
                if cmd_park in container["parks"]:
                    hostname = container["ip"]
                    port = container["port"]
                    username = container["user"]
                    password = container["password"]
                    private_key = paramiko.Ed25519Key.from_private_key_file(
                        container["private_key"]
                    )
                    with paramiko.SSHClient() as client:

                        client.load_system_host_keys()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        client.connect(
                            hostname, port, username, password, pkey=private_key
                        )
                        (stdin, stdout, stderr) = client.exec_command(cmd)
                        output = stdout.read()
                        output_sent = output.decode("utf-8")
                        grabber.send_commands("cmds_list.txt", cmd, output_sent)

                        print(str(output, "utf8"))
        return
