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

## Result
- With all the considerations, the result would be this: *The Big Bang Theory S01E01 Pilot* (for each episode the name changes). 
- If the serie has only one season, the result would be this: *The Big Bang Theory E01 Pilot* (for each episode the name changes). 

