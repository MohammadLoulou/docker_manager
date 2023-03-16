from sshrequest import SshRequest


def main():
    """
    Create an instance of SshRequest class

    Then we call its main method on
    If this file is run directly so we run the main function.

    Parameters
    ----------
    None

    Returns
    ------
    None
    """
    request = SshRequest()
    request.main()


if __name__ == "__main__":
    main()
