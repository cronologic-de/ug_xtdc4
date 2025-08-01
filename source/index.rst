xTDC4 User Guide
================


.. raw:: latex

    \RaggedRight

.. raw:: latex 

    \phantomsection
    \addcontentsline{toc}{chapter}{Introduction}
    \chapter*{Introduction}


The xTDC4 is a *common-start* high resolution time-to-digital converter.
Timestamps of leading or trailing edges of digital pulses are recorded.
The xTDC4 produces a stream of output packets, each containing data from a single
start event.
The relative timestamps of all stop pulses that occur within a configurable
range are grouped into one packet.

.. only:: latex

    This User Guide is also available online at 
    `docs.cronologic.de/xtdc4 <https://docs.cronologic.de/xtdc4>`_.

.. only:: html

    Features
    --------

.. raw:: latex 

    \phantomsection
    \addcontentsline{toc}{section}{Features}
    \section*{Features}

- 4-channel common-start TDC with 8 ps resolution
- Standard Range: 218 µs (24-bit timestamp)
- Extended Range: 13.975 ms
- Bin size: 13 ps
- Double-pulse resolution for best results: 5 ns
- Double-pulse resolution without lost hits: 1.7 ns
- Dead time between groups: none
- Minimum interval between starts: 250 ns
- L0 FIFO: 15 words/channel
- L1 FIFO: 512 words/channel
- L2 FIFO: 8000 words
- PCIe 1.1 x1 with 200 MB/s throughput


.. only:: html

    Applications
    ------------

.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{section}{Applications}
    \section*{Applications}


The xTDC4 can be used in all time measurement applications where a common start
setup with four channels is sufficient.
For alternatives with more channels or more flexible grouping check our TDC
website at `www.cronologic.de <https://www.cronologic.de>`__.

The xTDC4 is well suited for the following applications:

- Time-Of-Flight Mass Spectrometers (TOF-MS)
- LIDAR down to 2 mm resolution
- Reciprocal counters
- Coincidence measurements
- Quantum communication
- Time-Correlated Single Photon Counting (TCSPC)
- Synchronization of atomic clocks
- Fluorescence Lifetime Imaging Microscopy (FLIM)

.. only:: html

    Contents
    --------

.. toctree::
   :maxdepth: 2
   
   hardware
   functionality
   api_reference/index
   example
   technical_data
   ordering_information
   revhistory