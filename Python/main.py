import os
import glob
from natsort import natsorted

import tkinter as tk
from tkinter import filedialog

from pandas import *

import matplotlib.pyplot as plt
import numpy as np

color_palette = ["#0173B2", "#DE8F05", "#029E73", "#D55E00", "#CC78BC","#CA9161", "#FBAFE4", "#949494", "#ECE133", "#56B4E9","#0173B2", "#DE8F05", "#029E73", "#D55E00", "#CC78BC","#CA9161", "#FBAFE4", "#949494", "#ECE133", "#56B4E9","#0173B2", "#DE8F05", "#029E73", "#D55E00", "#CC78BC","#CA9161", "#FBAFE4", "#949494", "#ECE133", "#56B4E9","#0173B2", "#DE8F05", "#029E73", "#D55E00", "#CC78BC","#CA9161", "#FBAFE4", "#949494", "#ECE133", "#56B4E9","#0173B2", "#DE8F05", "#029E73", "#D55E00", "#CC78BC","#CA9161", "#FBAFE4", "#949494", "#ECE133", "#56B4E9"]


SMALL_SIZE = 15
MEDIUM_SIZE = 20
BIGGER_SIZE = 20

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
plt.rc('axes', titleweight='bold')       # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


class Liquid:
    def __init__(self, name, n, y):
        self.name = name
        self.n = n # dynamic viscosity [Ns/m**2]    https://www.engineeringtoolbox.com/absolute-viscosity-liquids-d_1259.html
        self.y = y # surface tension  [N/m]        http://www.surface-tension.de/ 


liquid_water = Liquid(name='water',
                     n = 0.00089,
                     y = 72.80e-3)

liquid_milk = Liquid(name='milk',
                     n = 0.003,
                     y = 72.80e-3)

liquid_olive_oil = Liquid(name='olive oil',
                     n = 10e-1,
                     y = 29.75e-3) # http://www.surface-tension.org/news/61.html

liquid_ethanol = Liquid(name='ethanol',
                     n = 0.001095,
                     y = 22.39e-3)

liquid_methanol = Liquid(name='methanol',
                     n = 0.00056,
                     y = 22.50e-3)

class Paper:
    def __init__(self, name , pore_size):
        self.name = name
        self.pore_size = pore_size # [m]

paper_what_grad_1 = Paper(name='Whatman Grade 1',
                     pore_size=11e-6)

paper_what_grad_2 = Paper(name='Whatman Grade 2', 
                     pore_size=8e-6)


paper_what_grad_3 = Paper(name='Whatman Grade 3',
                     pore_size=6e-6)

paper_what_grad_4 = Paper(name='Whatman Grade 4',
                     pore_size=22e-6)

paper_what_grad_5 = Paper(name='Whatman Grade 5',
                     pore_size=2.5e-6)

paper_what_grad_6 = Paper(name='Whatman Grade 6',
                     pore_size=3e-6)

paper_1um = Paper(name='Whatman Grade 6',
                     pore_size=1e-6)
                     
def select_csv_file():
    print("Select .csv file:")
    csv_file = filedialog.askopenfilename()
    print("Selected .csv file: {}".format(csv_file))
    print("")
    return csv_file

def set_header_row_nr():
    header_row = input("Set the header-row-number: ")
    print("Header row set to: {}".format(header_row))
    print("")
    # do minus 1 because python starts counting from zero
    header_row = int(header_row) - 1
    return int(header_row)

def get_header_values(file, header_row_nr):
    '''
    Sets header_values 
    header_values look like: [Time(s),I(A),U(V),...]
    we find the header_values by using the header_row_nr
    '''
    print("set_header_values was executed")
    with open(file, "r") as f:
        for x, line in enumerate(f):
            if x == header_row_nr:
                # print(line)
                header_list = line.split(",")
                break
    print(header_list)
    return header_list

def select_column_by_name(header_values, message):
    index = 0
    for header in header_values:
        print("({}) - {}".format(index, header))
        index = index + 1
    selected_index = int(input(message))
    selected_header = header_values[selected_index]
    print("Selected column with header: {}".format(selected_header))
    print("")
    return selected_index

def read_single_column_from_csv_file(csv_file,header_row_nr,column_number):
    '''
    returns the column in a numpy array
    '''
    col_data = pandas.read_csv(csv_file, sep=',', header = header_row_nr, usecols=[column_number],encoding = "ISO-8859-1")
    col_data_np_array = col_data.as_matrix()

    return col_data_np_array

def read_multiple_columns_from_csv_file(csv_file,header_row_nr,use_cols):
    '''
    returns the column in a numpy array
    '''
    col_data = pandas.read_csv(csv_file, sep=',', header = header_row_nr, usecols=use_cols,encoding = "ISO-8859-1")
    col_data_np_array = col_data.as_matrix()

    return col_data_np_array

def get_filename(full_filepath):
    '''
    Get the filename by using the full_filepath
    '''
    filename = os.path.basename(full_filepath)
    return filename


