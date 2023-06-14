cmake_minimum_required(VERSION 3.6.0)

project(PyDjinniCommonSupportLib C CXX)

add_library(common_support_lib INTERFACE)

target_include_directories(common_support_lib INTERFACE include)
target_compile_features(common_support_lib INTERFACE cxx_std_20)

add_library(support_lib::common ALIAS common_support_lib)

if(BUILD_TESTING)
    add_executable(common_support_lib_tests
        tests/test.cpp
        tests/test2.cpp
    )

    target_link_libraries(common_support_lib_tests
        PRIVATE
            support_lib::common
            Catch2::Catch2WithMain
    )

    catch_discover_tests(common_support_lib_tests)
endif()