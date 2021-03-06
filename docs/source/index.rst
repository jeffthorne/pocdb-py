.. pocdb-py documentation master file, created by
   sphinx-quickstart on Thu Apr 12 16:41:36 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pocdb-py
====================================

A Python 3 client for the POCdb Platform.


Installation
------------

.. code-block:: python

   pip install pocdb-py

|
| Note: Requires Python 3.5.2 or higher due to reliance on Python's typing module.
|


Getting Started
---------------
Start by creating an API object. This API represents the POCdb API endpoint.

.. code-block:: python

   from pocdb.models.api import API

   api = API(email=email, password=password)

   regions = ['region1', 'region2']
   products = ['product1', 'product2']

   pocs = api.pocs_by_product(products, regions)  #pocs by product and regions
   pocs = api.pocs(regions)  #poc by regions

