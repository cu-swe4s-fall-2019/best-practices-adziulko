# best-practices
The purpose of this software is so that students can
1. Practice python Pep8 standards using 'pycodestyle'
2. Practice best practices in 'get_column_stats.py'
3. Practice testing code using bash script

The actual function of these files is to:
1. Calculate mean and standard deviation of tab separated input file
2. Run tests through bash script

# File instruction
To test for python Pep8 style, you will need to:
1. Install pycodestyle
2. Run pycodestyle on desired file (in this case it is 'style.py')
```
pip install pycodestyle
pycodestyle style.py
```

To calculate the mean and standard deviation of a tab separated input file, you will need to:
1. Have python installed
2. In command line, input the file name and column number you wish to run calculations on (example shown below)
    (note that the first column of a file is '0' in python3)
```
python get_column_stats.py --file_name test_file.txt --column_number 0
```

To run test on 'get_column_stats.py', you can run the 'basic_test.sh' file:
```bash basic_test.sh```
