cmake_minimum_required(VERSION 3.5)
project(lab1_pkg_new)

# Find Python
find_package(Python 3 REQUIRED)

# Find Python modules and extensions
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Install Python executables
install(PROGRAMS talker.py
  DESTINATION lib/${PROJECT_NAME}
)

# Build and install ament index
ament_export_dependencies(ament_cmake)
ament_export_dependencies(rclpy)
ament_export_dependencies(Python)


ament_package()

