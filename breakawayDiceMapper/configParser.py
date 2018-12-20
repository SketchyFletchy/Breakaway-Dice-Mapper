import json
from breakawayDiceMapper.models import models 

DEFAULT_CONFIG = {
    "player_dice":"1:5",
    "dm_dice":"1:5",
    "dice_face_count":"6:6",
    "project_name":"output",
    "output_stats":[
        "win_percentage",
        "average_drawn_dice_per_checks"
    ],
    "models":list(models.keys())
}


def print_example_config():
    print(json.dumps(DEFAULT_CONFIG, indent=4))
    print('Range syntax is: <start>:<stop> or optionally <start>:<stop>:<step>')

def extract_range(key, config):
    try:
        string = config[key]
        range_vals = list(map(lambda x: int(x), string.split(":")))
        range_vals[1] += 1
        return range(*range_vals)
    except Exception as e:
        print("Could not parse range for {}: {}".format(key, repr(e)))

def parse_config(filename):
    # Get config and apply defaults for missing values
    config = DEFAULT_CONFIG
    with open(filename, 'r') as f:
        input_config = json.load(f)
    config.update(input_config)

    # Extract data iterators and vars
    dice_faces = extract_range("dice_face_count", config)
    player_dice = extract_range("player_dice", config)
    dm_dice = extract_range("dm_dice", config)
    output_stats = config["output_stats"]
    project_name = config["project_name"]
    selected_models = config["models"]

    # Construct jobs
    jobs = {}
    player_dice = [x for x in player_dice]
    dm_dice = [x for x in dm_dice]

    for model in selected_models:
        for face in dice_faces:
            for output_stat in output_stats:
                name = "{project}-{player_dice_count}x{dm_dice_count}-D{face}-{stat}-{model}.csv".format(
                    project=project_name,
                    player_dice_count=len(player_dice),
                    dm_dice_count=len(dm_dice),
                    face=face,
                    stat=output_stat,
                    model=model
                )
                jobs[name] = {
                    "face":face,
                    "player_dice":player_dice,
                    "dm_dice":dm_dice,
                    "output_stat":output_stat,
                    "model":model,
                    "description":models[model].__doc__
                }
    return jobs