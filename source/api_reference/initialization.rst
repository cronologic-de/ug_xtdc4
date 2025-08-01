.. raw:: latex

    \clearpage

.. _sec initialization:

==============
Initialization
==============

To initialize an xTDC4:

- Get a default set of initialization parameters using
  :c:func:`xtdc4_get_default_init_parameters`.
- Change parameters of :c:struct:`xtdc4_init_parameters` according to your
  specific requirements.
- Initialize an xTDC4 device using :c:func:`xtdc4_init`.
- Release all resources using :c:func:`xtdc4_close`.

The following example shows a basic setup of an xTDC4 using the default
initialization parameters.
A complete coding example can be found on
`github.com/cronologic-de/xtdc_babel <https://github.com/cronologic-de/xtdc_babel>`__
or in Section :ref:`sec code example`.

.. code-block:: C

    // get a default set of initialization parameters
    xtdc4_init_parameters params;
    status = xtdc4_get_default_init_parameters(&params);
    if (status != XTDC4_OK) { /* handle error */ }

    // initialize a device
    const char* err_message;
    xtdc4_device* device = xtdc4_init(&params, &status, &err_message);
    if (status != XTDC4_OK) { /* handle error */ }

    // use device

    // after usage, free up all resources by closing the device
    status = xtdc4_close(device)



xtdc4_get_default_init_parameters
=================================

.. c:function:: int xtdc4_get_default_init_parameters(\
    xtdc4_init_parameters *init)

    Initialize an :c:struct:`xtdc4_init_parameters` struct with default values.

    You should always use this method first to set up your initialization parameters,
    then adjust the parameters to your specific needs.

    :param init: Pointer to a :c:struct:`xtdc4_init_parameters` struct that
        will be filled.

    :returns: Status codes:
        :c:macro:`XTDC4_OK` or
        :c:macro:`XTDC4_CRONO_INVALID_ARGUMENTS`.

xtdc4_init
==========

.. c:function:: xtdc4_device xtdc4_init(\
    xtdc4_init_parameters *params,\
    int *error_code,\
    char **error_message)

    Opens and initializes the xTDC4 board with index
    :c:member:`params.card_index <xtdc4_init_parameters.card_index>`.

    :param params: Pointer to a :c:struct:`xtdc4_init_parameters`.
        The struct must have been completely initialized using
        :c:func:`xtdc4_get_default_init_parameters`.

    :param error_code: Pointer to the location where a potential error code will be
        stored.
        Equals :c:macro:`XTDC4_OK` if no error occurred. Otherwise can be
        :c:macro:`XTDC4_CRONO_INVALID_ARGUMENTS`,
        :c:macro:`XTDC4_DEVICE_OPEN_FAILED`,
        :c:macro:`XTDC4_HARDWARE_FAILURE`,
        :c:macro:`XTDC4_INVALID_BUFFER_PARAMETERS`,
        :c:macro:`XTDC4_CRONO_INTERNAL_ERROR`, or
        :c:macro:`XTDC4_WRONG_STATE`.


    :param error_message: Pointer to a location where a potential error message in plain
        text will be stored.

    :return: The xTDC4 device corresponding to
        :c:member:`params.card_index <xtdc4_init_parameters.card_index>`.


xtdc4_close
===========

.. c:function:: int xtdc4_close(xtdc4_device *device)

    Close an initialized xTDC4 device, releasing all resources.

    :param device: Pointer to the device that shall be closed.

    :returns: Status code:
        :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`,
        :c:macro:`XTDC4_WRONG_STATE`, or
        :c:macro:`XTDC4_CRONO_INTERNAL_ERROR`.


xtdc4_init_parameters
=====================

.. include:: structs/xtdc4_init_parameters.rst

xtdc4_device
============

.. c:struct:: xtdc4_device

    Structure referencing an initialized xTDC4 device.

    .. c:member:: void* xtdc4
