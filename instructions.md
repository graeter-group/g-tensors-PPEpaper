# Preparing the system

create the initial model in an <model_name>/model.xyz file and run 
./basic_scripts/workflow.sh <model_name> that optimizes the configuration
and submit the calculation of the g-values.

Note: if you want to remove unnecessary files for this matter, you can execute
./basic_scripts/clean_directories.sh <directory>

to get the table of results as latex tables, execute:
python ./basic_scripts/create_tables.py <directory>

All the analysis are stored in [analysis](https://github.com/Sucerquia/g-tensor/tree/master/analysis) directory.
