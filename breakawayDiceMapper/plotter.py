import matplotlib.pyplot as plt
import numpy as np
import glob
import sys
import os

def get_filepaths():    
    patterns = sys.argv[1:]
    try:
        globs = [glob.glob(pattern) for pattern in patterns]
        return list(set(sum(globs, [])))
    except Exception as e:
        print('Error parsing pattern: {}'.format(repr(e)))
        quit()

def extract_file_data(filepath):
    '''extracts data from csv file'''
    # Read data
    with open(filepath, 'r') as datafile:
        lines = datafile.readlines()

    # Cut metadata
    cutoff = None
    for i, line in enumerate(lines):
        if line == '\n':
            cutoff = i
            break
    lines = lines[:cutoff]

    # Strip x-axis title and labels
    x_title = lines[0].replace('\n', '').replace('\t', '')
    x_labels = lines[1].replace('\n', '').split('\t')[2:]
    lines = lines [2:]

    # Make data into matrix
    lines = [line.replace('\n', '').split('\t') for line in lines]

    # transpose, strip y-axis title and lables and re-transpose
    lines = list(map(list, zip(*lines)))
    y_title = ''.join(lines[0])
    y_labels = lines[1]
    lines = lines[2:]
    data = list(map(list, zip(*lines)))

    # Convert data to numeric values
    data = [[float(value) for value in row] for row in data]
    return {
        "x_title":x_title,
        "y_title":y_title,
        "x_labels":x_labels,
        "y_labels":y_labels,
        "data":data
    }


def plot_bulk_data(bulk_data):
    '''plots bulk data as subplots'''
    for name in bulk_data:
        chart_info = bulk_data[name]

        fig, ax = plt.subplots()
        im = ax.imshow(chart_info['data'])

        # We want to show all ticks...
        ax.set_xticks(np.arange(len(chart_info['x_labels'])))
        ax.set_yticks(np.arange(len(chart_info['y_labels'])))
        # ... and label them with the respective list entries
        ax.set_xticklabels(chart_info['x_labels'])
        ax.set_yticklabels(chart_info['y_labels'])

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                rotation_mode="anchor")

        # Loop over data dimensions and create text annotations.
        for i in range(len(chart_info['x_labels'])):
            for j in range(len(chart_info['y_labels'])):
                text = ax.text(j, i, "{:.2f}".format(chart_info['data'][i][j]),
                            ha="center", va="center", color="w")

        ax.set_title(name)
        ax.set_xlabel(chart_info['x_title'])
        ax.set_ylabel(chart_info['y_title'])
        fig.tight_layout()


        
        # Make output directory
        if not os.path.isdir('plots'):
            os.mkdir('plots')
        filepath = os.path.join('plots', '{}.png'.format(name.replace(' | ', '-')))
        plt.savefig(filepath)




def main():
    # Check inputs
    if len(sys.argv) <= 1:
        print('Please provide one or more unix style pathname patterns')
        print('\te.g. `bpm-plot *.csv`')
        quit()

    # Get filepaths and extract data from files
    bulk_data = {}
    filepaths = get_filepaths()
    for filepath in filepaths:
        name = ' | '.join(os.path.basename(filepath).split('.')[0].split('-')[2:])
        bulk_data[name] = extract_file_data(filepath)

    # Run plotter
    plot_bulk_data(bulk_data)


if __name__ == "__main__":
    main()

