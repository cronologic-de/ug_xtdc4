.. raw:: latex

    \clearpage

.. _sec configuration:

=============
Configuration
=============

After an xTDC4 device has been initialized (see :ref:`sec initialization`), it
must be configured before it can acquire data.

To configure an xTDC4 device:

- Get a default set of configuration parameters using
  :c:func:`xtdc4_get_default_configuration`.
- Change parameters of :c:struct:`xtdc4_configuration` according to your
  specific requirements.
- Configure the xTDC4 device using :c:func:`xtdc4_configure`.

The following example shows a basic configuration of an already initialized xTDC4
device using the default configuration parameters.
A complete coding example can be found on
`github.com/cronologic-de/xtdc_babel <https://github.com/cronologic-de/xtdc_babel>`__
or in Section :ref:`sec code example`.

.. code-block:: C

    // get a default set of configuration parameters
    xtdc4_configuration config;
    status = xtdc4_get_default_configuration(device, &config);
    if (status != XTDC4_OK) { /* handle error */ }

    // configure the device
    status = xtdc4_configure(device, &config);
    if (status != XTDC4_OK) { /* handle error */ }


xtdc4_configure
=====================

.. c:function:: int xtdc4_configure(\
    xtdc4_device *device,\
    xtdc4_configuration *config)

    Configures an xTDC4 device.

    :param device: Pointer to an xTDC4 device.
    :param config: Pointer to an :c:struct:`xtdc4_configuration` struct used
        for the configuration.
    :return: Status code: :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`,
        :c:macro:`XTDC4_HARDWARE_FAILURE`, or
        :c:macro:`XTDC4_INVALID_CONFIG_PARAMETERS`.


xtdc4_get_default_configuration
=====================================

.. c:function:: int xtdc4_get_default_configuration(\
    xtdc4_device *device,\
    xtdc4_configuration *config)

    Obtain a default set of configuration parameters.

    :param device: Pointer to an xTDC4 device.
    :param config: Pointer to an :c:struct:`xtdc4_configuration` struct that
        will be filled.
    :return: Status code: :c:macro:`XTDC4_OK`,
        :c:macro:`XTDC4_INVALID_DEVICE`, or
        :c:macro:`XTDC4_CRONO_INVALID_ARGUMENTS`.


xtdc4_get_current_configuration
=====================================

.. c:function:: int xtdc4_get_current_configuration(\
    xtdc4_device *device,\
    xtdc4_configuration *config)

    Obtain the current set of configuration parameters of an already configured
    xTDC4 device.

    :param device: Pointer to a configured xTDC4 device.
    :param config: Pointer to a :c:struct:`xtdc4_configuration` struct that
        will be filled.
    :return: Status code: :c:macro:`XTDC4_OK`, or
        :c:macro:`XTDC4_INVALID_DEVICE`.

xtdc4_configuration
=========================

.. include:: structs/xtdc4_configuration.rst


xtdc4_trigger
===================

.. include:: structs/xtdc4_trigger.rst


xtdc4_tiger_block
=======================

.. include:: structs/xtdc4_tiger_block.rst


xtdc4_channel
===================

.. include:: structs/xtdc4_channel.rst
