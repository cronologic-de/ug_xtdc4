.. raw:: latex

    \clearpage

.. _sec readout:

============
Data Readout
============

The device provides a stream of *packets* (see :ref:`sec data format`)
that are read in batches with :c:func:`xtdc4_read`.

:c:func:`xtdc4_read` requires :c:struct:`xtdc4_read_in` as configuration.

:c:func:`xtdc4_read` stores the read batch in a :c:struct:`xtdc4_read_out`
struct.

Every packet needs to be *acknowledged* before its memory location can be used again
by the xTDC4 device.

A typical workflow in an application would be:

- Start data acquisition (see :ref:`sec runtime control`).
- Read a batch of packets.
- Iterate through the batch and process the packets (see :ref:`sec data format` for
   the data layout). For this purpose, :c:macro:`crono_next_packet` is provided.
- Acknowledge the batch as processed with :c:func:`xtdc4_acknowledge`.

Instead of manually acknowledging each batch, each read batch of data can be
automatically acknowledged by setting
:c:struct:`xtdc4_read_in.acknowledge_last_read` to true.

The following example highlights the workflow.
A complete coding example can be found on
`github.com/cronologic-de/xtdc_babel <https://github.com/cronologic-de/xtdc_babel>`__
or in Section :ref:`sec code example`.

.. code-block:: C

    timetagger_read_in read_config;
    read_config.acknowledge_last_read = true;
    timetagger_read_out read_data;

    status = xtdc4_read(device, &read_config, &read_data)
    if (status != XTDC4_OK) {
        // handle errors of the call to xtdc4_read
    }
    else if (read_data.error_code != CRONO_READ_OK)
    {
        // handle read errors, e.g., empty packets
    }
    else
    {
        volatile crono_packet *p = read_data.first_packet;
        while (p <= read_data.last_packet)
        {

            /* process data */

            p = crono_next_packet(p);
        }
    }

.. _sec memory management:

Memory Management
=================

The xTDC4 internal FIFOs (first-in, first-out) that buffer data during
acquisition.

The data is streamed from the FIFO to the
host PC and stored in the *host buffer*. Data will only be overwritten in the
host buffer if it has been *acknowledged*.

The host buffer is managed by the DMA (direct memory access) driver. The DMA driver
can only ever write to the host buffer if enough memory is free. That means, new
packets will never overwrite old packets unless they have been acknowledged.

If the host buffer is full, data may be lost. If this occurred, the corresponding
packets will have the
:c:macro:`XTDC4_PACKET_FLAG_HOST_BUFFER_FULL<crono_packet.flags.XTDC4_PACKET_FLAG_HOST_BUFFER_FULL>`
bit of :c:member:`crono_packet.flags` will be set. This may result in lost packets.

If the hit rate is too high, the internal FIFOs may fill up. If this is the case,
the affected packets will have the
:c:macro:`XTDC4_PACKET_FLAG_DMA_FIFO_FULL<crono_packet.flags.XTDC4_PACKET_FLAG_DMA_FIFO_FULL>`
bit of :c:member:`crono_packet.flags` will be set. This may result in lost packets.
However, only if the 
:c:macro:`XTDC4_PACKET_FLAG_SHORTENED<crono_packet.flags.XTDC4_PACKET_FLAG_SHORTENED>`
bit of :c:member:`crono_packet.flags` is set, packets were actually missed.

xtdc4_read
================

.. c:function:: int xtdc4_read(\
    xtdc4_device *device,\
    xtdc4_read_in *in,\
    xtdc4_read_out *out)

    Read captured data.

    Data is read in batches of *packets*. Pointers to the first and last packets
    are stored in :c:member:`out.first_packet <xtdc4_read_out.first_packet>`
    and :c:member:`out.last_packet <xtdc4_read_out.last_packet>`.

    :param device: Pointer to an xTDC4 device.
    :param in: Pointer to an :c:struct:`xtdc4_read_in` struct, configuring the
        read call.
    :param out: Pointer to an :c:struct:`xtdc4_read_out` that will be filled
        by the call.
    :return: Status code:
        Same as :c:member:`out.error_code <xtdc4_read_out.error_code>`, or
        :c:macro:`XTDC4_INVALID_DEVICE`.




xtdc4_acknowledge
=======================

.. c:function:: int xtdc4_acknowledge(\
    xtdc4_device *device,\
    crono_packet *packet)

    Acknowledge all packets up to ``packet``.

    Only acknowledged data can be overwritten by the DMA controller.

    Explicitly calling ``xtdc4_acknowledge`` is only necessary if
    :c:func:`xtdc4_read` was called with ``in.acknowledge_last_read == false``.

    .. note::

        ``xtdc4_acknowledge`` allows freeing up memory early if there will
        be no call to :c:func:`xtdc4_read` anytime soon.

    .. note::

        ``xtdc4_acknowledge`` allows keeping data over multiple calls of
        :c:func:`xtdc4_read`, avoiding unnecessary copying of data.

    .. attention::

        After acknowledging a packet, it becomes *immediately* invalid. It is
        *immediately* unsafe to attempt accessing its content.

    :param device: Pointer to an xTDC4 device.
    :param packet: Pointer to a packet. All packets up to this one will be acknowledged.
    :return: Status code:
        :c:macro:`XTDC4_OK`, or
        :c:macro:`XTDC4_INVALID_DEVICE`.



crono_next_packet
=================

.. c:macro:: crono_next_packet(current_packet)

    Convenience macro that jumps to the next :c:struct:`crono_packet`.

    .. attention::

        You must explicitly check that the pointer to the next packet is valid!

    :param current_packet: Pointer to the current packet.
    :return: Pointer to the next packet.


xtdc4_read_in
===================

.. c:struct:: xtdc4_read_in

    .. c:member:: crono_bool_t acknowledge_last_read
        
        Automatically acknowledge last readout.

        If set, :c:func:`xtdc4_read` automatically acknowledges packets from
        the last read.

        Otherwise, :c:func:`xtdc4_acknowledge` needs to be explicitly called
        by the user.


xtdc4_read_out
====================

.. c:struct:: xtdc4_read_out

    .. c:member:: crono_packet *first_packet

        Pointer to the first packet that was captured by the call of
        :c:func:`xtdc4_read`.

    .. c:member:: crono_packet *last_packet

        Pointer to the last packet that was captured by the call of
        :c:func:`xtdc4_read`.

        This packet is still valid. All data after this packet is invalid.

    .. c:member:: int error_code

        Error codes.

        One of the following:

        .. c:macro:: CRONO_READ_OK

            ``0``. Read was successful. No errors occurred.

        .. c:macro:: CRONO_READ_NO_DATA

            ``1``. The read attempt did not yield any data.

        .. c:macro:: CRONO_READ_INTERNAL_ERROR

            ``2``. Some unhandled error occurred. The xTDC4 device needs to be
            reinitialized.
        
        .. c:macro:: CRONO_READ_TIMEOUT

            ``3``. Attempt to read packets did not yield data in the given time.

    .. c:member:: const char* error_message

        Error message in human-readable form.

        This may contain additional information about :c:member:`error_code`.