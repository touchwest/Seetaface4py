#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SeetaNet" for configuration ""
set_property(TARGET SeetaNet APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(SeetaNet PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NOCONFIG "-lpthread"
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libSeetaNet.so.v2.5.5"
  IMPORTED_SONAME_NOCONFIG "libSeetaNet.so.v2.5.5"
  )

list(APPEND _IMPORT_CHECK_TARGETS SeetaNet )
list(APPEND _IMPORT_CHECK_FILES_FOR_SeetaNet "${_IMPORT_PREFIX}/lib/libSeetaNet.so.v2.5.5" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
