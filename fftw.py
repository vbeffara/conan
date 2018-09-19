from conans import ConanFile, CMake, tools


class FftwConan(ConanFile):
    name = "fftw"
    version = "3.3.8"
    license = "GPL"
    url = "http://www.fftw.org/"
    description = "C subroutine library for computing the discrete Fourier transform"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        tools.download("http://fftw.org/fftw-3.3.8.tar.gz", "fftw.tar.gz")
        tools.untargz("fftw.tar.gz")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="fftw-3.3.8")
        cmake.build()

    def package(self):
        self.copy("fftw3*", dst="include", src="fftw-3.3.8/api")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["fftw3"]
