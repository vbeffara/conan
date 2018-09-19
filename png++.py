from conans import ConanFile, CMake, tools


class PngConan(ConanFile):
    name = "png++"
    version = "0.2.5"
    license = "BSD"
    url = "https://www.nongnu.org/pngpp/"
    description = "A C++ wrapper for the libpng library"
    generators = "cmake"
    requires = "libpng/1.6.34@bincrafters/stable"

    def source(self):
        tools.get(
            "http://download.savannah.nongnu.org/releases/pngpp/png++-0.2.5.tar.gz")

    def build(self):
        pass

    def package(self):
        self.copy("*.hpp", dst="include/png++", keep_path=False)
