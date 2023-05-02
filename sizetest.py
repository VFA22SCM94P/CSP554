import os


# program to check input file size . 
# because the EB volume on EMR cluseter has a limit.
# so this program tests if the file is under 400MB

filename = '/Users/vaishnavi/Downloads/charts_2.csv'
file_size = os.path.getsize(filename)

file_size_mb = file_size / (1024 * 1024)

if file_size_mb > 400:
    print(f"The file size greater than EBS volume .")
else:
    # pushtoHDFS();
    print(f"The File size acceptable, Pushed to HDFS.")
