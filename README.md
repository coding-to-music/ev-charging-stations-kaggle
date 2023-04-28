# ev-charging-stations-kaggle

# 🚀 Download via Kaggle API the EV Charging Stations dataset 🚀

https://github.com/coding-to-music/ev-charging-stations-kaggle


From / By 

## Environment variables:

https://github.com/Kaggle/kaggle-api

https://github.com/Kaggle/kaggle-api/blob/main/README.md

https://volkovlabs.io/blog/how-to-create-your-first-grafana-dashboard-bd0f68d631bd/

```java
kaggle.json is needed, see below

store in ~/.kaggle/kaggle.json
```

## GitHub

```java
git init
git add .
git remote remove origin
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:coding-to-music/ev-charging-stations-kaggle.git
git push -u origin main
```

## Get the dataset via the api

```
kaggle datasets download -d saketpradhan/electric-and-alternative-fuel-charging-stations
```

## Exploring Kaggle API Endpoints

After following the steps above, we can begin exploring the use of this package. I would be executing them in a Jupyter Notebook.

The Kaggle API offers the following endpoints with various commands:

```
Competitions {list, files, download, submit, submissions, leaderboard}
Datasets {list, files, download, create, version, init}
Kernels {list, init, push, pull, output, status}
Config {view, set, unset}
Competitions Endpoint
```

Suppose we would like to access the datasets of currently active competitions on Kaggle; we can do so with the following command.

```
!kaggle competitions list
```

Using the other commands, we can also check out the leaderboard scoring for a competition. For example, suppose we are interested to see the leaderboard for the “contradictory-my-dear-watson” competition.

```
!kaggle competitions leaderboard --show contradictory-my-dear-watson
```

We can also search for competitions with a keyword. For example, suppose we want to search for competitions related to finance.

```
!kaggle competitions list -s finance
```

To check the files associated with a competition dataset, we can use the following command.

```
!kaggle competitions files titanic
```

To explore more endpoints, use the following command.

```
!kaggle competitions -h
```

Datasets Endpoint

Similar to the competitions endpoints, we can also obtain datasets using the datasets endpoint. Thus, we would replace the competition with datasets.

```
!kaggle datasets list
```

We can also sort the datasets by most active and last updated.

```
!kaggle datasets list --sort-by active
```

To explore more endpoints, use the following command.

```
!kaggle datasets -h
```

Downloading, Unzipping and Reading Kaggle Datasets

Finally, we can also download the files associated with a competition or dataset. For example, suppose I am interested in downloading the files for “Reddit Vaccine Myth”.

Firstly, obtain the reference of the dataset. For Reddit Vaccine Myth, we can see that the reference for the dataset is: `gpreda/reddit-vaccine-myths`

```
!kaggle datasets list
```

Once we have the dataset’s reference, we can download the files using the following command.

```
!kaggle datasets download gpreda/reddit-vaccine-myths
```

By default, the files would be downloaded into your current working Python script directory in a ZIP file.

To extract a ZIP file, use the following function.

```
from zipfile import ZipFile
  
with ZipFile('reddit-vaccine-myths.zip', 'r') as zip:
    zip.printdir()
    zip.extractall()
```

Once that’s done, read in your files!

```
import pandas as pd
df = pd.read_csv("reddit_vm.csv")
df.head()
```

Simple as that! Once set up, this would likely help streamline the model building processing by obtaining and reading data directly from Kaggle.

The complete documentation can be found: Kaggle.https://github.com/Kaggle/kaggle-api

## Columns in the data file

