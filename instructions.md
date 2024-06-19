# Instructions to use this repository

create the initial model in a <model_name>/model.xyz file. In this case, we
created all the configurations using the script Createmodel.py in each one of
the directories. Once the model is created, run the script 
./basic_scripts/workflow.sh <model_name> that optimizes the configuration
and submit the calculation of the g-values.

The main scripts are in [basic_scripts](https://github.com/Sucerquia/g-tensor/tree/master/basic_scripts).
Mainly the input -orca and gaussian- scripts.

The script of the plot included in the paper is stored in
[analysis](https://github.com/Sucerquia/g-tensor/tree/master/analysis) directory.
