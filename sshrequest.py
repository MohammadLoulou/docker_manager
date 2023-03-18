import datafetcher
import paramiko
from commandgrabber import CommandGrabber
import pandas as pd
from handlejson import HandleJson
import matplotlib.pyplot as plt
import json


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

        cmd = ""
        park_num = input("what park do you want to select? ")

        while cmd != "exit":

            cmd = input("Type exit to quit,Type a command : ")

            if cmd == "change_park":
                park_num = input("what park do you want to select?")
                continue
            columns = [cmd]

            for container in dict:
                json_name = container["container_name"] + ".json"
                handle.open_json(json_name)
                df = handle.json_data_to_dataframe(json_name)
                if park_num in container["parks"]:
                    handle.add_to_dataframe(df, cmd)
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
                        handle.df_to_json(df, json_name)
                        print(str(output, "utf8"))
        # plot = df.plot.pie()
        for container in dict:
            data = json.load(open(container["container_name"] + ".json"))
            plt.pie(data.values(), labels=data.keys())
            plt.savefig(container["container_name"])

        return
