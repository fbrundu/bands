=====
bands
=====


.. image:: https://img.shields.io/pypi/v/bands.svg
        :target: https://pypi.python.org/pypi/bands

.. image:: https://img.shields.io/travis/fbrundu/bands.svg
        :target: https://travis-ci.org/fbrundu/bands

.. image:: https://readthedocs.org/projects/bands/badge/?version=latest
        :target: https://bands.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/fbrundu/bands/shield.svg
     :target: https://pyup.io/repos/github/fbrundu/bands/
     :alt: Updates


Chromosome bands plotting

* Free software: MIT license

Features
--------

.. image:: https://user-images.githubusercontent.com/697622/36401117-4317d56e-15a3-11e8-9939-fe65e256fb2f.png

It is a stub/unfinished and I cannot work on it right now. So feel free to update it, I may provide some support from time to time.

It is not yet published on pypi, install it with:

.. code:: shell

    pip install git+https://github.com/fbrundu/bands

The first argument contains the data for the genes you want to plot.
It should be a pandas DataFrame formatted similarly to a bedfile, with columns:

* "Chr" (name of the chromosome for the gene)
* "Start" (start coordinate of the gene) 
* "Stop" (end coordinate of the gene)
* "Name" (name/symbol/etc. for the gene)
* "colors" (color to associate to the gene in the map, it should be a string in the form, e.g., "#ffffff" for white - you don't want to color too many genes or the figure may get very crowded)

Credits
---------

Original author: Ryan Dale https://gist.github.com/daler/c98fc410282d7570efc3

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