def washburn_eq(L, liquid, paper):
    # L = distance to travel
    # n = viscosity
    # D = pore size
    # y = surface tension

    # This function returns the time it takes for a fluid to travel L
    n = liquid.n
    y = liquid.y
    D = paper.pore_size

    t = (L**2 * 4 * n) / (y*D) 
    return t

data_file = 'ArduinoData_Jordi_Jaspers.csv' # select_csv_file()

header_row_nr = 0 # set_header_row_nr()

time_col = read_single_column_from_csv_file(data_file,header_row_nr,0)
time_col = np.cumsum(time_col)/1000

# drop noisy data at the end
end_time = 235

end_index = min(range(len(time_col)), key=lambda i: abs(time_col[i]-end_time))

time_col = time_col[0:end_index]

data_col = read_multiple_columns_from_csv_file(data_file,header_row_nr,[1,2,3,4,5,6])
data_col = data_col[0:end_index]
print(type(data_col))
print(data_col.shape)


ax = plt.subplot(1,2,1)

ax.set_title('Capsense readout') # Title
ax.set_ylabel('Amplitude') # Y label
ax.set_xlabel('Time (s)') # X label

ax.plot(time_col, data_col, '.', color=color_palette[0], alpha=0.5)

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

# Bad idea
# Map all data between 1 and 100
# i = 0
# for column in data_col.T:
#     max_value = np.amax(column)
#     print(max_value)
#     plt.figure(1)
#     plt.plot(time_col, (column/max_value)*100, '.', color=color_palette[1], alpha=0.5)


# Better idea
# Find center datapoint

intersect_time_array = np.array([])

i = 0
for column in data_col.T:
    max_value = np.amax(column)
    min_value = np.amin(column)

    center_value = (min_value + max_value)/2

    center_value_index = min(range(len(column)), key=lambda i: abs(column[i]-center_value))
    
    print('Center value = {}'.format(center_value))

    plt.figure(1)

    time_point = time_col[center_value_index]
    intersect_time_array = np.append(intersect_time_array, time_point)

    plt.plot(time_point, center_value, 'o', markersize='10', color=color_palette[1], alpha=1)


distance_array = np.array([1,2,3,4,5,6]) # in cm

ax2 = plt.subplot(1,2,2)

ax2.set_title('Elapsed time per traveled distance') # Title
ax2.set_ylabel('Elapsed time (s)') # Y label
ax2.set_xlabel('Distance (cm)') # X label


# Hide the right and top spines
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax2.yaxis.set_ticks_position('left')
ax2.xaxis.set_ticks_position('bottom')

plt.plot(distance_array, intersect_time_array, '--o', markersize='10', color=color_palette[0], alpha=1, label='tap water')


# Plot curves for different liquids

distance_array_in_meters = distance_array/100
times_for_water = washburn_eq(distance_array_in_meters, liquid_water, paper_what_grad_1)
times_for_milk = washburn_eq(distance_array_in_meters, liquid_milk, paper_what_grad_1)
times_for_ethanol = washburn_eq(distance_array_in_meters, liquid_ethanol, paper_what_grad_1)
times_for_methanol = washburn_eq(distance_array_in_meters, liquid_methanol, paper_what_grad_1)

# times_for_water2 = washburn_eq(distance_array_in_meters, liquid_water, paper_what_grad_5)
# times_for_milk2 = washburn_eq(distance_array_in_meters, liquid_milk, paper_what_grad_5)
# times_for_ethanol2 = washburn_eq(distance_array_in_meters, liquid_ethanol, paper_what_grad_5)
# times_for_methanol2 = washburn_eq(distance_array_in_meters, liquid_methanol, paper_what_grad_5)

plt.plot(distance_array, times_for_water, '--o', markersize='10', color=color_palette[0], alpha=1, label = liquid_water.name + ' - grade 1' )
plt.plot(distance_array, times_for_milk, '--o', markersize='10', color=color_palette[1], alpha=1 ,label = liquid_milk.name + ' - grade 1' )
plt.plot(distance_array, times_for_ethanol, '--o', markersize='10', color=color_palette[2], alpha=1, label = liquid_ethanol.name + ' - grade 1' )
plt.plot(distance_array, times_for_methanol, '--o', markersize='10', color=color_palette[3], alpha=1, label = liquid_methanol.name + ' - grade 1' )

# plt.plot(distance_array, times_for_water2, '--^', markersize='10', color=color_palette[0], alpha=1, label = liquid_water.name + ' - grade 5'  )
# plt.plot(distance_array, times_for_milk2, '--^', markersize='10', color=color_palette[1], alpha=1 ,label = liquid_milk.name + ' - grade 5'  )
# plt.plot(distance_array, times_for_ethanol2, '--^', markersize='10', color=color_palette[2], alpha=1, label = liquid_ethanol.name + ' - grade 5' )
# plt.plot(distance_array, times_for_methanol2, '--^', markersize='10', color=color_palette[3], alpha=1, label = liquid_methanol.name + ' - grade 5' )

ax2.legend()

plt.show()

