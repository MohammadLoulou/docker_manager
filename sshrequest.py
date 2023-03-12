import datafetcher
import paramiko
from commandgrabber import CommandGrabber


class SshRequest:
    def main(self):

        fetcher = datafetcher.DataFetcher()
        grabber = CommandGrabber()
        dict = fetcher.getJson(
            "/home/adam/Documents/Docker_management/docker_manager/config.json"
        )

        hostname = dict["ip"]
        port = dict["port"]
        username = dict["user"]
        password = dict["password"]

        """
        hostname = "localhost"
        port = 2022
        username = "sshuser"
        password = ""
        """
        # private_key = paramiko.Ed25519Key.from_private_key_file(dict["private_key"])
        private_key = paramiko.Ed25519Key.from_private_key_file("keys")
        cmd = ""
        print("Type exit to quit")
        while cmd != "exit":
            cmd = input("Type a commande : ")

            with paramiko.SSHClient() as client:

                client.load_system_host_keys()
                client.connect(hostname, port, username, password, pkey=private_key)
                # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                # client.connect(hostname="localhost", port=2022, username=username, password="")

                (stdin, stdout, stderr) = client.exec_command(cmd)

                output = stdout.read()
                output_sent = output.decode("utf-8")
                # pw_bytes.decode("utf-8")
                grabber.send_commands("cmds_list.txt", cmd, output_sent)
                print(str(output, "utf8"))
