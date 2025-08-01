.. c:struct:: crono_pcie_info

    .. c:member:: uint32_t pwr_mgmt

        Organizes power supply of the PCIe lanes.

    .. c:member:: uint32_t link_width

        Number of PCIe lanes that the card uses.

    .. c:member:: uint32_t max_payload

        Maximum size in bytes for one PCIe transaction.

    .. c:member:: uint32_t link_speed

        Data rate of the PCIe card.

    .. c:member:: uint32_t error_status_supported

        Different from 0 if the PCIe error status is supported for this device.

    .. c:member:: uint32_t correctable_error_status

        Correctable error status flags.

        Read directly from the PCIe config register.

        Useful for debugging PCIe problems.

        One of the following:

        .. c:macro:: CRONO_PCIE_RX_ERROR

            Equals ``1 << 0``.

        .. c:macro:: CRONO_PCIE_BAD_TLP

            Equals ``1 << 6``.

        .. c:macro:: CRONO_PCIE_BAD_DLLP

            Equals ``1 << 7``.

        .. c:macro:: CRONO_PCIE_REPLAY_NUM_ROLLOVER

            Equals ``1 << 8``.

        .. c:macro:: CRONO_PCIE_REPLAY_TIMER_TIMEOUT

            Equals ``1 << 12``.

        .. c:macro:: CRONO_PCIE_ADVISORY_NON_FATAL

            Equals ``1 << 13``.

        .. c:macro:: CRONO_PCIE_CORRECTED_INTERNAL_ERROR

            Equals ``1 << 14``.

        .. c:macro:: CRONO_PCIE_HEADER_LOG_OVERFLOW

            Equals ``1 << 15``.


    .. c:member:: uint32_t uncorrectable_error_status

        Uncorrectable error status flags.

        Read directly from the PCIe config register.

        Useful for debugging PCIe problems.

        One of the following:

        .. c:macro:: CRONO_PCIE_UNC_UNDEFINED

            Equals ``1 << 0``.

        .. c:macro:: CRONO_PCIE_UNC_DATA_LINK_PROTOCOL_ERROR

            Equals ``1 << 4``.

        .. c:macro:: CRONO_PCIE_UNC_SURPRISE_DOWN_ERROR

            Equals ``1 << 5``.

        .. c:macro:: CRONO_PCIE_UNC_POISONED_TLP

            Equals ``1 << 12``.

        .. c:macro:: CRONO_PCIE_UNC_FLOW_CONTROL_PROTOCOL_ERROR

            Equals ``1 << 13``.

        .. c:macro:: CRONO_PCIE_UNC_COMPLETION_TIMEOUT

            Equals ``1 << 14``.

        .. c:macro:: CRONO_PCIE_UNC_COMPLETER_ABORT

            Equals ``1 << 15``.

        .. c:macro:: CRONO_PCIE_UNC_UNEXPECTED_COMPLETION

            Equals ``1 << 16``.

        .. c:macro:: CRONO_PCIE_UNC_RECEIVER_OVERFLOW_ERROR

            Equals ``1 << 17``.

        .. c:macro:: CRONO_PCIE_UNC_MALFORMED_TLP

            Equals ``1 << 18``.

        .. c:macro:: CRONO_PCIE_UNC_ECRC_ERROR

            Equals ``1 << 19``.

        .. c:macro:: CRONO_PCIE_UNC_UNSUPPORED_REQUEST_ERROR

            Equals ``1 << 20``.


