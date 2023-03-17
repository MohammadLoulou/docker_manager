import datafetcher
import paramiko
from commandgrabber import CommandGrabber
import pandas as pd
from handlejson import HandleJson
import matplotlib.pyplot as plt


class SshRequest:
    """
        A class for executing commands on remote Docker containers via SSH.

        Attributes:
            None.
    t
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
        handle = HandleJson()
        dict = fetcher.getJson("config.json")
        columns = []
        cmd = ""
        cmd_park = input("Type exit to quit, what park do you want to select? ")
        handle.create_json("commandes.json")

        df = handle.get_json_data_to_dataframe("commandes.json")

        # df = pd.read_json("commandes.json")

        while cmd != "exit":
            cmd = input("Type a command : ")
            if cmd == "change_park":
                cmd_park = input("Type a command ")
                continue
            columns.append(cmd)
            handle.add_to_dataframe(df, cmd)
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

                        print(str(output, "utf8"))  # type: ignore
        # plot = df.plot.pie()
        plot_data = df[columns]
        plot = plot_data.sum().plot(subplots=True, kind="pie")
        plt.legend(columns)
        # plot = df.plot(kind="pie", y=cmd)
        plt.show()
        handle.df_to_json(df, "commanded.json")
        return
