project(lr-proto)
cmake_minimum_required(VERSION 3.16)
set(CMAKE_CXX_STANDARD 17)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include(${CMAKE_CURRENT_BINARY_DIR}/conan_paths.cmake)
find_package(Protobuf REQUIRED)

add_library(
        ${PROJECT_NAME}
        hostinput.proto
        userinput.proto
)

protobuf_generate_cpp(
        PROTO_SRCS PROTO_HDRS
        TARGET
        ${PROJECT_NAME}
)
