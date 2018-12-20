import os

def write_csv(data, job, filename):
    # Make output directory
    if not os.path.isdir('output'):
        os.mkdir('output')
    filename = os.path.join('output', filename)

    with open(filename, 'w') as csv:
        rows = len(data)
        cols = len(data[list(data.keys())[0]])

        # Build horiz_key
        horiz_key = ['' for x_ in range(cols+2)]
        horiz_key[cols//2] = 'DM Rolls'
        csv.write('\t'.join(horiz_key) + '\n')

        # Build vert_key
        vert_key = ['' for x_ in range(rows+2)]
        vert_key[rows//2] = 'Player Rolls'

        # Extract data and write to file
        for i, player_roll in enumerate(data):
            if i == 0:
                row = ['', ''] + [str(x) for x in data[player_roll]]
                csv.write('\t'.join(row)+'\n')

            row = [vert_key[i], str(player_roll)]
            for dm_roll in data[player_roll]:
                win_percentage = data[player_roll][dm_roll]
                row.append(str(win_percentage))
            csv.write('\t'.join(row)+'\n')

        # Write info section
        csv.write('\n\n')
        csv.write('Model Name:\t{}\n'.format(job["model"]))
        csv.write('Calculated statistic:\t{}\n'.format(job["output_stat"]))
        csv.write('Dice:\tD{}\n'.format(job["face"]))
        csv.write('\n\nDescription:\n')

        description = job["description"].split('\n')
        for line in description:
            csv.write('\t{}\n'.format(line))

