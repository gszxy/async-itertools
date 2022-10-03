async-itertools
=================

.. image:: https://readthedocs.org/projects/async-itertools/badge/?version=latest
   :target: https://async-itertools.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

This library provides wrappers and routines inspired by ``itertools``
and ``more_itertools``, but for **asynchronous** iterables.

This project is currently under development.
Feel free to share your thoughts or ideas by submitting an issue or start a discussion.


Install
----------------------

async-itertools requires python >= 3.8

To install with pip, run::

   pip install async_itertools

Overview
------------------------

This section gives a simple overview of all available functions.
For detailed usage, please refer to the `document <https://async-itertools.readthedocs.io/en/latest/>`_.

+-----------+------------------------------------------------------------------+
|category   |functions                                                         |
+===========+==================================================================+
|grouping   |                                                                  |
+-----------+------------------------------------------------------------------+
|combining  |``chain``                                                         |
+-----------+------------------------------------------------------------------+
|windowing  |                                                                  |
+-----------+------------------------------------------------------------------+
|wrapping   |``as_async``                                                      |
+-----------+------------------------------------------------------------------+
|others     |                                                                  |
+-----------+------------------------------------------------------------------+


Build and Test
----------------------

This project uses PEP-517 packaging API. This requires ``build`` package::

   pip install build

To build both ``sdist`` and ``wheel`` package, run::

   python -m build

To install all development dependencies, run::

   pip install setuptools setuptools-scm tox coverage pytest pytest-cov mypy flake8 sphinx furo

This project uses ``tox`` to integrate linting and testing.
To run tests on all supported python versions(you will need to install them first), run::

   tox

To run static check(flake8) and type check(mypy) only, run::

   tox -e linting

To run tests on specific python versions, for example, on cpython3.9 and 3.10, use::

   tox -e py39,py310

The documents are built using ``sphinx`` and the ``furo`` theme.

To build docs on linux, run::

   cd docs && make html

LICENSE
----------------------

This project is licensed under the MIT license.
For detailed information. please read the ``LICENSE`` file in the repository.
