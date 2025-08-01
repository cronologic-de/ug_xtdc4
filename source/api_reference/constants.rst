.. raw:: latex

    \clearpage

===================
Constants and Types
===================

General
=======

.. c:macro:: XTDC4_TDC_CHANNEL_COUNT
    
    The number of TDC input channels.

.. c:macro:: XTDC4_TIGER_COUNT

   The number of :ref:`timing generators <sec tiger>`.

.. c:macro:: XTDC4_TRIGGER_COUNT

    The number of potential trigger sources for the
    :ref:`timing generators <sec tiger>`.

    One for each TDC input and one for the Start input, as well as some special
    trigger. See :c:member:`timetagger4_tiger_block.sources` for more information.

.. c:macro:: XTDC4_API_VERSION
    
    Current version of the API.

.. c:type:: crono_bool_t

    Data type used for booleans in various structs.


Status Codes
============

.. c:macro:: XTDC4_OK

    Equals ``0``. Return value of various API functions if no error occurred.

.. c:macro:: XTDC4_DEVICE_NOT_FOUND

    Equals ``2``.

.. c:macro:: XTDC4_NOT_INITIALIZED

    Equals ``3``.

.. c:macro:: XTDC4_WRONG_STATE

    Equals ``4``.

.. c:macro:: XTDC4_INVALID_DEVICE

    Equals ``5``.

.. c:macro:: XTDC4_BUFFER_ALLOC_FAILED

    Equals ``6``.

.. c:macro:: XTDC4_INVALID_BUFFER_PARAMETERS

    Equals ``8``.

.. c:macro:: XTDC4_INVALID_CONFIG_PARAMETERS

    Equals ``9``.

.. c:macro:: XTDC4_HARDWARE_FAILURE

    Equals ``11``.

.. c:macro:: XTDC4_SYNCHRONIZATION_FAILED

    Equals ``13``.

.. c:macro:: XTDC4_DEVICE_OPEN_FAILED

    Equals ``14``.

.. c:macro:: XTDC4_CRONO_INTERNAL_ERROR
    
    Equals ``15``.

.. c:macro:: XTDC4_CRONO_INVALID_ARGUMENTS

    Equals ``17``.

cronologic Device IDs
=====================

.. c:macro:: CRONO_DEVICE_XTDC4