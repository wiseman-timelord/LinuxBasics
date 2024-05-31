import os
import sys

def main_menu():
    while True:
        os.system('clear')  # Clear the screen
        print("\n         -= Linux Basics =-\n")
        print("1. Package Updates")
        print("2. Version Information\n")
        choice = str(input("Select; Options=1-2, Exit=X: ")).strip()

        if choice.upper() == 'X':
            print("Exiting...")
            break
        elif choice == '1':
            package_updates_menu()
        elif choice == '2':
            version_information_menu()
        else:
            print("Invalid choice. Please try again.")
            pause()

def package_updates_menu():
    while True:
        os.system('clear')  # Optionally clear the screen here as well
        print("\n    -= Package Updates =-\n")
        print("1. Update package lists")
        print("2. Upgrade all packages")
        print("3. Fix broken dependencies")
        print("4. Remove unused packages\n")
        choice = str(input("Select; Options=1-4, Exit=X: ")).strip()

        if choice.upper() == 'X':
            break
        elif choice == '1':
            update_packages()
        elif choice == '2':
            upgrade_packages()
        elif choice == '3':
            fix_dependencies()
        elif choice == '4':
            autoremove_packages()
        else:
            print("Invalid choice. Please try again.")
        pause()

def version_information_menu():
    while True:
        print("\n      -= Version Information =-\n")
        print("1. Show Python Version")
        print("2. Show Linux Kernel Version")
        print("3. Show System Release Info\n")
        choice = str(input("Select; Options=1-3, Exit=X: ")).strip()

        if choice.upper() == 'X':
            break
        elif choice == '1':
            show_python_version()
        elif choice == '2':
            show_linux_kernel_version()
        elif choice == '3':
            show_system_release_info()
        else:
            print("Invalid choice. Please try again.")
        pause()

def update_packages():
    print("Updating package lists...")
    os.system('sudo apt-get update -y')
    print("Package lists updated.")

def upgrade_packages():
    print("Upgrading all packages...")
    os.system('sudo apt-get upgrade -y')
    os.system('sudo apt-get upgrade --fix-missing -y')
    os.system('sudo apt-get dist-upgrade -y')
    print("Packages upgraded.")

def fix_dependencies():
    print("Fixing broken dependencies...")
    os.system('sudo apt-get -f install -y')
    print("Broken dependencies fixed.")

def autoremove_packages():
    print("Removing unused packages...")
    os.system('sudo apt autoremove -y')
    print("Unused packages removed.")

def show_python_version():
    print("Python Version:")
    print(sys.version)

def show_linux_kernel_version():
    print("Linux Kernel Version:")
    os.system('uname -r')

def show_system_release_info():
    print("System Release Information:")
    os.system('lsb_release -a')

def pause():
    try:
        input("Press any key to continue...")
    except (EOFError, KeyboardInterrupt):
        print("\nContinuing automatically due to input error...")

if __name__ == '__main__':
    main_menu()

