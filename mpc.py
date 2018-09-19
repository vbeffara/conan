from conans import ConanFile, AutoToolsBuildEnvironment, tools


class CairoConan(ConanFile):
    name = "mpc"
    version = "1.1.0"
    license = "LGPL"
    url = "http://www.multiprecision.org/mpc/"
    description = "C library for the arithmetic of complex numbers with arbitrarily high precision"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    requires = "mpfr/4.0.1@vbeffara/testing"

    def source(self):
        tools.get("https://ftp.gnu.org/gnu/mpc/mpc-1.1.0.tar.gz")

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir=self.source_folder+"/mpc-1.1.0")
        autotools.make()
        autotools.install()

    def package(self):
        self.copy("*", src="package")

    def package_info(self):
        self.cpp_info.libs = ["mpc"]
