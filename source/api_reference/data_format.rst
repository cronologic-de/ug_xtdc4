.. raw:: latex

    \clearpage

.. _sec data format:

==================
Output Data Format
==================

Data read from :c:func:`xtdc4_read` is provided as *packets*. The data
layout of a packet is :c:struct:`crono_packet`.

The following code snippets shows the principal of how to unpack a
:c:struct:`crono_packet`.

A complete coding example can be found on
`github.com/cronologic-de/xtdc_babel <https://github.com/cronologic-de/xtdc_babel>`__
or in Section :ref:`sec code example`.

.. code-block:: C

    uint32_t binsize_ps = param_info->packet_binsize;

    int64_t absolute_time_bins = packet->timestamp;
    double absolute_time_ps = absolute_time_bins * binsize_ps;

    // 2 TDC hits are in each packet->data word.
    int hit_count = 2 * packet->length;
    // If an odd number of hits were recorded, the high 32 bits of the last data word
    // do not contain valid data
    if ((packet->flags & XTDC4_PACKET_FLAG_ODD_HITS) != 0)
        hit_count -= 1;

    uint32_t *packet_data = (uint32_t*)(packet->data);

    // keep track of possible timestamp rollovers
    uint32_t rollover_counter = 0;
    uint64_t rollover_period_bins = static_info->rollover_period;

    for(int i=0; i<hit_count; ++i)
    {
        uint32_t channel = packet_data[i]      & 0xF;
        uint32_t flags   = packet_data[i] >> 4 & 0xF;

        if ((flags & XTDC4_HIT_FLAG_TIME_OVERFLOW) != 0)
        {
            rollover_counter += 1;
        }
        else
        {
            uint32_t timestamp_bins = packet_data[i] >> 8 & 0xFFFFFF;
            double timestamp_ps = binsize * (
                timestamp_bins + rollover_counter * rollover_period_bins);
            double absolute_timestamp = absolute_time_ps + timestamp_ps;
        }
    }


crono_packet
============

