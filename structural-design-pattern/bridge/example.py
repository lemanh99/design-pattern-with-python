from abc import ABC, abstractmethod


class Device(ABC):

    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def set_volume(self, volume):
        pass

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass


class Tv(Device):
    def __init__(self):
        self.enabled = False
        self.volume = 0
        self.channel = 1

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel


class TV(Device):
    def __init__(self):
        self.enabled = False
        self.volume = 1
        self.channel = 1

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel


class Remote:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def channel_down(self):
        self.device.set_channel(self.device.get_channel() - 1)

    def channel_up(self):
        self.device.set_channel(self.device.get_channel() + 1)

    def get_info(self):
        print(
            f"Device: {self.device.__class__.__name__}: {self.device.is_enabled()}, {self.device.get_volume()}, {self.device.get_channel()}"
        )


class AdvancedRemote(Remote):
    def mute(self):
        self.device.set_volume(0)


class ClientCode:
    def __init__(self, remote: Remote) -> None:
        self.remote = remote

    def some_operation(self) -> None:
        self.remote.toggle_power()
        self.remote.volume_down()
        self.remote.volume_up()
        self.remote.channel_down()
        self.remote.channel_up()
        self.remote.get_info()


if __name__ == "__main__":
    tv = Tv()
    remote = Remote(tv)
    client = ClientCode(remote)
    client.some_operation()
    print("\n")
    tv = TV()
    remote = AdvancedRemote(tv)
    client = ClientCode(remote)
    client.some_operation()
