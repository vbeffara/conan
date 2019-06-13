from conans import ConanFile, AutoToolsBuildEnvironment, tools


class HpxConan(ConanFile):
    name = "hwloc"
    version = "2.0.3-1"
    license = "BSD"
    author = "Vincent Beffara <vbeffara@gmail.com>"
    url = "https://github.com/vbeffara/conan"
    description = "portable abstraction of the hierarchical topology of modern architectures"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        tools.get(
            "https://download.open-mpi.org/release/hwloc/v2.0/hwloc-2.0.3.tar.gz")

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir=self.source_folder+"/hwloc-2.0.3")
        autotools.make()
        autotools.install()

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hwloc"]
