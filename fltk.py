from conans import ConanFile, CMake, tools


class FltkConan(ConanFile):
    name = "fltk"
    version = "1.3.4"
    license = "LGPL"
    url = "http://www.fltk.org/"
    description = "FLTK is a cross-platform C++ GUI toolkit"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        tools.get("http://fltk.org/pub/fltk/1.3.4/fltk-1.3.4-2-source.tar.gz")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["OPTION_BUILD_SHARED_LIBS"] = "ON"
        if self.settings.os == "Linux":
            cmake.definitions["CMAKE_C_FLAGS"] = "-fPIC"
            cmake.definitions["CMAKE_CXX_FLAGS"] = "-fPIC"
        cmake.configure(source_folder="fltk-1.3.4-2", )
        cmake.build()

    def package(self):
        self.copy("FL/*", dst="include", src="fltk-1.3.4-2")
        self.copy("*abi-version.h", dst="include/FL", keep_path=False)
        self.copy("*fltk.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*fluid", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["fltk_SHARED", "fltk_gl_SHARED"]
        if self.settings.os == "Macos":
            self.cpp_info.sharedlinkflags = [
                "-framework", "OpenGL", "-framework", "Cocoa"]
            self.cpp_info.exelinkflags = [
                "-framework", "OpenGL", "-framework", "Cocoa"]