```
 1 Fuel Type Code,
 2 Station Name,
 3 Street Address,
 4 Intersection Directions,
 5 City,
 6 State,
 7 ZIP,
 8 Plus4,
 9 Station Phone,
10 Status Code,
11 Expected Date,
12 Groups With Access Code,
13 Access Days Time,
14 Cards Accepted,
15 BD Blends,
16 NG Fill Type Code,
17 NG PSI,
18 EV Level1 EVSE Num,
19 EV Level2 EVSE Num,
20 EV DC Fast Count,
21 EV Other Info,
22 EV Network,
23 EV Network Web,
24 Geocode Status,
25 Latitude,
26 Longitude,
27 Date Last Confirmed,
28 ID,
29 Updated At,
30 Owner Type Code,
31 Federal Agency ID,
32 Federal Agency Name,
33 Open Date,
34 Hydrogen Status Link,
35 NG Vehicle Class,
36 LPG Primary,
37 E85 Blender Pump,
38 EV Connector Types,
39 Country,
40 Intersection Directions (French),
41 Access Days Time (French),
42 BD Blends (French),
43 Groups With Access Code (French),
44 Hydrogen Is Retail,
45 Access Code,
46 Access Detail Code,
47 Federal Agency Code,
48 Facility Type,
49 CNG Dispenser Num,
50 CNG On-Site Renewable Source,
51 CNG Total Compression Capacity,
52 CNG Storage Capacity,
53 LNG On-Site Renewable Source,
54 E85 Other Ethanol Blends,
55 EV Pricing,
56 EV Pricing (French),
57 LPG Nozzle Types,
58 Hydrogen Pressures,
59 Hydrogen Standards,
60 CNG Fill Type Code,
61 CNG PSI,
62 CNG Vehicle Class,
63 LNG Vehicle Class,
64 EV On-Site Renewable Source,
65 Restricted Access
```

## Target columns

 1 Fuel_Type_Code           varchar(400) NULL,
 2 Station_Name             varchar(400) NULL,
 3 Street_Address           varchar(400) NULL,
 5 City                     varchar(400) NULL,
 6 State                    varchar(400) NULL,
 7 ZIP                      varchar(400) NULL,
 8 Plus4                    varchar(400) NULL,
10 Status_Code              varchar(400) NULL,
12 Groups_With_Access_Code  varchar(400) NULL,
13 Access_Days_Time         varchar(400) NULL,
25 Latitude                 varchar(400) NULL,
48 Facility_Type            varchar(400) NULL,
26 Longitude                varchar(400) NULL


## The new .csv file should look like this

create table ev_locations
(
Fuel_Type_Code           varchar(400) NULL,
Station_Name             varchar(400) NULL,
Street_Address           varchar(400) NULL,
City                     varchar(400) NULL,
State                    varchar(400) NULL,
ZIP                      varchar(400) NULL,
Plus4                    varchar(400) NULL,
Status_Code              varchar(400) NULL,
Groups_With_Access_Code  varchar(400) NULL,
Access_Days_Time         varchar(400) NULL,
Latitude                 varchar(400) NULL,
Facility_Type            varchar(400) NULL,
Longitude                varchar(400) NULL
);

## How to cut columnns from the .csv and put the desired columns into a new file

You can use the cut command to extract specific columns from your CSV file and then use paste command to combine those columns into a new CSV file. Here's an example command that you can use:

```
cut -d',' -f1,3,5,7,9 original_file.csv | paste -sd ',' > new_file.csv
```

This command extracts columns 1, 3, 5, 7, and 9 from original_file.csv using the comma (,) delimiter and then combines them using the comma delimiter as well to create a new file called new_file.csv.

You can change the column numbers according to your needs, and the delimiter can be changed to a different character if needed.

## use cut to create the file to be loaded

```
# this leaves the header row in the file
cut -d',' -f1,2,3,5,6,7,8,10,12,13,25,48,26 Electric-and-Alternative-Fuel-Charging-Stations.csv | paste -sd ',' > ev_locations.csv

cut -d',' -f1,2,3,5,6,7,8,10,12,13,25,48,26 original.csv | paste -sd ',' > original-1.csv
```

```
# this removes the header row from the file
tail -n +2 Electric-and-Alternative-Fuel-Charging-Stations.csv | cut -d',' -f1,2,3,5,6,7,8,10,12,13,25,48,26  | paste -sd ',' > ev_locations.csv

tail -n +2 original.csv | cut -d',' -f1,2,3,5,6,7,8,10,12,13,25,48,26  | paste -sd ',' > original-2.csv
```

