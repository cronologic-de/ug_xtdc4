================
Revision History
================

Firmware
========

Gen 1
-----

2.1218 – 2024-07-12
    - PCIe interface optimizations
    - Fixed first-level FIFO overflow
    - Fixed rare bug causing PC freeze

2.1192 – 2023-06-14
    - Fixed bug related to packet polarity

2.1134 – 2021-12-10
    - Fixed TDC over-temperature alarm issue

2.1126 – 2021-12-06
    - Fixed possible register read issue

2.1117 – 2021-06-23
    - Fixed register write issue

2.834 – 2017-12-05
    - Internal optimizations

2.797 – 2015-09-08
    - Fixed hit sorting and packet generation issues

Gen 2
-----

2.24192 – 2024-07-10
    - Fixed erroneous packet for very high trigger rates

2.24117 – 2024-04-26
    - Fixed bug related to PCIe readout

2.23060 – 2023-03-01
    - Fixed bug related to packet polarity

2.22341 – 2022-12-07
    - Minor bug fixes

2.22327 – 2022-11-18
    - Support for board revision 7


.. _sec driver revisions:

Driver & Applications
=====================
1.12.1 – 2025-07-17
    - Added support for kernel mode driver 1.5.2
    - Improved error handling

1.10.7 – 2024-07-25
    - Support for TimeTagger4-10G (incl. calibration tool)
    - Include baseline calibration
    - Reduced supported range of dc_offset by 100 mV

1.9.0 – 2023-07-10
    - Added quantization to timetagger4_param_info structure
    - Code refactorization

1.8.3 – 2023-06-07
    - Minor bug fixes
    - Code refactorization

1.8.2 – 2023-05-17
    - Added bounds and checks for various parameters

1.8.1 – 2023-05-09
    - Renamed autotrigger mode to continuous mode

1.8.0 – 2023-05-05
    - Added configurable input delay

1.7.0 – 2023-04-18
    - Board Revision 7 support
    - TimeTagger4: added autotrigger mode

1.4.5 – 2022-10-17
    - Kernel driver v1.4.2 for xTDC4 only (fixes crash on Windows for Thunderbolt hot-plug)

1.4.4 – 2022-06-27
    - Kernel driver v1.4.1

1.4.2 – 2021-07-28
    - Firmware updated
    - ReadoutGUI added/updated
    - User guide example added/updated

1.4.1 – 2019-11-11
    - x64 32 mode issues fixed

1.4.0 – 2019-06-04
    - Improved Windows 10 support

1.3.0 – 2019-01-23
    - Added Windows 10 support

User Guide
==========

2.0.1-dev – TBD
    - Various clarifications in API

2.0.0 – 2025-08-01
    - Initial Release of the HTML User Guide
    - Separated xHPTDC8, xTDC4, and TimeTagger4 User Guides

1.10.7 – 2025-07-12
    - xTDC4 and TimeTagger4: Documented driver release 1.12.1

1.10.6 – 2025-06-10
    - xTDC4 and TimeTagger4: Updated Figure 3.2
    - Removed references to J6 connector

1.10.5 – 2025-04-23
    - TimeTagger4 and xTDC4: Fixed code examples
    - Documented minimal pulse height

1.10.4 – 2025-03-20
    - TimeTagger4: Updated Table 8.2.2

1.10.3 – 2025-03-18
    - xHPTDC8: Documented Firmware 2.1225 and Driver 1.5.0

1.10.2 – 2024-12-17
    - xHPTDC8: Updated Figure 2.3
    - xTDC4: Fixed formatting

1.10.1 – 2024-09-19
    - xHPTDC8: Fixes and additions to introduction
    - xHPTDC8 and TimeTagger4: Documented max. readout rate for single channels
    - Updated Figure 2.4
1.10.0 – 2024-08-14
    - TimeTagger4: Renamed 10G calibration tool
    - Added Section "Memory Layout"

1.9.4 – 2024-07-30
    - Updated driver and firmware revision lists
    - xHPTDC8: Updated user guide example.cpp

1.9.3 – 2024-07-16
    - xHPTDC8: Fix driver revision list

1.9.2 – 2024-07-09
    - xHPTDC8: Added LED documentation
    - TimeTagger4 and xTDC4: Add overview figure of TBT and PCIe variant
    - Fixed grammar

1.9.1 – 2024-07-02
    - xHPTDC8: Updated firmware list

1.9.0 – 2024-06-27
    - Added new driver revision
    - TimeTagger4 and xTDC4: Added TBT variant
    - TimeTagger4 and xTDC4: Added ordering information
    - TimeTagger4 and xTDC4: Updated supported range for dc_offset

1.8.17 – 2024-06-20
    - xTDC4: Fixed API documentation

1.8.16 – 2024-06-20
    - TimeTagger4: Added documentation for 10G calibration tool
    - xTDC4 and TimeTagger4: Added LED documentation
    - xHPTDC8: Fixed default values for zero_channel
    - Clarifications for TiGer block indices

1.8.15 – 2024-05-08
    - Fixed auto_trigger formula
    - Updated oscillator characteristics
    - xHPTDC8: Fixed mistakes in API
    - xHPTDC8: Updated Code Examples

1.8.14 – 2024-03-27
    - Updated API
    - Updated information on power consumption
    - xHPTDC8: Extended chapter on gating

1.8.13 – 2024-01-18
    - xHPTDC8: Updated cover
    - TimeTagger4: Updated feature list

1.8.12 – 2024-01-10
    - xHPTDC8: Updated driver revision history

1.8.11 – 2023-11-29
    - Reformatting
    - Added latency between signal and Tiger output to Section 3.5
    - TimeTagger4: Updated table in Section 8.1.2
    - TimeTagger4: Clarifications in Features-list
    - TimeTagger4: Added ignore_empty_packets API documentation
    - xHPTDC8: Added default values for manager and configuration structs
    - xHPTDC8: Fixed number of boards that can be synchronized from 8 to 6

1.8.10 – 2023-07-28
    - Changed extended range values to 0.429s and 2.147s, respectively.
    - API clarifications.

1.8.9 – 2023-07-10
    - TimeTagger4 User Guide rework

1.8.8 – 2023-03-15
    - New TimeTagger4 variants -1.25G to -10G added

1.8.7 – 2022-11-24
    - Firmware revision notes updated

1.8.6 – 2022-11-23
    - Spelling and grammar corrections
    - New example source code for xHPTDC8

1.8.5 – 2021-12-17
    - Clarifications related to TimeTagger4 configuration.

1.8.4 – 2021-12-08
    - Updated grouping structure in xHPTDC8 API

1.8.3 – 2021-07-28
    - Updated firmware revision history

1.8.2 – 2021-04-23
    - Added software trigger and _SYNC trigger sources for xHPTDC8
    - Corrected 3.3V power requirement for xHPTDC8
    - Changed types with fixed bit width to stdint.h for xHPTDC8
    - Added user flash functions for xHPTDC8

1.8.1 – 2021-04-09
    - Many corrections and updates to the xHPTDC8 API

1.8.0 – 2021-03-22
    - Added xHPTDC8 User Guide

1.7.0 – 2021-02-04
    - Combined User Guide for -1G and -2G
    - Added characteristics for INL, DNL and Time Base
    - Reordered sections for clarity
    - Error corrections for rollovers, binsize and range
    - Added figure 3.2 (TiGer matrix)
    - Corrected board revision

1.3.0 – 2019-06-05
    - API clarifications