import argparse
from breakawayDiceMapper.supervisor import runScenario
from breakawayDiceMapper.csvWriter import write_csv
from breakawayDiceMapper.configParser import print_example_config, parse_config


def main():
    '''
        To run:
        python __main__.py
    '''
    parser = argparse.ArgumentParser(description='Compute dice roll percentages.')
    parser.add_argument('--config', help='config JSON file. See example file by running `bdm --example-config`')
    parser.add_argument('--verbose', action='store_true', help='verbose output')
    parser.add_argument('--example-config', action='store_true', help='print example config.JSON file')

    args = parser.parse_args()


    # Check if requesting example
    if args.example_config:
        print_example_config()
        quit()
    elif args.config:
        jobs = parse_config(args.config)
        verbose = args.verbose

        # Load scenarios
        for name in jobs:
            job = jobs[name]
            playerDiceArray = job["player_dice"]
            dmDiceArray = job["dm_dice"]
            face = job["face"]
            stat = job["output_stat"]
            model = job["model"]
            description = job["description"]

            #Supervisor runs sims
            data = runScenario(
                player_dice=playerDiceArray, 
                dm_dice=dmDiceArray, 
                face=face, 
                stat=stat, 
                model=model,
                verbose=verbose
            )

            #Csv writer exports data    
            write_csv(data=data, job=job, filename=name)
        quit()
    else:
        print("Invalid syntax, please run `bdm --help`")
        quit()

if __name__ == "__main__":
    main()