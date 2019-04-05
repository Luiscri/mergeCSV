# mergeCSV

mergeCSV is a little script which allows you to merge different CSV files located on the same directory. These files must have the same **header** and **separator**, otherwise you will get an error when trying to read the generated file.

In the following lines we will describe how to use this tool.

## Usage

mergeCSV has just one file, composed by a single method which you will need to run. In order to use it, you will have to import it first to your project.

```
import mergeCSV as mgcsv

source_directory_path = ...
output_file = ...
mgcsv.mergeCSV(source_directory_path, output_file)
```

As you can see the `mergeCSV()` method receives two different arguments:
1. source_directory_path: the path to the directory containing the CSV files you want to merge.
2. output_file: the path to the output file you want to save the data in.

## Saving different directories to the same file

By default, mergeCSV deletes the previous output file in case it exists everytime it is called. If you want to merge CSV files located on different directories you will have to remove the following lines from `mergeCSV.py` file:

```
try:
    os.remove(output_file)
except OSError:
    pass
```



