# Renamer
A simple renamer for your TV shows and series (you can also change the name of your subtitles)

## Requirements
- pip install python-dotenv python-decouple requests
- .env file with the FULL_PATH variable (Example *C:\Program Files\The Big Bang Theory Season 1*), inside this path must be the files to be renamed

## Considerations
- You can search by name or by IMDb Id
  - By name: *The Big Bang Theory* or in case there are several *The Big Bang Theory 2007* -> with the year of release at the end
  - By IMDb Id: *tt0898266*  | All we need is the id of this url  ->  https://www.imdb.com/title/tt0898266/  
- All file names must at least have the season and episode abbreviation as follows: **S01E01**
  - Examples:  *The Big Bang Theory S01E01*, *the.big.bang.theory.s01e01*, or just *S01E01*

## Result
- With all the considerations, the result would be this: *The Big Bang Theory S01E01 Pilot* (for each episode the name changes) 

