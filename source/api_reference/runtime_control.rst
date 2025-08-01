.. raw:: latex

    \clearpage

.. _sec runtime control:

===============
Runtime Control
===============

Once an xTDC4 device is configured, the following functions can be used to control
the behavior of it.

These functions return quickly with very little overhead. However, they are not
guaranteed to be thread safe. 

xtdc4_start_capture
=========================

.. c:function:: int xtdc4_start_capture(xtdc4_device *device)

    Start data acquisition.

    :param device: Pointer to an xTDC4 device.
    :returns: Status code:
        :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`,
        :c:macro:`XTDC4_CRONO_INTERNAL_ERROR`,
        :c:macro:`XTDC4_HARDWARE_FAILURE`, or
        :c:macro:`XTDC4_WRONG_STATE`.


xtdc4_pause_capture
=========================

.. c:function:: int xtdc4_pause_capture(xtdc4_device *device)

    Pause data acquisition.

    :c:func:`xtdc4_pause_capture` and :c:func:`xtdc4_continue_capture`
    have less overhead than :c:func:`xtdc4_start_capture` and
    :c:func:`xtdc4_stop_capture`, but do not allow for a
    configuration change.

    :param device: Pointer to an xTDC4 device.
    :returns: Status code:
        :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`,
        :c:macro:`XTDC4_WRONG_STATE`.


xtdc4_continue_capture
============================

.. c:function:: int xtdc4_continue_capture(xtdc4_device *device)

    Continue data acquisition.

    :c:func:`xtdc4_pause_capture` and :c:func:`xtdc4_continue_capture`
    have less overhead than :c:func:`xtdc4_start_capture` and
    :c:func:`xtdc4_stop_capture`, but do not allow for a
    configuration change.

    :param device: Pointer to an xTDC4 device.
    :return: Status code:
        :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`,
        :c:macro:`XTDC4_WRONG_STATE`.


xtdc4_stop_capture
=========================

.. c:function:: int xtdc4_stop_capture(xtdc4_device *device)

    Stop data acquisition.

    :param device: Pointer to an xTDC4 device.
    :returns: Status code:
        :c:macro:`XTDC4_OK`, or
        :c:macro:`XTDC4_INVALID_DEVICE`.


xtdc4_start_tiger
=======================

.. c:function:: int xtdc4_start_tiger(xtdc4_device *device)

    Start the :ref:`Timing Generator (TiGer) <sec tiger>`

    This can be done independently of the state of the data acquisition.

    :param device: Pointer to an xTDC4 device.
    :return: Status code:
        :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`, or
        :c:macro:`XTDC4_WRONG_STATE`.


xtdc4_stop_tiger
=======================

.. c:function:: int xtdc4_stop_tiger(xtdc4_device *device)

    Stop the :ref:`Timing Generator (TiGer) <sec tiger>`

    This can be done independently of the state of the data acquisition.

    :param device: Pointer to an xTDC4 device.
    :return: Status code:
        :c:macro:`XTDC4_OK` or
        :c:macro:`XTDC4_INVALID_DEVICE`.