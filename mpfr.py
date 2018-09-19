from conans import ConanFile, AutoToolsBuildEnvironment, tools


class CairoConan(ConanFile):
    name = "mpfr"
    version = "4.0.1"
    license = "LGPL"
    url = "https://www.mpfr.org/"
    description = "C library for multiple-precision floating-point computations with correct rounding"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        tools.get("https://www.mpfr.org/mpfr-current/mpfr-4.0.1.tar.xz")

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir=self.source_folder+"/mpfr-4.0.1")
        autotools.make()
        autotools.install()

    def package(self):
        self.copy("*", src="package")

    def package_info(self):
        self.cpp_info.libs = ["mpfr"]
