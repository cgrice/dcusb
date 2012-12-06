"""Driver for DreamCheeky LED Message board

USB IDs for DreamCheeky LED Messageboard:

Vendor ID: 0x1D34
Product ID: 0x0013
"""


import usb
import alphabet
import time


class LEDMessageBoard:

    def __init__(self, vendor_id=0x1D34, product_id=0x0013):
        """Set up driver with usb device

        Keyword arguments:
        vendor_id -- the USB vendor_id (default 0x1D34)
        product_id -- the imaginary part (default 0x0013)

        USB ids can be found using `lsusb` on Linux and using
        `system_profiler SPUSBDataType` on OSX

        """

        self.device = usb.core.find(idVendor=vendor_id,
                                    idProduct=product_id)

        # Need to detach from kernel in order to claim device
        try:
            if self.device.is_kernel_driver_active(0) is True:
                self.device.detach_kernel_driver(0)
        except AttributeError:
            raise LEDUsbError('LED Message board not connected')

        # Set up framebuffer representing 21x7 grid of LEDs.
        # 1 = off
        # 0 = on
        self.screen = {}

        for i in range(7):
            self.screen[i + 1] = [1 for n in range(21)]

        # Keep a copy of the clear screen to quickly wipe display
        self.cleared_screen = dict(self.screen)

    def print_screen(self):
        """Print a string representation of the LED display.
        Useful for debugging"""
        for row in self.screen:
            print self.screen[row]

    def write_char(self, char, xloc, glyph=None):
        """Write a single character to the framebuffer.
        Does not update display.

        Arguments:
        char -- character to write. This gets translated to glyph
                by alphabet.py
        xloc -- x location on the framebuffer to write.

        Keyword arguments:
        glyph -- A representation of an icon to display on the screen.

        Returns the x location of the end of the character

        """
        # grab char to glyph conversion from alphabet.py
        if glyph is None:
            glyph = alphabet.convert(char)

        # For each line of the display, update only the rows between
        # xloc and xloc + len(glyph)
        for y in self.screen:
            line = self.screen[y]
            for x in range(xloc, xloc + len(glyph[y])):
                if x >= len(self.screen[y]):
                    # Need to extend the framebuffer to write this character
                    self.screen[y].append(glyph[y][x - xloc])
                else:
                    self.screen[y][x] = glyph[y][x - xloc]

        return xloc + len(glyph[1])

    def write_string(self, string, xloc):
        """Write string of characters to framebuffer, starting at x location
        defined by xloc. Does not update display

        """
        for char in string:
            xloc = self.write_char(char, xloc)

    def clear_screen(self):
        self.screen = self.cleared_screen
        self.push_screen()

    def scroll_message(self, string, xloc=21, speed=10):
        """Scroll a message across the LED screen. Updates display.

        """

        self.write_string(string, xloc)
        self.push_screen()
        sleep_time = float(1) / speed
        for i in range(len(self.screen[1])):
            self.scroll()
            self.push_screen()
            time.sleep(sleep_time)

    def scroll(self):
        for row in self.screen:
            line = self.screen[row]
            for i in range(len(line)):
                if i - 1 > 0:
                    self.screen[row][i - 1] = self.screen[row][i]
                if i + 1 < len(line):
                    self.screen[row][i] = self.screen[row][i + 1]
                else:
                    self.screen[row][i] = 1

    def push_screen(self):
        lines = []
        for row in self.screen:
            line = self.screen[row][0:21]
            # line.reverse()
            lines.append(line)

        # Step through the LEDs in groups of 2 rows
        for i in range(0, len(lines), 2):

            # We need to slice each row of the LED representation into
            # 3 byte arrays LED bits run from right to left, so we need to
            # reverse our slices
            byte_4_range = reversed(
                [unicode(item) for item in lines[i][0:8]]
            )
            byte_3_range = reversed(
                [unicode(item) for item in lines[i][8:16]]
            )
            byte_2_range = reversed(
                [unicode(item) for item in lines[i][16:21]]
            )

            # Convert from binary to int
            byte_4 = int(''.join(byte_4_range), 2)
            byte_3 = int(''.join(byte_3_range), 2)
            byte_2 = int(''.join(byte_2_range), 2)

            # We need to send the board an 8-byte packet - however the board
            # only has 7 rows, so we just pad the last 3 bytes if we're past
            # the last row
            if(i < 6):
                # Note the i+1 here to get the next row
                byte_7_range = reversed(
                    [unicode(item) for item in lines[i + 1][0:8]]
                )
                byte_6_range = reversed(
                    [unicode(item) for item in lines[i + 1][8:16]]
                )
                byte_5_range = reversed(
                    [unicode(item) for item in lines[i + 1][16:21]]
                )

                byte_7 = ''.join(byte_7_range)
                byte_6 = ''.join(byte_6_range)
                byte_5 = ''.join(byte_5_range)
            else:
                byte_7 = '11111111'
                byte_6 = '11111111'
                byte_5 = '11111111'

            # Convert from binary to int
            byte_7 = int(byte_7, 2)
            byte_6 = int(byte_6, 2)
            byte_5 = int(byte_5, 2)

            # Byte 0 should denote brightness, with 2 being minimum,
            # and 0 maximum. However the DreamCheeky doesn't seem to have any
            # brightness settings, so we just set this to max
            byte_0 = int('0x00', 16)
            # Byte 1 selects the row index - we update in groups of two
            byte_1 = int(hex(i), 16)

            bytes = [
                byte_0,
                byte_1,
                byte_2,
                byte_3,
                byte_4,
                byte_5,
                byte_6,
                byte_7
            ]

            self.send_packet(bytes)

    def send_packet(self, bytes):
        return self.device.ctrl_transfer(0x21, 0x09, 0, 0, bytes)


class LEDUsbError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
