from conans import ConanFile


class PngConan(ConanFile):
    name = "sqlite_modern_cpp"
    version = "3.2-HEAD"
    license = "MIT"
    url = "https://github.com/SqliteModernCpp/sqlite_modern_cpp"
    description = "C++14 wrapper around sqlite library"
    generators = "cmake"
    requires = "sqlite3/3.21.0@bincrafters/stable"

    def source(self):
        self.run("git clone https://github.com/SqliteModernCpp/sqlite_modern_cpp.git")

    def build(self):
        pass

    def package(self):
        self.copy("*.h", src="sqlite_modern_cpp/hdr",
                  dst="include", keep_path=True)
