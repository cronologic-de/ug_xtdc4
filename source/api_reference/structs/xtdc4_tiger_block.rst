
.. c:struct:: xtdc4_tiger_block

    This struct configures the Timing Generators
    [see also :ref:`sec tiger`].

    .. c:member:: crono_bool_t enable

        Activates the TiGer.

        .. note::

            To use a TiGer, make sure to also set :c:member:`enable_lemo_output` to
            true.

    .. c:member:: crono_bool_t negate

        Inverts the output polarity.

        Default is false.

    .. c:member:: crono_bool_t retrigger

        Enables re-triggering.

        If re-triggering is enabled, the following applies:
        After an event triggered the TiGer output, another event that is detected
        before the :c:member:`stop` value is reached will extend the TiGer output
        for a time :c:member:`stop` minus :c:member:`start`.

    .. c:member:: crono_bool_t extend

        Not applicable for the xTDC4.

    .. c:member:: crono_bool_t enable_lemo_output

        Enables the LEMO output.

        Drive the TiGer signal to the corresponding LEMO connector as an output.

        Pulses created by the TiGer are visible at the corresponding input and can
        be used to get their exact timing.

        .. attention::

            The output is DC coupled. Make sure to not connect any devices to
            the corresponding input, as this may damage the device or the xTDC4.

    .. c:member:: uint_32_t start

        Configure the duration when the TiGer output is enabled
        relative to the trigger.

        See also :c:member:`stop`.

    .. c:member:: uint_32_t stop

        Configure the duration when the TiGer output is enabled
        relative to the trigger.

        In multiplies of 20 ns / 3 ≈ 6.67 ns.

        The range is 0 ≤ :c:member:`start` ≤ :c:member:`stop` < 2\ :sup:`16`.

        After a trigger event, a timer starts. Once the timer reaches
        :c:member:`start`, the TiGer activates. Once the timer reaches
        :c:member:`stop`, the TiGer deactivates.

        If another trigger event is detected before the timer reaches
        :c:member:`stop` and :c:member:`retrigger` is true, the timer resets
        to :c:member:`start`.


    .. c:member:: int sources

        A bitmask with a bit set for all trigger sources that can trigger this
        TiGer block.

        Default is :c:macro:`XTDC4_TRIGGER_SOURCE_S`.

        Possible trigger sources are:

        .. c:macro:: XTDC4_TRIGGER_SOURCE_NONE

            ``0x00000000``. No sources will trigger the TiGer block.

        .. c:macro:: XTDC4_TRIGGER_SOURCE_S

            ``0x00000001``. If this bit is set, the Start channel can trigger the TiGer
            block.

        .. c:macro:: XTDC4_TRIGGER_SOURCE_A

            ``0x00000002``. If this bit is set, Stop channel A can trigger the TiGer
            block.

        .. c:macro:: XTDC4_TRIGGER_SOURCE_B

            ``0x00000004``. If this bit is set, Stop channel B can trigger the TiGer
            block.

        .. c:macro:: XTDC4_TRIGGER_SOURCE_C

            ``0x00000008``. If this bit is set, Stop channel C can trigger the TiGer
            block.

        .. c:macro:: XTDC4_TRIGGER_SOURCE_D

            ``0x00000010``. If this bit is set, Stop channel D can trigger the TiGer
            block.

        .. c:macro:: XTDC4_TRIGGER_SOURCE_AUTO

            ``0x00004000``. If this bit is set, the
            :ref:`auto trigger function generator <sec auto trigger>` can trigger
            the TiGer block.

        .. c:macro:: XTDC4_TRIGGER_SOURCE_ONE

            ``0x00008000``. If this bit is set, the TiGer block is triggered every
            clock cycle.

        For example, if you want the Start channel and the auto trigger to trigger
        the TiGer block:

        .. code-block:: c

            int bitmask = XTDC4_TRIGGER_SOURCE_S | XTDC4_TRIGGER_SOURCE_AUTO;
            config.tiger_block[i].sources = bitmask;


