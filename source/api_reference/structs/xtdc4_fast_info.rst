.. c:struct:: xtdc4_fast_info

    .. c:member:: int size

        The number of bytes this struct occupies.

    .. c:member:: int version

        Version number of this struct. It is increased when the definition of the
        struct changes.

    .. c:member:: int tdc_rpm

        Speed of the TDC fan in rounds per minute.

        0 if no fan is present.

    .. c:member:: int fpga_rpm

        Speed of the FPGA fan in rounds per minute.

        0 if no fan is present.

    .. c:member:: int alerts

        Alert bits from the temperature sensor and the system monitor.

        Bit 0 is set, if the TDC temperature exceeds 140°C. If set, the TDC
        shut down and the device needs to be reinitialized.

    .. c:member:: int pcie_pwr_mgmt

        Fixed at 0.

    .. c:member:: int pcie_link_width

        Number of PCIe lanes the xTDC4 device uses.

        Should always be 10.

    .. c:member:: int pcie_max_payload

        Maximum size in bytes for one PCIe transaction.

        Depends on the system configuration.