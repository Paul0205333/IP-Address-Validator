from ipv4 import is_valid_ipv4
from ipv6 import is_valid_ipv6

continue_program = "y"

while continue_program == "y":

    choice = input("Choose IP version (4/6): ")

    if choice == "4":
        ip = input("Enter an IPv4 address: ")
        print(is_valid_ipv4(ip))

    elif choice == "6":
        ip = input("Enter an IPv6 address: ")
        print(is_valid_ipv6(ip))

    else:
        print("Invalid choice. Please choose 4 or 6.")

    continue_program = input("Do you want to continue? (y/n): ").lower()