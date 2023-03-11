import datafetcher
import paramiko


class SshRequest:
    def main(self):

        fetcher = datafetcher.DataFetcher()
        dict = fetcher.getJson("config.json")

        hostname = dict["ip"]
        port = dict["port"]
        username = dict["user"]
        password = dict["password"]
        private_key = paramiko.Ed25519Key.from_private_key_file(dict["private_key"])

        cmd = "uname"

        with paramiko.SSHClient() as client:

            client.load_system_host_keys()
            client.connect(hostname, port, username, password, pkey=private_key)

            (stdin, stdout, stderr) = client.exec_command(cmd)

            output = stdout.read()
            print(str(output, "utf8"))
