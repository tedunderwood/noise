Measuring the consequences of noise in digital libraries
=========================================================

Code and data used for a proof of concept experiment, establishing the need for a project that measures the downstream consequences of different types of noise, including paratext as well as OCR error.

We have subdivided folders into **code** and **data**.

code
======

corpusbuilding
--------------

Code used to compare Gutenberg, TCP-ECCO, and HathiTrust holdings in order to identify a sample of matched files. Also a script I used to download Hathi files.

train
--------
Code that actually trains predictive models.

vizscripts
----------

Visualization scripts, in R.

wordcounting
------------

Code used to turn text files into wordcounts.

data
=======

allclean
--------
Manually transcribed texts, with paratext removed.

gutendirty
----------

Raw data for Gutenberg files.

hathidirty
-----------

Raw data for HathiTrust files.

quadallclean
-------------

Tabular data files for the clean manually transcribed texts.

quaddirtyweak
-------------

Tabular data files for the uncorrected optically transcribed texts.

quaddirtystrong
---------------

Tabular data files for optically transcribed texts that have undergone some simple OCR correction (see **wordcounting**) but still have paratext.

quadcleanstrong
---------------

Tabular data files for optically transcribed texts that have undergone some simple OCR correction (see **wordcounting**) and have paratext removed.


