# Subsystems
class VideoFile:
    def __init__(self, filename):
        self.filename = filename

class Codec:
    def decode(self, file):
        print(f"Decoding {file.filename}...")

class Converter:
    def convert(self, file, format):
        print(f"Converting {file.filename} to {format} format...")

class Exporter:
    def export(self, file, format):
        print(f"Exporting {file.filename} as .{format} file")

# Facade
class VideoConverterFacade:
    def convert(self, filename, target_format):
        file = VideoFile(filename)
        codec = Codec()
        converter = Converter()
        exporter = Exporter()

        codec.decode(file)
        converter.convert(file, target_format)
        exporter.export(file, target_format)
    
def main():
    converter = VideoConverterFacade()
    converter.convert("output.mp4","mkv")

main()