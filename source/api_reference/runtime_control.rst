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




.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_start\_capture}

.. c:function:: int xtdc4_start_capture(xtdc4_device *device)

    Start data acquisition.

    :param device: Pointer to an xTDC4 device.
    :returns: Status code:
        :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`,
        :c:macro:`XTDC4_CRONO_INTERNAL_ERROR`,
        :c:macro:`XTDC4_HARDWARE_FAILURE`, or
        :c:macro:`XTDC4_WRONG_STATE`.





.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_pause\_capture}

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





.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_continue\_capture}

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





.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_stop\_capture}

.. c:function:: int xtdc4_stop_capture(xtdc4_device *device)

    Stop data acquisition.

    :param device: Pointer to an xTDC4 device.
    :returns: Status code:
        :c:macro:`XTDC4_OK`, or
        :c:macro:`XTDC4_INVALID_DEVICE`.





.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_start\_tiger}

.. c:function:: int xtdc4_start_tiger(xtdc4_device *device)

    Start the :ref:`Timing Generator (TiGer) <sec tiger>`

    This can be done independently of the state of the data acquisition.

    :param device: Pointer to an xTDC4 device.
    :return: Status code:
        :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`, or
        :c:macro:`XTDC4_WRONG_STATE`.





.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsection}{xtdc4\_stop\_tiger}

.. c:function:: int xtdc4_stop_tiger(xtdc4_device *device)

    Stop the :ref:`Timing Generator (TiGer) <sec tiger>`

    This can be done independently of the state of the data acquisition.

    :param device: Pointer to an xTDC4 device.
    :return: Status code:
        :c:macro:`XTDC4_OK` or
        :c:macro:`XTDC4_INVALID_DEVICE`.