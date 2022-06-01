# kDTA

## Project Description
This repository contains the python code to calculate the heating rate anlysis of a single high temperature susceptibility bridge (HTSB) run as described in
> Doctor, R. & Feinberg, J. M. (in review). Differential thermal analysis using high temperature susceptibility instruments. JGR: Solid Earth

This analysis using the heating rate information form a sample blank and the sample of interest measured on a HTSB to identify thermal fluctuations caused by reactions. 

Please cite paper if using the code in your research.

## How to Run
### Python libraries needed
- numpy
- pandas
- matplotlib
- scipy
- statsmodels

### Run in command prompt (Windows)
	python kDTA_quickplot.py
	
### Inputs:
	blank file - txt with columns corresponding to time and temperature
	sample file - txt with columns corresponding to time and temperature
  file structure - answer prompts to identify time and temperature columns
	
### Output:
	plot of the heating rate analysis, detrended, with locally weighted regression smoothing over 3%


## Contact
Rashida Doctor
docto005@umn.edu
