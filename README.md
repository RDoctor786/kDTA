# kDTA

## Project Description
Python code to analyze the heating rate of a single high temperature susceptibility bridge (HTSB) measurement as described in
> Doctor, R. & Feinberg, J. M. (in review). Differential thermal analysis using high temperature susceptibility instruments. JGR: Solid Earth

This analysis uses the heating information from a blank sample and the sample of interest measured on an HTSB to calculate thermal fluctuations. 

Please cite this paper if using the code in your research.

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
.txt input files must include time and temperature columns and have column names as the first row:
- blank file
- sample file
	
### Output:
plot of the heating rate analysis, detrended, with locally weighted regression smoothing over a 3% window


## Contact
Rashida Doctor
docto005@umn.edu
