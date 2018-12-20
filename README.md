# Breakaway Dice Mapper
A dice probability sim for the development of [hit Sci-Fi Tabletop RPG Breakaway](http://www.breakaway.pub/)

## Installation
1. Git clone
2. Enter Breakaway-Dice-Mapper directory
3. pip install .

## Dev Installation
1. Git clone
2. Enter Breakaway-Dice-Mapper directory
3. pip install -e .

## Run sim
+ Create a `config.json` file. An example format can be found by running `bdm --example-config`
+ Run `bdm --config config.json`
+ Data will be stored in `./outputs`

## Plot all output CSV files
+ run `bdm-plot output/*.csv`
+ Plots will be stored in `./plots`

## Clean all CSV and PNG files
+ run `bdm-clean`