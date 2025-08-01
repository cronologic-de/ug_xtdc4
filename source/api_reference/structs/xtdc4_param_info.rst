.. c:struct:: xtdc4_param_info

    This structure is provided by :c:func:`xtdc4_get_param_info`.

    .. c:member:: int size

        The number of bytes this struct occupies.

    .. c:member:: int version

        Version number of this struct. It is increased when the definition of the
        struct changes.

    .. c:member:: double binsize

        Bin size in ps of the measured TDC data.

        For the xTDC4, it is 13.02083 ps.

    .. c:member:: int board_id

        ID of the xTDC4 device.

        Used to identify itself in the output data stream.

        Is between 0 and 255.

    .. c:member:: int channels

        Number of TDC channels of the board.

        Fixed at 4.

    .. c:member:: int channel_mask

        Bit assignment of each enabled input channel.

        Bit 0 ≤ *n* ≤ 3 is set if channel *n* is enabled.

    .. c:member:: int64_t total_buffer

        The total amount of DMA buffer in bytes.

    .. c:member:: double packet_binsize

        For the xTDC4, it is 5000 ps / 3 ≈ 1666.6 ps.

        :c:member:`crono_packet.timestamp` is given in multiples of this value.

    .. c:member:: double quantisation

        Quantisation, that is, measurement resolution of the xTDC4, in ps.

        For the xTDC4, it is equal to :c:member:`xtdc4_param_info.binsize`.



