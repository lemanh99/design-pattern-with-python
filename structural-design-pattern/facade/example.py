class File:
    def __init__(self, file):
        self.filename = file


class VideoFile:
    def __init__(self, filename):
        self.filename = filename


class OggCompressionCodec:
    pass


class MPEG4CompressionCodec:
    pass


class CodecFactory:

    @staticmethod
    def extract(file):
        pass


class BitrateReader:
    @staticmethod
    def read(filename, source_codec):
        pass

    @staticmethod
    def convert(buffer, destination_codec):
        pass


class AudioMixer:
    @staticmethod
    def fix(result):
        pass


class VideoConverter:
    def convert(self, filename, format):
        file = VideoFile(filename)
        source_codec = CodecFactory.extract(file)

        if format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)
        result = (AudioMixer().fix(result))
        return File(result)
