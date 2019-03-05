from conans import ConanFile, AutoToolsBuildEnvironment, tools


class MPIRConan(ConanFile):
    name = "mpir"
    version = "3.0.0-1"
    license = "LGPL"
    url = "http://mpir.org/"
    description = "highly optimised library for bignum arithmetic forked from the GMP bignum library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        tools.get("http://mpir.org/mpir-3.0.0.tar.bz2")

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir=self.source_folder +
                            "/mpir-3.0.0", args=["--enable-cxx", "--enable-gmpcompat"])
        autotools.make()
        autotools.install()

    def package(self):
        self.copy("*", src="package")

    def package_info(self):
        self.cpp_info.libs = ["mpir"]
