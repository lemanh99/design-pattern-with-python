from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass


class FileDataSource(DataSource):
    def __init__(self, filename):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    def write_data(self, data):
        print(f'Write data to file {self._filename} with {data}')

    def read_data(self):
        print(f'Read data from file {self._filename}')


class DataSourceDecorator(DataSource):
    _wrappee: DataSource = None

    def __init__(self, wrappee):
        self._wrappee = wrappee

    @property
    def wrappee(self) -> DataSource:
        return self._wrappee

    def write_data(self, data):
        self._wrappee.write_data(data)

    def read_data(self):
        self._wrappee.read_data()


class EncryptionDecorator(DataSourceDecorator):
    def write_data(self, data):
        print(f'Encrypt data')
        self.wrappee.write_data(data)

    def read_data(self):
        print(f'Decrypt data')
        self.wrappee.read_data()


class CompressionDecorator(DataSourceDecorator):
    def write_data(self, data):
        print(f'Compress data')
        self.wrappee.write_data(data)

    def read_data(self):
        print(f'Decompress data')
        self.wrappee.read_data()


class ClientCode:
    def __init__(self, component: DataSource):
        self.component = component

    def execute(self):
        print("Executing ClientCode:")
        self.component.write_data('data')


if __name__ == "__main__":
    component = FileDataSource('filename')
    decorator = EncryptionDecorator(component)
    client = ClientCode(decorator)
    client.execute()
