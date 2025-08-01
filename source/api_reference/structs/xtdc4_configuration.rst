.. c:struct:: xtdc4_configuration

    This struct is used to configure an xTDC4 device using
    :c:func:`xtdc4_configure`.

    .. c:member:: int size

        The number of bytes this struct occupies.

    .. c:member:: int version

        Version number of this struct. It is increased when the definition of the
        struct changes.

    .. c:member:: int tdc_mode

        Operational mode of the TDC.

        Must be equal to the following:

        .. c:macro:: XTDC4_TDC_MODE_GROUPED

            Operate in grouped mode.

            Classical Common-Start operation. See also :ref:`sec grouping`.

    .. c:member:: crono_bool_t start_rising

        Selects whether the rising or falling edge of the start signal
        is used to start a group.

    .. c:member:: double dc_offset[XTDC4_TDC_CHANNEL_COUNT + 1]

        Set the threshold voltage for the input channels S, A–D.

        See also :numref:`fig-input-circuit`.

        - ``dc_offset[0]``: Threshold for channel Start.
        - ``dc_offset[1-4]``: Thresholds for Stop channels A–D.

        The supported range is –1.27 to 1.13 V.

        The threshold should be close to 50% of the height of the input pulse.

        The effective resolution is about :math:`\pm` 4 mV.

        .. note::

            The inputs are AC coupled. Thus, the absolute voltage is not important for
            pulse inputs. It is the relative pulse amplitude that causes the input
            circuit to switch. The parameter must be set to the relative switching
            voltage for the input standard in use.

            If the pulses are negative, a negative switching threshold must be set
            and vice versa.

        .. attention::

            The supported range changed for :ref:`driver release<sec driver revisions>`
            1.10.7. That means, if you use a value for ``dc_offset`` outside the new
            supported range in your source code, the device configuration will
            adjust it automatically to the new supported range (e.g., a value of
            1.18 V will be reduced to 1.13 V).

        Values for various signaling standards are provided as macros:

        .. c:macro:: XTDC4_DC_OFFSET_P_NIM

            DC offset is set to 0.35 V.

        .. c:macro:: XTDC4_DC_OFFSET_P_CMOS

            DC offset is set to 1.13 V.

        .. c:macro:: XTDC4_DC_OFFSET_P_LVCMOS_33

            DC offset is set to 1.13 V.

        .. c:macro:: XTDC4_DC_OFFSET_P_LVCMOS_25

            DC offset is set to 1.13 V.

        .. c:macro:: XTDC4_DC_OFFSET_P_LVCMOS_18

            DC offset is set to 0.90 V.

        .. c:macro:: XTDC4_DC_OFFSET_P_TTL

            DC offset is set to 1.13 V.

        .. c:macro:: XTDC4_DC_OFFSET_P_LVTTL_33

            DC offset is set to 1.13 V.

        .. c:macro:: XTDC4_DC_OFFSET_P_LVTTL_25

            DC offset is set to 1.13.

        .. c:macro:: XTDC4_DC_OFFSET_P_SSTL_3

            DC offset is set to 1.13 V.

        .. c:macro:: XTDC4_DC_OFFSET_P_SSTL_2

            DC offset is set to 1.13 V.

        .. c:macro:: XTDC4_DC_OFFSET_N_NIM

            DC offset is set to –0.35 V.

        .. c:macro:: XTDC4_DC_OFFSET_N_CMOS

            DC offset is set to –1.27 V.

        .. c:macro:: XTDC4_DC_OFFSET_N_LVCMOS_33

            DC offset is set to –1.27 V.

        .. c:macro:: XTDC4_DC_OFFSET_N_LVCMOS_25

            DC offset is set to –1.25 V.

        .. c:macro:: XTDC4_DC_OFFSET_N_LVCMOS_18

            DC offset is set to –0.90 V.

        .. c:macro:: XTDC4_DC_OFFSET_N_TTL

            DC offset is set to –1.27 V.

        .. c:macro:: XTDC4_DC_OFFSET_N_LVTTL_33

            DC offset is set to –1.27 V.

        .. c:macro:: XTDC4_DC_OFFSET_N_LVTTL_25

            DC offset is set to –1.25 V.

        .. c:macro:: XTDC4_DC_OFFSET_N_SSTL_3

            DC offset is set to –1.27 V.

        .. c:macro:: XTDC4_DC_OFFSET_N_SSTL_2

            DC offset is set to –1.25 V.


    .. c:member:: xtdc4_trigger trigger[XTDC4_TRIGGER_COUNT]

        Configuration of the polarity of the external trigger sources.

        External trigger sources are used as inputs for the TiGer blocks and as
        inputs to the time measurement unit.

        Index 0 refers to the Start channel, indices 1
        through 4 to the Stop channels A through D.

    .. c:member:: xtdc4_tiger_block tiger_block[XTDC4_TIGER_COUNT]

        Configuration of the :ref:`Timing Generators <sec tiger>`.

        Index 0 refers to the TiGer connected to the Start channel, indices 1
        through 4 to the TiGer-Units connected to the Stop channels A through D.

    .. c:member:: xtdc4_channel channel[XTDC4_TDC_CHANNEL_COUNT]

        Configuration of the Stop channels.

        Indices 0 through 3 refer to the Stop channels A through D.

    .. c:member:: xtdc4_lowres_channel lowres_channel[XTDC4_LOWRES_CHANNEL_COUNT]

        Configures additional digital low-res inputs.

        Only applicable to the xTDC4-S.

    .. c:member:: uint32_t auto_trigger_period

        Configure the base frequency of the
        :ref:`auto trigger function generator <sec auto trigger>`.

        See also :c:member:`auto_trigger_random_exponent`.

    .. c:member:: uint32_t auto_trigger_random_exponent

        Configure the randomness of the
        :ref:`auto trigger function generator <sec auto trigger>`.

        There is no enable or reset of the auto trigger.

        Given the two parameters :c:member:`auto_trigger_period` (*M*) and
        :c:member:`auto_trigger_random_exponent` (*N*), the frequency *T* of the
        auto trigger function generator will be

        .. math::

            T = M + [1 \dots 2^N] - 1

        with 6 ≤ *M* \< 2\ :sup:`32` and 0 ≤ *N* < 32.

        *M* and *N* are given in units of
        :c:member:`xtdc4_static_info.auto_trigger_ref_clock`.

    .. note::

        The auto trigger can be used as a source of the TiGer blocks
        (:c:member:`xtdc4_tiger_block.sources`).
