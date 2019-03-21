from conans import ConanFile, CMake, tools


class FltkConan(ConanFile):
    name = "fltk"
    version = "1.3.5-1"
    license = "LGPL"
    url = "http://www.fltk.org/"
    description = "FLTK is a cross-platform C++ GUI toolkit"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "libjpeg/9c@bincrafters/stable", "libpng/1.6.36@bincrafters/stable"

    def source(self):
        self.run(
            "git clone --branch release-1.3.5 --depth 1 http://github.com/fltk/fltk.git")
        self.run("rm fltk/VERSION")
        tools.replace_in_file("fltk/CMakeLists.txt", "project(FLTK)",
                              "project(FLTK) \ninclude(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) \nconan_basic_setup(KEEP_RPATHS)")

    def build(self):
        cmake = CMake(self)
        if self.settings.os == "Linux":
            cmake.definitions["CMAKE_C_FLAGS"] = "-fPIC"
            cmake.definitions["CMAKE_CXX_FLAGS"] = "-fPIC"
        cmake.configure(source_folder="fltk", )
        cmake.build()

    def package(self):
        self.copy("FL/*", dst="include", src="fltk")
        self.copy("*abi-version.h", dst="include/FL", keep_path=False)
        self.copy("*fltk.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*fluid", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["fltk", "fltk_gl"]
        if self.settings.os == "Macos":
            self.cpp_info.sharedlinkflags = [
                "-framework", "OpenGL", "-framework", "Cocoa"]
            self.cpp_info.exelinkflags = [
                "-framework", "OpenGL", "-framework", "Cocoa"]
        if self.settings.os == "Linux":
            self.cpp_info.libs += ["GLU", "GL", "X11", "Xext", "pthread", "Xinerama",
                                   "Xfixes", "Xcursor", "Xft", "Xrender", "m", "fontconfig", "dl"]
