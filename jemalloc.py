from conans import ConanFile, AutoToolsBuildEnvironment, tools

# TODO: depend on jemalloc/tcmalloc


class HpxConan(ConanFile):
    name = "jemalloc"
    version = "5.2.0-1"
    license = "BSD-like"
    author = "Vincent Beffara <vbeffara@gmail.com>"
    url = "https://github.com/vbeffara/conan"
    description = "a general purpose malloc implementation"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        tools.get(
            "https://github.com/jemalloc/jemalloc/releases/download/5.2.0/jemalloc-5.2.0.tar.bz2")

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir=self.source_folder+"/jemalloc-5.2.0")
        autotools.make()

    def package(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir=self.source_folder+"/jemalloc-5.2.0")
        autotools.install()

    def package_info(self):
        self.cpp_info.libs = ["jemalloc"]
