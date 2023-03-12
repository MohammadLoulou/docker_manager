import datafetcher
import paramiko


class SshRequest:
    def main(self):

        fetcher = datafetcher.DataFetcher()
        dict = fetcher.getJson("config.json")

        for container in dict:

            hostname = container["ip"]
            port = container["port"]
            username = container["user"]
            password = container["password"]
            private_key = paramiko.Ed25519Key.from_private_key_file(
                container["private_key"]
            )

            cmd = "touch battikh.txt"

            with paramiko.SSHClient() as client:

                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname, port, username, password, pkey=private_key)

                (stdin, stdout, stderr) = client.exec_command(cmd)

                output = stdout.read()
                print(str(output, "utf8"))
