import argparse
from supervisor import runScenario
from csvWriter import write_csv

def main():
    '''
        To run:
        python __main__.py
    '''
    parser = argparse.ArgumentParser(description='Compute dice roll percentages.')
    parser.add_argument('--output', required=True, nargs='?', type=str, help='an integer for the accumulator')
    parser.add_argument('--legacy', action='store_true', help='use legacy roll mechanic')
    parser.add_argument('--verbose', action='store_true', help='verbose output')
    args = parser.parse_args()

    legacy  = args.legacy
    output_filename = args.output
    verbose = args.verbose

    # Scenarios
    playerDiceArray = [1,2,3,4,5,6,7,8]
    dmDiceArray = [1,2,3,4,5,6,7,8]
    face = 6

    #Supervisor runs sims
    data = runScenario(playerDiceArray, dmDiceArray, face, verbose, legacy)

    #Csv writer exports data    
    write_csv(data=data, filename=output_filename)

if __name__ == "__main__":
    main()