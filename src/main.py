from equipment import WandererRotatorLite

def print_menu():
    print("\nMenu:")
    print("1. Handshake")
    print("2. Set Home Position")
    print("3. Move Rotator")
    print("4. Set Rotator Backlash")
    print("5. Enable/Disable Rotator Backlash")
    print("6. Reverse Rotator")
    print("7. Abort Rotator")
    print("8. Timer Hit")
    print("9. Home Rotator")
    print("9. Exit")

def main():
    rotator = WandererRotatorLite(port='/dev/rotator', baudrate=19200)
    
    try:
        while True:
            print_menu()
            choice = input("Enter your choice: ")

            try:
                if choice == '1':
                    rotator.handshake()
                    print("Handshake successful")

                elif choice == '2':
                    rotator.set_home_position()
                    print("Home position set")

                elif choice == '3':
                    angle = float(input("Enter angle to move: "))
                    rotator.move_rotator(angle)
                    print(f"Moved to {angle} degrees, current position: {rotator.position}")

                elif choice == '4':
                    steps = int(input("Enter backlash steps: "))
                    rotator.set_rotator_backlash(steps)
                    print("Backlash set")

                elif choice == '5':
                    enabled = input("Enable backlash (yes/no): ").lower() == 'yes'
                    rotator.set_rotator_backlash_enabled(enabled)
                    print("Backlash enabled" if enabled else "Backlash disabled")

                elif choice == '6':
                    enabled = input("Reverse rotator (yes/no): ").lower() == 'yes'
                    rotator.reverse_rotator(enabled)
                    print("Rotator reversed" if enabled else "Rotator normal")

                elif choice == '7':
                    rotator.abort_rotator()
                    print("Rotator aborted")

                elif choice == '8':
                    rotator.timer_hit()

                elif choice == '9':
                    rotator.home_rotator()
                    print("Rotator homed")

                elif choice == '10':
                    break

                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

    finally:
        try:
            rotator.close()
            print("Connection closed")
        except Exception as e:
            print(f"Error closing connection: {e}")

if __name__ == "__main__":
    main()