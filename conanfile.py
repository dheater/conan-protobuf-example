import os
from conans import ConanFile, CMake, RunEnvironment, tools
import shutil



class TestProtobufConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_paths", "cmake_find_package", "cmake"
    requires="protobuf/3.11.4"

    def build(self):
        with tools.environment_append(RunEnvironment(self).vars):

            # Build with protoc
            cmake = CMake(self)
            cmake.definitions["protobuf_VERBOSE"] = True
            cmake.definitions["protobuf_MODULE_COMPATIBLE"] = True
            cmake.definitions["PROTOC_AVAILABLE"] = True
            cmake.build()

