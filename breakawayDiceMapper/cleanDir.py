import os 
import glob


def clean_current_dir():    
    globs = [
        glob.glob('output/*.png'),
        glob.glob('plots/*.csv'),
    ]
    filepaths = list(set(sum(globs, [])))

    for filepath in filepaths:
        os.remove(filepath)



def main():
    clean_current_dir()


if __name__ == "__main__":
    main()
