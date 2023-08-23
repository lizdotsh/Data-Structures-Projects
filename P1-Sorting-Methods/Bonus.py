import re 
import os
import functools as ft
from plotnine import ggplot, geom_point, aes, geom_line, labs, facet_wrap, theme
import patchworklib as pw
import pandas as pd

# PARAMS
ARRAY_SIZE_LIST = [10000, 20000, 30000, 40000, 50000]
ORDER_TYPE_LIST = ['random', 'increasing', 'decreasing']

def unpack_and_reduce(list_regex:str, start, end):
	"""
	takes the following arguments; 

	1. list of lists where each sub list is either blank or with a single regex'd number in string form
	2. bounds for adding up from said list
	uses functool's reduce() to do the following: 
		a. start with original of 0
		b. take element of list and check if it is empty (filtered_list has nested everything, so [])
		c. if it is empty, return x (sum of everything up to this point
		d. if not, select the first element of the list item, convert it to an integer, and add it to x (starts at zero))
		e. repeat steps a-d but with the result of d instead of zero, repeat until all are added. 
	"""
	return ft.reduce(
		lambda x, y: x + int(y[0]) if(y != []) else x, 
		list_regex[start:end], 0
		) 

def process_cover_file(file:str = 'sort.cover', duplicate_row = 8, bounds:dict = {
	'insertion': {'start': 4, 'end': 12},
	'selection': {'start': 14, 'end': 16} }) -> list[int]:
	"""
	1. Uses regex and re.findall to isolate the numbers in every line of the file specified 
	2. saves this as a variable and subsets only the relevant lines 
	3. feeds to unpack_and_reduce for each of the algorithsms
	"""
	filtered_list = [
		re.findall(r'^\s*(\d+):',line)
		for line in open(file)
	]
	filtered_list[duplicate_row][0] = str(
		int(filtered_list[duplicate_row][0]) * 2
	)
	return {
		st:unpack_and_reduce(filtered_list, bounds[st]['start'], bounds[st]['end'])
		for st in bounds.keys() 
	}

def run_sort_script(size_of_array:int, array_type:str, script_path:str = 'Sort.py') -> list:
	"""
	A simple function that takes 3 arguments: 
	
		size_of_array: integer of the length of the array to be sorted 
		array_type: if the array is random, increasing, or decreasing
		script_path: path to Script.py
	Takes these arguments and runs a python shell command with trace enabled with the arguments above. 
	This creates a new sort.cover, so the function runs process_cover_file() to scrape and add those numbers
	It then returns the result of process_cover_file
	"""
	print(array_type)
	print(size_of_array)
	command = f"python -m trace --count -C . {script_path} {size_of_array} {array_type}"
	print('now running', command)
	os.system(command)
	return process_cover_file(
		file = 'sort.cover', 
		bounds = {
			'insertion': {'start': 4, 'end': 13},
			'selection': {'start': 14, 'end': 26}
		})

def run_all_permutations(
	array_size_list:list = ARRAY_SIZE_LIST,
	order_type_list:list = ORDER_TYPE_LIST,
	csv_path:str = 'size_type_df.csv'
	):
	size_type_df = pd.merge(
		pd.Series(array_size_list, name = 'array_size'),
		pd.Series(order_type_list, name = 'order_type'),
		how = 'cross'
	)
	size_type_df[['insertion', 'selection']] = size_type_df.apply(
		lambda row: run_sort_script(row[0], row[1]),
		axis = 1, 
		result_type='expand'
	) 
	size_type_df = size_type_df.melt(id_vars = ['array_size', 'order_type'], value_vars = ['insertion', 'selection'],
	var_name='sort_type', value_name='num_operations')
	size_type_df.to_csv(csv_path)
	return size_type_df

def make_plot(df:pd.DataFrame, details:dict = {'random': {"x":'hi', "title" : 'random'}}):
	"""
	makes plot. input
	1. Dataframe
	2. dictionary, second level gets put into each plot's labs() using kwargs**
	"""
	base_plots = {name:(
	ggplot(df.query(f"order_type == '{name}'"), aes(x = 'array_size', y = 'num_operations', color = 'sort_type'))
		+ geom_point()
		+ geom_line()
		+ labs(**details[name])
		) for name in details	
	}
	return_dict = {}
	for elm in base_plots.keys():
		g1 = pw.load_ggplot(base_plots[elm] + theme(legend_position='none', figure_size=(5,4)) + labs(caption = ""))
		g2 = pw.load_ggplot(base_plots[elm] + facet_wrap('sort_type', ncol = 1, nrow = 2, scales = 'free_y') + theme(figure_size = (2,4), legend_position = 'none')+labs(title = ""))
		return_dict[elm] = (g1|g2)
	return return_dict

if __name__ == '__main__':
	size_type_df = run_all_permutations()
	#size_type_df = pd.read_csv('size_type_df.csv') #Testing
	print(size_type_df)
	plot_details = {
		"random" : {
			'x' : 'Size of Array',
			'y' : 'Number of Operations (Millions)',
			'title' : 'Random Array',
			'caption': 'Made by Elizabeth Goodwin'
		},
		"increasing" : {
			'x' : 'Size of Array', 
			'y' : 'Number of Operations (Millions)',
			'title' : 'Increasing Array',
			'caption' : 'Made by Elizabeth Goodwin'
		},
		"decreasing" : {
			'x' : 'Size of Array', 
			'y' : 'Number of Operations (Thousands)',
			'title' : 'Decreasing Array',
			'caption': 'Made by Elizabeth Goodwin'
		}
	}
	size_type_df['num_operations'] = size_type_df['num_operations']/1000000
	plots = make_plot(size_type_df, plot_details)
	pw.param["margin"] = 0.2
	for p in plots.keys(): plots[p].savefig(f'{p}_plot.pdf')



