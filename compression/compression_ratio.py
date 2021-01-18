import os


class compression_ratio:
    size_before_compression = 0
    size_after_compression = 0

    def get_size_before_compression(self, path):
        print(os.stat(path).st_size)
        return os.stat(path).st_size

    def get_size_after_compression(self, encoder):
        print(encoder.compressed_chars_count)
        return encoder.compressed_chars_count

    def getCompressionRatio(self, path, encoder):
        self.size_before_compression = self.get_size_before_compression(path)
        self.size_after_compression = self.get_size_after_compression(encoder)
        ratio = self.size_before_compression / self.size_after_compression
        return ratio
