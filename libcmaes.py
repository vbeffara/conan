from conans import ConanFile, CMake, tools


class LibcmaesConan(ConanFile):
    name = "libcmaes"
    version = "0.9.5-HEAD"
    license = "LGPL3"
    url = "http://github.com/beniz/libcmaes"
    description = "libcmaes is a multithreaded C++11 implementation of algorithms of the CMA-ES family"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    requires = "eigen/3.3.5@conan/stable"

    def source(self):
        self.run("git clone http://github.com/beniz/libcmaes.git")
        tools.replace_in_file("libcmaes/CMakeLists.txt", "project (libcmaes)",
                              "project (libcmaes) \ninclude(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) \nconan_basic_setup(KEEP_RPATHS)")
        tools.replace_in_file("libcmaes/src/CMakeLists.txt",
                              "target_compile_features", "#")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="libcmaes")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="libcmaes/src")
        self.copy("libcmaes_config.h", dst="include")
        self.copy("cmaes_export.h", src="src", dst="include")
        self.copy("*.hpp", dst="include", src="libcmaes/src")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["cmaes"]
