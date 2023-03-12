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
        cmd = ""
        print("Type exit to quit")
        while cmd != "exit":
            cmd = input("Type a command : ")
        for container in dict:

            hostname = container["ip"]
            port = container["port"]
            username = container["user"]
            password = container["password"]
            private_key = paramiko.Ed25519Key.from_private_key_file(
                container["private_key"]
            )


            with paramiko.SSHClient() as client:

                client.load_system_host_keys()
                #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname, port, username, password, pkey=private_key)
                (stdin, stdout, stderr) = client.exec_command(cmd)
                output = stdout.read()
                output_sent = output.decode("utf-8")
                grabber.send_commands("cmds_list.txt", cmd, output_sent)

                print(str(output, "utf8"))
