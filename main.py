from sshrequest import SshRequest
from commandgrabber import CommandGrabber


def main():
    request = SshRequest()
    commands = CommandGrabber()
    request.main()


if __name__ == "__main__":
    main()
