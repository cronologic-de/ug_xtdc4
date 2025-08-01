.. c:struct:: xtdc4_trigger

    Configure if rising or falling or both edges create a trigger event for
    :c:struct:`xtdc4_tiger_block`.

    Select which edge(s) trigger an event inside the FPGA.

    The xTDC4 can output measurements with a reduced bin size of
    5/6 ≈ 833.3 ps for one or both edges of the input signal.
    Use :c:member:`xtdc4_channel.rising` to select which edge is measured with
    full resolution.

    .. attention::

        The edge that is selected for full-resolution measurements
        must also be enabled for a low-resolution measurement, here.

    See :ref:`sec difficult hits` for more information on hits with varying
    resolution.

    .. c:member:: crono_bool_t falling

        Falling edges will trigger an event.

    .. c:member:: crono_bool_t rising

        Rising edges will trigger an event.
