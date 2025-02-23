# This is a structural pattern. Example of a screw which lets say does not fit in a hole which is bigger in size.
# Instead we use an adapter to fit the screw.

class UsbCable:
    def __init__(self):
        self.isplugged = False

    def plugUsb(self):
        self.isplugged = True

class UsbPort:
    def __init__(self):
        self.portAvailable = True

    
    def plug(self, usb):

        if self.portAvailable:
            usb.plugUsb()
            self.portAvailable = False

# UsbCables can plug directly plug into usb ports
usbCable = UsbCable()
usbPort = UsbPort()
usbPort.plug(usbCable)

class MircoUsbCable:
    def __init__(self):
        self.isplugged = False
    
    def plugMicroUsb(self):
        self.isplugged = True

class MicroToUsbAdapter(UsbCable):
    def __init__(self, mircoUsbCable):
        self.microUsbCable = mircoUsbCable
        self.microUsbCable.plugMicroUsb()

    # can override Usbcable.plug() if needed

# MicroUsbCables can plug into UsbPorts via an adapter
microToUsbAdapter = MicroToUsbAdapter(MircoUsbCable())
usbPort2 = UsbPort()
usbPort2.plug(microToUsbAdapter)