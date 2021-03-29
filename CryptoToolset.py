#!/usr/bin/env python3
from Encryptor import Encrypt
from Decryptor import Decrypt


# print statement made into a function so it can be collapsed in IDE and not get in the way
def pr_splash_screen():
    # CRYPTO KIT
    print("__________________________________________________________________________________")
    print("||   ██████ ██████  ██    ██ ██████  ████████  ██████ "
          "     ██   ██ ██ ████████  ||")

    print("||  ██      ██   ██  ██  "
          "██  ██   ██    ██    ██    ██"
          "     ██  ██  ██    ██     ||")

    print("||  ██      ██████    ████   ██████     ██    ██    ██"
          "     █████   ██    ██     ||")

    print("||  ██      ██   ██    ██    ██         ██    ██    ██"
          "     ██  ██  ██    ██     ||")

    print("||   ██████ ██   ██    ██    ██         ██     ██████ "
          "     ██   ██ ██    ██     ||")
    print("||------------------------------------------------------------------------------||")

    print("||                                                                              ||")
    print("||                                                                              ||")
    print("||                          Press 1 for RSA Encryption                          ||")
    print("||                          Press 2 for RSA Decryption                          ||")
    print("||                          Press 3 for AES Encryption                          ||")
    print("||                          Press 4 for AES Decryption                          ||")
    print("||                                Press 0 to Exit                               ||")
    print("||                                                                              ||")
    print("||                                                                              ||")
    print("||                                 Liam Gerrior                                 ||")
    print("||______________________________________________________________________________||")


pr_splash_screen()
# creates a list that ensures that a integer that was added corresponds to valid options
valid = [i for i in range(0, 5)]
while True:
    try:
        op = int(input("What would you like to do?\n"))
        if op not in valid:
            print("Invalid Operation. Please try again")
            continue
    except ValueError:
        print("Invalid Operation. Please try again")
        continue

    if op == 0:
        print("Have a secure day!")
        break

    elif op == 1:
        print(r"    ____  _____ ___       ______                            __           ",
              r"   / __ \/ ___//   |     / ____/___  ____________  ______  / /____  _____",
              r"  / /_/ /\__ \/ /| |    / __/ / __ \/ ___/ ___/ / / / __ \/ __/ _ \/ ___/",
              r" / _, _/___/ / ___ |   / /___/ / / / /__/ /  / /_/ / /_/ / /_/  __/ /    ",
              r"/_/ |_|/____/_/  |_|  /_____/_/ /_/\___/_/   \__, / .___/\__/\___/_/     ",
              r"                                            /____/_/                     ", "", sep="\n")

        message = input("Input what needs to be encrypted:\n")
        Encrypt().rsa(message)
        break

    elif op == 2:
        print(r"    ____  _____ ___       ____                             __            ",
              r"   / __ \/ ___//   |     / __ \___  ____________  ______  / /____  _____ ",
              r"  / /_/ /\__ \/ /| |    / / / / _ \/ ___/ ___/ / / / __ \/ __/ _ \/ ___/ ",
              r" / _, _/___/ / ___ |   / /_/ /  __/ /__/ /  / /_/ / /_/ / /_/  __/ /     ",
              r"/_/ |_|/____/_/  |_|  /_____/\___/\___/_/   \__, / .___/\__/\___/_/      ",
              r"                                           /____/_/                      ", "", sep="\n")

        Decrypt().dec_rsa()
        break

    elif op == 3:
        print(r"    ___    ___________    ______                            __            ",
              r"   /   |  / ____/ ___/   / ____/___  ____________  ______  / /____  _____ ",
              r"  / /| | / __/  \__ \   / __/ / __ \/ ___/ ___/ / / / __ \/ __/ _ \/ ___/ ",
              r" / ___ |/ /___ ___/ /  / /___/ / / / /__/ /  / /_/ / /_/ / /_/  __/ /     ",
              r"/_/  |_/_____//____/  /_____/_/ /_/\___/_/   \__, / .___/\__/\___/_/      ",
              r"                                            /____/_/                      ", "", sep="\n")

        message = input("Input what needs to be encrypted:\n")
        Encrypt().aes(message)
        break

    elif op == 4:
        print(r"    ___    ___________    ____                             __            ",
              r"   /   |  / ____/ ___/   / __ \___  ____________  ______  / /____  _____ ",
              r"  / /| | / __/  \__ \   / / / / _ \/ ___/ ___/ / / / __ \/ __/ _ \/ ___/ ",
              r" / ___ |/ /___ ___/ /  / /_/ /  __/ /__/ /  / /_/ / /_/ / /_/  __/ /     ",
              r"/_/  |_/_____//____/  /_____/\___/\___/_/   \__, / .___/\__/\___/_/      ",
              r"                                           /____/_/                      ", "", sep="\n")

        Decrypt().dec_aes()
        break
