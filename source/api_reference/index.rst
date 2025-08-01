=============
API Reference
=============

The API is a DLL with C linkage.

The functions provided by the driver are declared in ``xTDC4_interface.h``
which must be included by your source code. You must tell your compiler to link with
the file ``xTDC4_driver_64.lib``.

When running your program, the dynamic link library containing the 
actual driver code must reside in the same directory as your executable or be in a 
directory included in the PATH variable. For Linux, it is provided only as a static 
library ``libxtdc4_driver.a``. The file for the DLL is called ``xTDC4_driver_64.dll``. 
All these files are provided with the driver installer that can be downloaded from the 
product website at `www.cronologic.de <https://www.cronologic.de>`_.

By default, the installer will place the files into 
the directory ``C:\Program Files\cronologic\xTDC4\driver``.

**Setting up and using an xTDC4**

Setting up and using a xTDC4 in your application software requires that you:

- Initialize an xTDC4 device (see :ref:`sec initialization`).
- Configure the initialized xTDC4 device (see :ref:`sec configuration`).
- Start data acquisition (see :ref:`sec runtime control`).
- Read data from the device (see :ref:`sec readout`).
- Process the data provided as packets (see :ref:`sec data format`).


.. raw:: html

    <h2>Contents</h2>

.. toctree::
    :maxdepth: 2

    constants
    initialization
    configuration
    runtime_control
    readout
    data_format
    status_information
    driver_information
