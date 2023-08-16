from ppadb.client import Client

adb = Client(host='localhost', port=5037)
devices = adb.devices()
deviceList=[]
for device in devices:
    deviceList.append(device.serial)
print(deviceList)