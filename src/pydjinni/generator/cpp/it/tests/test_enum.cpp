// Copyright 2023 jothepro
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "catch2/catch_test_macros.hpp"
#include "example_enum.hpp"
#include "helper.hpp"
#include <iostream>
#include <sstream>

TEST_CASE("Cpp.EnumTest") {
    GIVEN("a ExampleEnum enum value") {
        auto enum_value = test::enum_test::ExampleEnum::A;
        WHEN("passing the enum through a helper interface") {
            auto new_enum_value = test::enum_test::Helper::get_enum(enum_value);
            THEN("the enum should still be the same") {
                REQUIRE(new_enum_value == test::enum_test::ExampleEnum::A);
            }
        }
    }
    GIVEN("a ExampleEnum enum value") {
        auto enum_value = test::enum_test::ExampleEnum::A;
        WHEN("stringifying he enum value") {

            std::stringstream stringified;
            stringified << enum_value;
            THEN("the stringified value should be 'A'") {
                REQUIRE(stringified.str() == "A");
            }
        }
    }
}
