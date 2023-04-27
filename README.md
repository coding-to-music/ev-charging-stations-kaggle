# ev-charging-stations-kaggle

# 🚀 Download via Kaggle API the EV Charging Stations dataset 🚀

https://github.com/coding-to-music/ev-charging-stations-kaggle


From / By 

## Environment variables:

https://github.com/Kaggle/kaggle-api

https://github.com/Kaggle/kaggle-api/blob/main/README.md

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
Fuel Type Code,
Station Name,
Street Address,
Intersection Directions,
City,
State,
ZIP,
Plus4,
Station Phone,
Status Code,
Expected Date,
Groups With Access Code,
Access Days Time,
Cards Accepted,
BD Blends,
NG Fill Type Code,
NG PSI,
EV Level1 EVSE Num,
EV Level2 EVSE Num,
EV DC Fast Count,
EV Other Info,
EV Network,
EV Network Web,
Geocode Status,
Latitude,
Longitude,
Date Last Confirmed,
ID,
Updated At,
Owner Type Code,
Federal Agency ID,
Federal Agency Name,
Open Date,
Hydrogen Status Link,
NG Vehicle Class,
LPG Primary,
E85 Blender Pump,
EV Connector Types,
Country,
Intersection Directions (French),
Access Days Time (French),
BD Blends (French),
Groups With Access Code (French),
Hydrogen Is Retail,
Access Code,
Access Detail Code,
Federal Agency Code,
Facility Type,
CNG Dispenser Num,
CNG On-Site Renewable Source,
CNG Total Compression Capacity,
CNG Storage Capacity,
LNG On-Site Renewable Source,
E85 Other Ethanol Blends,
EV Pricing,
EV Pricing (French),
LPG Nozzle Types,
Hydrogen Pressures,
Hydrogen Standards,
CNG Fill Type Code,
CNG PSI,
CNG Vehicle Class,
LNG Vehicle Class,
EV On-Site Renewable Source,
Restricted Access
```
