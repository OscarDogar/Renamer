# Renamer
A simple renamer for your TV shows and series (you can also change the name of your subtitles).

## Requirements
- pip install requests

## Considerations
- Enter the path where the files are located (Example *C:\Program Files\The Big Bang Theory Season 1*), inside this path must be the files to be renamed.
- You can search by name or by IMDb Id.
  - By name: *The Big Bang Theory* or in case there are several *The Big Bang Theory 2007* -> with the year of release at the end.
  - By IMDb Id: *tt0898266*  | All we need is the id of this url  ->  https://www.imdb.com/title/tt0898266/  
- All file names must at least have the season and episode abbreviation as follows: **S01E01**, **1x01**
  - Examples:  *The Big Bang Theory S01E01*, *the.big.bang.theory.s01e01*, *The Big Bang Theory 1x01*, or just *S01E01*, *1x01*
- If the serie has only one season, the season abbreviation can be omitted and only the episode abbreviation is needed.
  - Example: *The Big Bang Theory E01*
- If you want to rename your subtitles, they must be in a folder called *Subtitles* or *Subs*

## Installation
Run the Setup and inside the Renamer folder run the .exe file.
- You can find the lastest version here: https://github.com/OscarDogar/Renamer/releases

## Sponsor [<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/60854050/263421335-c7468ed6-7853-42c6-9de9-05be51da1ca2.png" width="25"/>](https://github.com/sponsors/OscarDogar)

- If you have found this repository useful or helpful, I would be very grateful if you could consider clicking on the sponsor button. Your support is what drives the continuous improvement and the creation of new projects similar to this one. Together, we can continue to do great things, thank you for being part of this community!

[Sponsor me <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/60854050/263421335-c7468ed6-7853-42c6-9de9-05be51da1ca2.png" width="20"/>](https://github.com/sponsors/OscarDogar)

 
## Result
- With all the considerations, the result would be this: *The Big Bang Theory S01E01 Pilot* (for each episode the name changes). 
- If the serie has only one season, the result would be this: *The Big Bang Theory E01 Pilot* (for each episode the name changes). 

