# ev-charging-stations-kaggle

# 🚀 Download via Kaggle API the EV Charging Stations dataset 🚀

https://github.com/coding-to-music/ev-charging-stations-kaggle


From / By 

https://www.youtube.com/watch?v=HNCKbGfAU0Q&ab_channel=VolkovLabs

https://github.com/Kaggle/kaggle-api

https://github.com/Kaggle/kaggle-api/blob/main/README.md

https://volkovlabs.io/blog/how-to-create-your-first-grafana-dashboard-bd0f68d631bd/

## Environment variables:

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

```
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
```


## The new .csv file should look like this

```
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
```

## Remove the header row

```
tail -n +2 original.csv > original-1.csv
```

## use csvkit because it can handle quotes around the address field which itself contains commas

```
pip install csvkit
```

```
csvcut -c 1,2,3,5,6,7,8,10,12,13,25,26,48 original-1.csv > original-2.csv


csvcut -c 1,2,3,5,6,7,8,10,12,13,25,26,48 junk.csv > junk-2.csv
```

## To ensure there are line breaks after each line

```
# NOT NEEDED - OMIT
csvcut -c 1,2,3,5,6,7,8,10,12,13,25,26,48 original-1.csv | unix2dos > original-2.csv
```


## How to cut columnns from the .csv and put the desired columns into a new file

```
NOT NEEDED - DOES NOT HANDLE COMMAS IN THE ADDRESS FIELD CORRECTLY
awk -F ',' '{print $1 "," $2 "," $3 "," $5 "," $6 "," $7 "," $8 "," $10 "," $12 "," $13 "," $25 "," $48 "," $26 }' original-1.csv > original-2.csv
```

## View the header row?

```
head -n 1 original.csv
head -n 1 original-1.csv
head -n 1 original-2.csv
```

## Count the columns in the header row or the body

Counting the number of columns in the header row:

```
head -n 1 original.csv | awk -F ',' '{print NF}'
head -n 1 original-1.csv | awk -F ',' '{print NF}'
head -n 1 original-2.csv | awk -F ',' '{print NF}'
```

Counting the number of columns in the body:

```
awk -F ',' '{print NF; exit}' original.csv
awk -F ',' '{print NF; exit}' original-1.csv
awk -F ',' '{print NF; exit}' original-2.csv


65
65
13

awk -F ',' '{print NF; exit}' junk-2.csv

```

## Count the number of rows in the csv file

```
wc -l original.csv
wc -l original-1.csv
wc -l original-2.csv


71819
71818
70453

wc -l junk-2.csv
```

## Copy original-2.csv to a file named ev_locations.csv

```
cp original-2.csv ev_locations.csv
```

## Count how many columns are in each row of the csv file

```
python count-csv-columns.py junk.csv
python count-csv-columns.py original.csv
python count-csv-columns.py ev_locations.csv
```

## verify can connect from the command line

```
sudo apt install postgresql-client
```

## connect via postgresql-client 

```
psql -h localhost -p 5432 -U postgres
```

Try a command, always end with a semicolin;
```
CREATE TABLE IF NOT EXISTS mytable (
  id SERIAL PRIMARY KEY,
  datetime TIMESTAMP NOT NULL
);
```

verify

```
SELECT COUNT(*) FROM mytable;
```

Full example of connecting and executing commands

```
psql -h localhost -p 5432 -U postgres
Password for user postgres: 
```

Output

```
psql (12.14 (Ubuntu 12.14-0ubuntu0.20.04.1), server 15.2 (Debian 15.2-1.pgdg110+1))
WARNING: psql major version 12, server major version 15.
         Some psql features might not work.
Type "help" for help.

postgres=# CREATE TABLE IF NOT EXISTS mytable (
postgres(#   id SERIAL PRIMARY KEY,
postgres(#   datetime TIMESTAMP NOT NULL
postgres(# );
CREATE TABLE
postgres=# SELECT COUNT(*) FROM mytable;
 count 
-------
     0
(1 row)
```

## Try the simulation

```
npm run simulation
```

Output

```
> postgresql-pgadmin-docker-compose@1.0.0 simulation
> node ./simulation.js

Number of rows before: 2
{
  id: '1679990154903',
  mystring: 'mykey_1679990154903',
  datetime: 2023-03-28T12:55:54.903Z
}
Number of rows after: 3
[
  { id: '1679990031918', datetime: 2023-03-28T12:53:51.918Z },
  { id: '1679990039882', datetime: 2023-03-28T12:53:59.882Z },
  { id: '1679990154903', datetime: 2023-03-28T12:55:54.903Z}
]
```

## To load into Postgres

```
\copy ev_locations from 'ev_locations.csv' delimiter',' CSV header;
```

## Count rows in the table

```
SELECT COUNT(*) FROM ev_locations;

 count 
-------
 70405
```