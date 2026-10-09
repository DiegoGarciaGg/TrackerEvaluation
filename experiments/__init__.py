"""Experiments: run the kit tracker (unchanged) over a detection source and record provenance.

This package is the only place that executes the tracker. ``evaluation/`` never does; it reads
the CSVs written here. ``opencv`` is allowed here (frame count and fps come from the video).
"""
