import os
class compression_ratio:
    sizeBeforeCompression=0
    sizeAfterCompression=0

    def getSizeBeforeCompression(self,path):
        return os.stat(path).st_size

    def getSizeAfterCompression(self,encoder):
        return encoder.compressed_chars_count

    def getCompressionRatio(self,path,encoder):
        self.sizeBeforeCompression=self.getSizeBeforeCompression(path)
        self.sizeAfterCompression=self.getSizeAfterCompression(encoder)
        ratio=self.sizeBeforeCompression/self.sizeAfterCompression
        return ratio