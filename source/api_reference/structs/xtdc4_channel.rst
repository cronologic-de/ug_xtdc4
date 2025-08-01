.. c:struct:: xtdc4_channel

    .. c:member:: crono_bool_t enabled

        Enable the TDC channel.

    .. c:member:: crono_bool_t rising

        Select which edge of the signal is used for full-resolution measurements.

        For selecting a signal edge for low-resolution measurements,
        :c:member:`xtdc4_trigger.rising` and :c:member:`xtdc4_trigger.falling`
        are used.

        .. attention::

            The edge that is select for full-resolution measurements here must also
            be selected for low-resolution measurements.

        See :ref:`sec difficult hits` for more information on hits with varying
        resolution.

    .. c:member:: crono_bool_t cc_enable

        Enable Delay-Line TDC.

        This is set to *true* by default and should be left unchanged.

    .. c:member:: crono_bool_t cc_same_edge

        Sets whether the Delay-Line TDC records the same or the opposite edge
        as the full-resolution TDC chip.

        If the same edge is selected, the Delay-Line TDC acts as a backup if
        the full-resolution TDC chip misses hits due to FIFO overflows or short
        input pulses.

        If opposite edges are selected, both edges of a pulse can be measured with
        reasonable resolution.

        See :ref:`sec difficult hits` for more information on hits with varying
        resolution.

    .. c:member:: crono_bool_t ths788_disable

        Disable full-resolution timestamps.

        This is set to *false* by default and should be left unchanged.


    .. c:member:: uint32_t start

        Start value for the grouping functionality.

        In multiples of :c:member:`xtdc4_param_info.binsize`.

        See also :c:member:`stop` and :ref:`sec grouping`.

    .. c:member:: uint32_t stop

        Stop value for the grouping functionality.

        In multiples of :c:member:`xtdc4_param_info.binsize`.

        Only hits between :c:member:`start` and :c:member:`stop` are read out.

        The range is 0 ≤ :c:member:`start` ≤ :c:member:`stop` < 2\ :sup:`30`.

        See also :ref:`sec grouping`.
