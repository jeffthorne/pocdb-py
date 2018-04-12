.. pocdb-py documentation master file, created by
   sphinx-quickstart on Thu Apr 12 16:41:36 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pocdb-py
====================================

A Python 3 client for the pocdb Platform.


Installation
------------

.. code-block:: python

   pip install pocdb-py

|
| Note: Requires Python 3.5.2 or higher due to reliance on Python's typing module.
|


Getting Started
---------------
Start by creating a DSM manager object. This manager represents the DSM API endpoint

.. code-block:: python

   from pocdb.models.api import API

   api = API(email=email, password=password, host="https://www.pocdb.com", api_version='v1', verify_cert=False)
   pocs = api.pocs_by_product(product, region)




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