## another attempt to cut columns from the csv and put them into a new csv

```
awk -F ',' '{print $1 "," $3 "," $5 "," $7 "," $9}' original_file.csv > new_file.csv

cut -d',' -f1,2,3,5,6,7,8,10,12,13,25,48,26 original.csv | paste -sd ',' > original-1.csv

awk -F ',' '{print $1 "," $2 "," $3 "," $5 "," $6 "," $7 "," $8 "," $10 "," $12 "," $13 "," $25 "," $48 "," $26 }' original.csv > original-4.csv
```

This command tells awk to use comma as the field separator (-F ',') and then print the 1st, 3rd, 5th, 7th, and 9th fields separated by commas. The output is then redirected to a new file named new_file.csv.

Note that you can modify the column numbers in the {print ...} statement to extract the columns you need.

Also, if your original file has a header row, you can exclude it from the output by adding NR>1 && before the {print ...} statement. This tells awk to only perform the action on lines with a line number (NR) greater than 1.

## I have a .csv file. How do I cut the first row (column headers) and only keep the rows with data? 

You can use the tail command in Linux to remove the first row of the CSV file and then redirect the output to a new file. Here's an example command:

```
tail -n +2 input.csv > output.csv

tail -n +2 original.csv > original-3.csv
```

Explanation:

- tail command is used to output the last part of a file.
- -n option is used to specify the number of lines to be displayed.
- +2 means to start from the second line of the file.
- input.csv is the name of the input file.
- > is used to redirect the output to a new file called output.csv.

This command will remove the first row (column headers) from the input.csv file and write the remaining rows (data) to a new file called output.csv.

## How would I view the header row?

If you want to view the header row of a CSV file, you can use the head command in Linux to display the first few lines of the file. Here's an example command:

```
head -n 1 input.csv

head -n 1 original.csv
head -n 1 original-1.csv
head -n 1 original-2.csv
head -n 1 original-3.csv
head -n 1 original-4.csv
```

Explanation:

- head command is used to output the first part of a file.
- -n option is used to specify the number of lines to be displayed. In this case, we want to display only the first line.
- 1 means the first line of the file.
- input.csv is the name of the input file.
- This command will display the header row (first line) of the input.csv file.

## How would I count the columns in the header row or the body?

To count the number of columns in the header row or the body of a CSV file in Linux, you can use the awk command. Here are the examples:

Counting the number of columns in the header row:

```
head -n 1 input.csv | awk -F ',' '{print NF}'

head -n 1 original.csv | awk -F ',' '{print NF}'
head -n 1 original-1.csv | awk -F ',' '{print NF}'
head -n 1 original-2.csv | awk -F ',' '{print NF}'
head -n 1 original-3.csv | awk -F ',' '{print NF}'
head -n 1 original-4.csv | awk -F ',' '{print NF}'
```

Explanation:

- head -n 1 input.csv command is used to extract the first row (header row) of the CSV file.
- awk command is used to split the header row into columns using , as the delimiter and count the number of columns.
- -F ',' option is used to specify the delimiter as ,.
- {print NF} prints the number of columns.

This command will output the number of columns in the header row of the input.csv file.

Counting the number of columns in the body:

```
awk -F ',' '{print NF; exit}' input.csv

awk -F ',' '{print NF; exit}' original.csv
awk -F ',' '{print NF; exit}' original-1.csv
awk -F ',' '{print NF; exit}' original-2.csv
awk -F ',' '{print NF; exit}' original-3.csv
awk -F ',' '{print NF; exit}' original-4.csv
```

Explanation:

awk command is used to split the rows in the CSV file into columns using , as the delimiter and count the number of columns in the first row only.

- -F ',' option is used to specify the delimiter as ,.
- {print NF; exit} prints the number of columns in the first row and then exits.

This command will output the number of columns in the body of the input.csv file. Note that this assumes that all the rows in the file have the same number of columns.

## Count the number of rows in the csv file

```
wc -l original.csv
wc -l original-1.csv
wc -l original-2.csv
wc -l original-3.csv
wc -l original-4.csv
```


