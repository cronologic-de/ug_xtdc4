.. raw:: latex

    \clearpage

:tocdepth: 3

==================
Status Information
==================

The driver provides functions to retrieve detailed information on the board type,
its configuration, settings, and state. The information is split according to
its scope and the computational requirements to query the information from the board.



.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_get\_device\_type}

.. c:function:: int xtdc4_get_device_type(xtdc4_device *device)

    Get the type of the TimeTagger device.

    :param device: Pointer to an xTDC4 device.
    :return: :c:macro:`CRONO_DEVICE_XTDC4`




.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_get\_last\_error\_message}

.. c:function:: const char* xtdc4_get_last_error_message(\
    xtdc4_device *device)

    Get the last error message.

    :param device: Pointer to an xTDC4 device.
    :return: The error message.




.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_get\_fast\_info}

.. c:function:: int xtdc4_get_fast_info(\
    xtdc4_device *device,\
    xtdc4_fast_info *info)

    Obtain dynamic information about a xTDC4 device that can be obtained
    within a few microseconds.

    :param device: Pointer to an xTDC4 device.
    :param info: Pointer to a :c:struct:`xtdc4_fast_info` struct that
        will be filled.
    :return: Status codes:
        :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`,
        :c:macro:`XTDC4_CRONO_INVALID_ARGUMENTS`, or
        ``-1``.




.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_get\_param\_info}

.. c:function:: int xtdc4_get_param_info(\
    xtdc4_device *device,\
    xtdc4_fast_info *info)

    Obtain information about configuration changes.

    Gets information that changes indirectly due to configuration changes.

    :param device: Pointer to an xTDC4 device.
    :param info: Pointer to a :c:struct:`xtdc4_param_info` struct that
        will be filled.
    :return: Status codes:
        :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_CRONO_INVALID_ARGUMENTS`, or
        :c:macro:`XTDC4_WRONG_STATE`,





.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_get\_static\_info}

.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_get\_param\_info}

.. c:function:: int xtdc4_get_static_info(\
    xtdc4_device *device,\
    xtdc4_static_info *info)

    Obtain information about an xTDC4 device that does not change during runtime.

    :param device: Pointer to an xTDC4 device.
    :param info: Pointer to an :c:struct:`xtdc4_static_info` struct that
        will be filled.
    :return: Status codes:
        :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`, or
        :c:macro:`XTDC4_CRONO_INVALID_ARGUMENTS`.





.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_get\_pcie\_info}
    
.. c:function:: int xtdc4_get_pcie_info(\
    xtdc4_device *device,\
    crono_pcie_info *pcie_info)

    Obtain PCIe information.

    :param device: Pointer to an xTDC4 device.
    :param pcie_info: Pointer to a :c:struct:`crono_pcie_info` struct that
        will be filled.
    :return: Status codes:
        :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`, or
        :c:macro:`XTDC4_HARDWARE_FAILURE`.




.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_clear\_pcie\_errors}

.. c:function:: int xtdc4_clear_pcie_errors(\
    xtdc4_device *device,\
    int flags)

    Clear PCIe errors.

    Only useful for PCIe debugging.

    Valid ``flags`` are:

    .. c:macro:: CRONO_PCIE_CORRECTABLE_FLAG

        Clear correctable PCIe errors.

    .. c:macro:: CRONO_PCIE_UNCORRECTABLE_FLAG

        Clear uncorrectable PCIe errors.

    :param device: Pointer to an xTDC4 device.
    :param flag: Flag which errors to clear.
    :return: Status codes:
        :c:macro:`XTDC4_OK`, or
        :c:macro:`XTDC4_INVALID_DEVICE`.




.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_fast\_info}

.. include:: structs/xtdc4_fast_info.rst




.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_param\_info}

.. include:: structs/xtdc4_param_info.rst
    



.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_static\_info}

.. include:: structs/xtdc4_static_info.rst




.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{crono\_pcie\_info}

.. include:: structs/crono_pcie_info.rst