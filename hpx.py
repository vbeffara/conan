from conans import ConanFile, CMake, tools

# TODO: depend on jemalloc/tcmalloc


class HpxConan(ConanFile):
    name = "hpx"
    version = "1.3.0-1"
    license = "Boost Software License - Version 1.0"
    author = "Vincent Beffara <vbeffara@gmail.com>"
    url = "https://github.com/vbeffara/conan"
    description = "a C++ Standard Library for Concurrency and Parallelism"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    requires = "hwloc/2.0.3-1@vbeffara/testing", "boost/1.70.0@conan/stable"
    # "jemalloc/5.2.0-1@vbeffara/testing"

    def source(self):
        tools.get("http://stellar.cct.lsu.edu/files/hpx_1.3.0.tar.gz")
        tools.replace_in_file("hpx_1.3.0/CMakeLists.txt", "project(HPX CXX C)",
                              "project(HPX CXX C) \ninclude(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) \nconan_basic_setup(KEEP_RPATHS)")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="hpx_1.3.0")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder="hpx_1.3.0")
        cmake.install()

    def package_info(self):
        pass
