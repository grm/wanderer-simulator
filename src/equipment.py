import serial
import time

class WandererRotatorLite:
    def __init__(self, port='/dev/ttyUSB0', baudrate=19200):
        self.serial_connection = serial.Serial(port, baudrate, timeout=1)
        self.position = 0
        self.backlash = 0
        self.reverse_coefficient = 1
        self.backlash_compensation = 0
        self.position_history = 0
        self.halt_command = False

    def send_command(self, cmd):
        print(f"Command: {cmd}")
        self.serial_connection.write(cmd.encode())
        time.sleep(1.2)  # Simulate delay
        response = self.serial_connection.readline().decode().strip()
        if response:
            print(f"Response: {response}")
        else:
            print("No response received")
        return response

    def move_rotator(self, angle):
        self.backlash_compensation = 0
        angle -= self.position
        if angle * self.position_history < 0 and angle > 0:
            angle += self.backlash
            self.backlash_compensation = -self.backlash
        elif angle * self.position_history < 0 and angle < 0:
            angle -= self.backlash
            self.backlash_compensation = self.backlash

        position = int(self.reverse_coefficient * angle * 1155)
        self.position_history = angle
        cmd = f"{position}"
        self.send_command(cmd)
        self.position += angle

    def set_home_position(self):
        self.send_command("1500002")
        self.position = 0

    def set_rotator_backlash(self, steps):
        self.backlash = steps / 1155

    def set_rotator_backlash_enabled(self, enabled):
        if enabled:
            self.set_rotator_backlash(self.backlash)
        else:
            self.set_rotator_backlash(0)

    def reverse_rotator(self, enabled):
        self.reverse_coefficient = -1 if enabled else 1

    def abort_rotator(self):
        self.halt_command = True
        self.send_command("HALT")

    def handshake(self):
        self.send_command("1500001")

    def timer_hit(self):
        # Simulate periodic tasks
        print("Timer hit: Performing periodic tasks")

    def home_rotator(self):
        angle = -1 * self.reverse_coefficient * self.position
        self.position_history = angle
        position = int(angle * 1155)
        cmd = f"{position}"
        self.send_command(cmd)
        return "IPS_BUSY"   

    def close(self):
        self.serial_connection.close()