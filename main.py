import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEVICE_DIR = os.path.join(BASE_DIR, "devices")


def run_script(script_name):
    script_path = os.path.join(DEVICE_DIR, script_name)
    subprocess.run(["python", script_path])

    input("\nPress Enter to return to the main menu...")

while True:

    print("\n")
    print("=" * 55)
    print(" BLOCKCHAIN-BASED IDENTIFICATION & VERIFICATION SYSTEM")
    print("=" * 55)

    print("1. Register Device")
    print("2. Authenticate Device")
    print("3. Query Device")
    print("4. Revoke Device")
    print("5. View Blockchain Events")
    print("6. Exit")

    print("=" * 55)

    choice = input("Select an option: ")

    if choice == "1":
        run_script("register_device.py")

    elif choice == "2":
        run_script("authenticate_device.py")

    elif choice == "3":
        run_script("query_device.py")

    elif choice == "4":
        run_script("revoke_device.py")

    elif choice == "5":
        run_script("view_events.py")

    elif choice == "6":
        print("\nThank you for using the system.")
        break

    else:
        print("\nInvalid option. Please try again.")