.. c:struct:: crono_packet

    .. c:member:: uint8_t channel

        Always 0 for the xTDC4.

        The channel source of a hit are encoded in :c:member:`data`.

    .. c:member:: uint8_t card

        Identifies the source card of the data, in case multiple xTDC4
        are installed in the system.

        Defaults to 0 if no value is assigned to
        :c:member:`xtdc4_init_parameters.board_id`.

    .. c:member:: uint8_t type

        The type of :c:member:`crono_packet.data`.

        In case of the xTDC4, this is always an 32-bit unsigned integer,
        corresponding to ``CRONO_PACKET_TYPE_32_BIT_UNSIGNED``.
            
    .. c:member:: uint8_t flags

        Bit field of packet flags.

        Each bit corresponds to one of the following:

        .. c:macro:: XTDC4_PACKET_FLAG_ODD_HITS

            ``0x1``.
            
            If this bit is set, the last word in the :c:member:`data` array
            consists of one timestamp only, which means that only  the lower 32
            bits (little endian) of the 64-bit data word are valid.
        
        .. c:macro:: XTDC4_PACKET_FLAG_SLOW_SYNC

            ``0x2``.

            If this bit is set, the timestamp of a hit is above the range of the
            8-bit rollover number and the 24-bit hit timestamp. The group is closed
            and all other hits are ignored.

        .. c:macro:: XTDC4_PACKET_FLAG_START_MISSED

            ``0x4``.

            If this bit is set, packets were discarded due to a full FIFO
            potentially caused by a data hit rate that is too high.

            Starts were missed and stops are potentially in wrong groups.

        .. c:macro:: XTDC4_PACKET_FLAG_SHORTENED

            ``0x8``.

            If this bit is set, packets were shortened due to a full pipeline of the
            FIFO potentially caused by a data hit rate that is too high.

            Stops are missing in the current packet.

        .. c:macro:: XTDC4_PACKET_FLAG_DMA_FIFO_FULL

            ``0x10``.

            If this bit is set, the internal FIFO was full, potentially caused by a
            hit rate that is too high.

        .. c:macro:: XTDC4_PACKET_FLAG_HOST_BUFFER_FULL

            ``0x20``.

            If this bit is set, the host buffer was full. This might result in
            dropped packets.

            This is caused either by a hit rate that is too high or by data not being
            retrieved and acknowledged fast enough from the buffer.

            Solutions are increasing the buffer size
            (see :c:member:`xtdc4_init_parameters.buffer_size`) or
            avoiding or optimizing any additional processing in the application
            reading the data.

    .. c:member:: uint32_t length

        Length of :c:member:`data` in multiples of 64 bit.

        Each 64-bit data word contains up to two TDC hits.

        | The number of TDC hits can be calculated as
        | 2 :math:`\times` :c:member:`length` – ((:c:member:`flags` &
            :c:macro:`XTDC4_PACKET_FLAG_ODD_HITS <flags.XTDC4_PACKET_FLAG_ODD_HITS>`)
            ? 1 : 0)

    .. c:member:: uint64_t timestamp

        Coarse timestamp of the Start trigger hit.

        Values are given in multiples :c:member:`xtdc4_param_info.packet_binsize`.


    .. c:member:: uint64_t data[1]

        Contains the TDC hits as variable length array.

        The length is given by :c:member:`length` and can be zero.

        .. note::

            To directly operate on the TDC hit, cast this array to ``uint32_t``.

        The data layout of a 32-bit TDC hit is as follows:

        +------------------+------------------+--------+-----------+
        | Bits             | 31 – 8           | 7 – 4  | 3 – 0     |
        +------------------+------------------+--------+-----------+
        | Content          | 24-bit timestamp | Flags  | Channel   |
        +------------------+------------------+--------+-----------+

        That is, one can extract the timestamp, flags, and channel number as follows:

        .. code-block:: C

            uint32_t timestamp = (hit >> 8) & 0xFFFFFF;
            uint32_t flags     = (hit >> 4) & 0xF;
            uint32_t channel   =  hit       & 0xF;

        The 24-bit timestamp is given in multiples of
        :c:member:`xtdc4_param_info.packet_binsize`.

        Channel value 0–3 correspond to Stop channels A–D.

        The flag bits correspond to the following:

        .. c:macro:: XTDC4_HIT_FLAG_FPGA_MISSING

            ``0x8``, corresponding to **bit 7** of the data word.
            
            See also :c:macro:`XTDC4_HIT_FLAG_COARSE_TIMESTAMP <crono_packet.data.XTDC4_HIT_FLAG_COARSE_TIMESTAMP>`.

        .. c:macro:: XTDC4_HIT_FLAG_COARSE_TIMESTAMP

            ``0x4``, corresponding to **bit 6** of the data word.

            Bits 6 and 7 encode the measurement resolution according to the following
            table:

            +-------+-------+---------------------------------------------------------------------------------+
            | bit 7 | bit 6 | Measurement Type                                                                |
            +=======+=======+=================================================================================+
            | 0     | 0     | Normal, full resolution measurement.                                            |
            +-------+-------+---------------------------------------------------------------------------------+
            | 0     | 1     | Measurement performed with the Delay-Line TDC at about 150 ps resolution.       |
            +-------+-------+---------------------------------------------------------------------------------+
            | 1     | 0     | Full resolution measurement that be might in the wrong place in the data stream.|
            +-------+-------+---------------------------------------------------------------------------------+
            | 1     | 1     | Measurement with only 5000 ps / 6 ≈ 833.3 ps resolution.                        |
            +-------+-------+---------------------------------------------------------------------------------+


        .. c:macro:: XTDC4_HIT_FLAG_TIME_OVERFLOW

            ``0x2``.

            If this bit is set, the data word indicates a rollover and
            does *not* encode a TDC hit.

            The time since the Start trigger hit exceeded the 24-bit range that
            can be encoded in one 32-bit TDC hit.

            To correctly determine the timestamp of the following TDC hits, the
            application needs to increment a rollover counter if the
            ``XTDC4_HIT_FLAG_TIME_OVERFLOW`` bit is set:

            .. code-block:: C

                int rollover_counter = 0;
                if ((flags & XTDC4_HIT_FLAG_TIME_OVERFLOW) != 0)
                {
                    rollover_counter += 1;
                }
                timestamp += rollover_counter * rollover_period

            ``rollover_period`` is given by
            :c:member:`xtdc4_static_info.rollover_period`.

            .. attention::

                The rollover counter needs to be reset for each
                :c:struct:`crono_packet`.

        .. c:macro:: XTDC4_HIT_FLAG_RISING

            ``0x1``.

            If this bit is set, this hit corresponds to a signal's rising edge,
            otherwise to a falling edge.




