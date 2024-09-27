import colorama

from {MODULE}.globals import DEBUG

if DEBUG:
    colorama.init()
    print(
        colorama.Fore.RED
        + "WARNING: Debug mode is enabled. This is meant for development purposes only, and should be disabled before building a release."
        + colorama.Style.RESET_ALL
    )
    input("Press Enter to continue...")
