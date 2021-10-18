from pymavlink import mavutil
# Create the connection
# master = mavutil.mavlink_connection('udpin:127.0.0.1:14550')
# Wait a heartbeat before sending commands

# Send a positive x value, negative y, negative z,
# positive rotation and no button.
# https://mavlink.io/en/messages/common.html#MANUAL_CONTROL
# Warning: Because of some legacy workaround, z will work between [0-1000]
# where 0 is full reverse, 500 is no output and 1000 is full throttle.
# x,y and r will be between [-1000 and 1000].


class Command:
    def __init__(self):
        self.master = mavutil.mavlink_connection('/dev/ttyACM0')
        self.master.wait_heartbeat()

    # this function will control the servo
    def send_command(self, x, y, z, t):
        self.master.mav.manual_control_send(
            self.master.target_system,
            x,
            y,
            z,
            t,
            0)


# test
a = Command()
a.send_command(0, -1000, 0, 1000)

