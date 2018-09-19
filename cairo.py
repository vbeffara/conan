from conans import ConanFile, AutoToolsBuildEnvironment, tools


class CairoConan(ConanFile):
    name = "cairo"
    version = "1.14.12"
    license = "LGPL/MPL"
    url = "https://cairographics.org/"
    description = "2D graphics library with support for multiple output devices"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        tools.get("https://cairographics.org/releases/cairo-1.14.12.tar.xz")

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir=self.source_folder+"/cairo-1.14.12")
        autotools.make()
        autotools.install()

    def package(self):
        self.copy("*", src="package")

    def package_info(self):
        self.cpp_info.libs = ["cairo"]
