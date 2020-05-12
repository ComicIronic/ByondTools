==================
0.1.4 - 12/05/2020
==================

* Fixed use of deprecated & removed `clock()` function in the DMM library.

==================
0.1.3 - 19/11/2016
==================

* Fixed an issue with the script-copying helper not forming bangs correctly on Windows.

==================
0.1.2 - 19/11/2016
==================

* Modified get-dmi-data to output the PIL image's md5 instead of Python's default to-string behaviour.

==================
0.1.1 - 19/11/2016
==================

* Fixed issue with binary strings preventing dmi header extraction.
* Added single version value to setup.dmi for ease of use.

==================
0.1.0 - 18/11/2016
==================

* Split get-dmi-data into two utilities - old header extraction is now under get-dmi-header, and get-dmi-data now produces a generated header.

==================
0.0.1 - 18/11/2016
==================

* Started new fork of ByondTools with breaking changes planned.
* Changed DMI's get-dmi-data to write to stdout.
* Updated code to compile under Python 3 - functionality not tested.

=================
0.1.7 - 3/6/2015
=================

* Added pyparsing-based list() parser to DMM system
* DMMFix lives again!
* Move from print() to logging for console logging.
* Renamed ss13_makeinhands to dmi_compile, now uses a dmi_config.yml file.
* Fixed dmindent duplicating proc contents, cleaned out excessive newlines.

==================
0.1.6 - 12/24/2014
==================

* Fixed completely broken map rendering system.
* Repaired object tree generation
* Fixed color support

=================
0.1.5 - 6/18/2014
=================

* Emergency path fix for Linux

=================
0.1.4 - 6/18/2014
=================

* Added dmm diff and patch commands for patching maps.
* Added color name support to BYOND2RGBA.  Should fix rendering maps on TG/NT/Bay.
* Proper handling of nulls.

=================
0.1.3 - 6/17/2014
=================

* Fixed broken post-install operation on Linux (sorry)

