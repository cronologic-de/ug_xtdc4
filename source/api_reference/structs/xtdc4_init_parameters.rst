.. c:struct:: xtdc4_init_parameters

    Struct for the initialization of the xTDC4.

    This structure must be completely initialized. For this, obtain a default
    set of initialization parameters first by using
    :c:func:`xtdc4_get_default_init_parameters`, then adjust parameters
    for your use case.

    .. c:member:: int version

        The version number.

        Must be set to :c:macro:`XTDC4_API_VERSION`.

    .. c:member:: int card_index

        The index in the list of xTDC4 boards that should be initialized.

        There might be multiple boards in the system that are handled by
        the driver as reported by :c:func:`xtdc4_count_devices`. This index
        selects one of them.

        Boards are enumerated depending on the PCIe slot.
        The lower the bus number and the lower the slot number the lower the
        card index.

    .. c:member:: int board_id

        The global index in all cronologic devices.

        This 8-bit number is filled into each packet created by the
        board and is useful if data streams of multiple boards are be merged.

        If only xTDC4 cards are used this number can be set to the
        :c:member:`card_index`.

        If boards of different types that use a compatible data format are used in a 
        system, each board should get a unique ID.

    .. c:member:: uint64_t buffer_size[8]

        The minimum size of the DMA buffer in bytes.

        Defaults to 4 :math:`\times` 1024 :math:`\times` 1024 bytes.

        The minimal possible size is 1024 :math:`\times` 1024 bytes.

        For the xTDC4, only the first entry is used.

    .. c:member:: int buffer_type

        The type of buffer.

        Must be one of the following:

        .. c:macro:: XTDC4_BUFFER_ALLOCATE

            Use allocated buffer.

        .. c:macro:: XTDC4_BUFFER_USE_PHYSICAL

            Use physical buffer (currently not supported).

    .. c:member:: uint64_t buffer_address

        The start address of the reserved memory.

        The buffers will be allocated with the sizes given above. Make
        sure that the memory is large enough.

    .. c:member:: int variant

        A variant, for reconfiguring the chip for future extension. Currently fixed at 0.

    .. c:member:: int device_type

        A constant for the different devices from cronologic.

        Initialized by :c:func:`xtdc4_get_default_init_parameters`
        to :c:macro:`CRONO_DEVICE_XTDC4`.

        Must be left unchanged.

    .. c:member:: int dma_read_delay

        The update delay of the writing pointer after a packet has
        been send over PCIe.

        Given in multiples of 16 ns.

        Must be left unchanged.

    .. c:member:: int use_ext_clock

        Select external 10 MHz reference.

        | If set to 1 use external 10 MHz reference.
        | If set to 0 use internal reference.

    .. c:member:: int rclk_sel

        Set THS788 RClk frequency, default is :c:macro:`TDC4_RCLK_150M`.

        Must be one of the following:

        .. c:macro:: TDC4_RCLK_37M5

            37.5 MHz

        .. c:macro:: TDC4_RCLK_75M

            75 MHz

        .. c:macro:: TDC4_RCLK_150M

            150 MHz
        