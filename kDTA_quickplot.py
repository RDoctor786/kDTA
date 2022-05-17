'''
Quick plot for heating rate analysis

@Author: Rashida Doctor
@Date: 05/16/2022

Python 3.7.3

Run in command prompt (Windows)
	python kDTA_quickplot.py
	
Inputs:
	blank file - txt with columns corresponding to time and temperature
	sample file - txt with columns corresponding to time and temperature
	
Output:
	plot of the heating rate analysis, detrended, with locally weighted regression smoothing over 3%
 '''

# libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import statsmodels.api as sm

# function to rename columns
def rename_Commence(data):
	i = 0
	for col in data.columns:
		print(str(i) + '. ' + col)
		i += 1
	time_colold = data.columns[int(input('Which column number corresponds to the time value?  '))]
	temp_colold = data.columns[int(input('Which column number corresponds to the temperature value?  '))]
	data.rename(columns = {time_colold : 'time', temp_colold : 'temp'}, inplace = True)
	#print('Check new dataframe head')
	#print(data.head())
	return(data)

# function to select data
def getheat(mindat, data = None, return_full = False, susplot = True):

        
    # take out first row if all zeros
    if mindat['temp'][0] == 0:
        mindat.drop(labels = [0], inplace = True)
        mindat.reset_index(drop = True, inplace = True)
    

    # split into heating and cooling
    Tmax = max(mindat['temp'])
    mindat.loc[:,'sec'] = 'cool' 
    iTmax = mindat.index[mindat['temp'] == Tmax][0]
    mindat.loc[0:iTmax, 'sec'] = 'heat'
    
    minheat = mindat[mindat['sec'] == 'heat'].copy()
    
    if susplot == True:
        plt.figure(figsize = (10,5))
        plt.plot(mindat['temp'], mindat['csusc'], 'b-')
        plt.plot(minheat['temp'], minheat['csusc'], 'r-')
        plt.xlabel('Temperature (C)')
        plt.ylabel('Uncorrected Susceptibility')
    
    if return_full == True:
        return minheat, mindat
    else:
        return minheat


# get files
blank_filename = input("Enter path to blank file: ")
samp_filename = input("Enter path to sample file: ")

#samp_mass = input("Enter mass of sample in grams: ")

# read files into pandas
blank_og = pd.read_csv(blank_filename, delim_whitespace = True)
sample_og = pd.read_csv(samp_filename, delim_whitespace = True)

# check column names
print(blank_og.head())

while True:
	rename_greenlight = input("Are the columns named time, temp? [T/F]: ")

	if rename_greenlight == 'F':
		print("Let's fix that")
		print("Blank columns:")
		blank_og = rename_Commence(blank_og)
		print("Sample columns:")
		sample_og = rename_Commence(sample_og)
		break
	elif rename_greenlight == 'T':
		print("Great")
		break
	else:
		print("Please answer with T or F")


# read files
blank = getheat(blank_og, susplot = False)
sample = getheat(sample_og, susplot = False)


#interpolation
t_max = max(blank['time'].max(), sample['time'].max())

t = np.arange(0,t_max + 15,15)

int_blank = interp1d(blank['time'][:-5],blank['temp'][:-5], kind = 'linear', bounds_error = False)
temp_blank = int_blank(t)

int_sample = interp1d(sample['time'][:-5],sample['temp'][:-5], kind = 'linear', bounds_error = False)
temp_sample = int_sample(t)


# combined DF
comb_df = pd.DataFrame({'time':t, 'blank': temp_blank, 'samp': temp_sample})


#calculate residual
comb_df['res'] = comb_df['samp'] - comb_df['blank']


# best fit linear
comb_df.dropna(inplace = True)

fit_r = np.polyfit(comb_df['samp'], comb_df['res'],1)
comb_df['d_res'] = comb_df['res'] - (fit_r[0]*comb_df['samp']+fit_r[1])

# loess function
comb_df['loess_d_res'] = sm.nonparametric.lowess(comb_df['d_res'], comb_df['samp'], frac = .03, return_sorted = False)


# plot
csfont = {'fontname':'Microsoft Tai Le', 'fontsize':15}
plt.figure(figsize = (10,5))

plt.plot(comb_df['samp'], comb_df['d_res'], 'b.', alpha = .125)
plt.plot(comb_df['samp'], comb_df['loess_d_res'], 'b-')


plt.xlabel('Temperature (C)')
plt.ylabel('Residual Temperature (C)')

plt.show()


