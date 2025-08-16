import os, requests, re, json

def findPath(name):
    path=os.getcwd()
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

try:
    configError = None
    CONFIG_FILE = json.load(open(findPath('config.json')))
except Exception as err:
    CONFIG_URL = "https://raw.githubusercontent.com/OscarDogar/Renamer/main/config.json"
    ConfigResponse = requests.get(CONFIG_URL)
    CONFIG_FILE = ConfigResponse.json()
        

# name = "The Big Bang Theory"
# imdb = "tt0898266":
# TODO Add the ability to search movies 
fullPath = input("Enter the full path of the folder where the episodes or subs are located: ")
option = input("Select if you want to search by name or imdb id\n1. By Name\n2. By IMDb Id\nType: ")
name = ""
imdb = ""
while(option.strip() != "1" and option.strip() != "2" or "name".lower() not in option.lower() or "imdb".lower() not in option.lower()):
    if option.strip() == "1" or "name".lower() in option.lower():
        print("Please make sure it is the correct name otherwise the names will be overwritten")
        name = input("Enter the name of the show (example The Big Bang Theory): ")
        break
    elif option.strip() == "2" or "imdb".lower() in option.lower():
        imdb = input("Enter IMDB ID (example tt0898266): ")
        break
    else:
        print("Invalid option")
        option = input("Select if you want to search by name or imdb id\n1. By name\n2. By imdb id\nType: ")
else:
    print("Name Error")
    exit()
year = ""
if imdb != "":
    IMDB_URL = CONFIG_FILE["APIs"]["IMDB_URL"].format(imdb)
    info = requests.request("GET", IMDB_URL)
elif name != "":
    #Remove the year from the name
    if len(name) >= 1 and name.split():
        nameArray = name.split(" ")
        nameArray = [x for x in nameArray if x != ""]
        #Check if the name has numbers in it
        
        if nameArray[-1].isnumeric():
            year = name.split(" ")[-1]
            name = " ".join(nameArray[:-1])
    TV_SHOWS_URL = CONFIG_FILE["APIs"]["TV_SHOWS_URL"].format(name)
    info = requests.request("GET", TV_SHOWS_URL)
else:
    print("No name or iIMDb id was provided")
    exit()
TV_SHOWS_EPISODE_URL = CONFIG_FILE["APIs"]["TV_SHOWS_EPISODE_URL"]#.format(ID, season, episode)

def rename(id, name):
    subsExtension = ""
    if "subs" in fullPath.lower() or "subtitle" in fullPath.lower():
        subsExtension = input("Enter the subtitle language: (example: en, spa, fr, etc) or leave it empty if you don't want any specific language: ")
    os.chdir(fullPath)
    path = os.getcwd()
    
    VALID_VIDEO_EXTENSIONS = CONFIG_FILE["VALID_EXTENSIONS"]["VIDEO"]
    VALID_SUBTITLE_EXTENSIONS = CONFIG_FILE["VALID_EXTENSIONS"]["SUBTITLE"]
    for file in os.listdir(path):
        ## get the extension of the file
        dot = file.rfind(".") ## get the position of the last dot
        if dot != -1: ## if there is a dot
            extension = file[dot:]
            if extension in VALID_VIDEO_EXTENSIONS or extension in VALID_SUBTITLE_EXTENSIONS:
                ACCEPTED_NAMES = CONFIG_FILE["REGEX"]["ACCEPTED_NAMES"]
                regexResult = None
                for regex in ACCEPTED_NAMES:
                    regexResult = re.search(regex, file)
                    if regexResult:
                        break
                namesErrors = []
                if regexResult:
                    positions = regexResult.span()
                    seasonInfo = file[positions[0]:positions[1]].upper()
                    #TODO Give users the option to save the name in the season-episode format of their choice
                    if "S" in seasonInfo:
                        seasonNumber = seasonInfo[seasonInfo.index("S")+1:3]
                        episodeNumber = seasonInfo[seasonInfo.index("E")+1:len(seasonInfo)]
                    elif "X" in seasonInfo:
                        seasonNumber = seasonInfo[0:seasonInfo.index("X")]
                        episodeNumber = seasonInfo[seasonInfo.index("X")+1:len(seasonInfo)]
                        if len(seasonNumber) == 1:
                            seasonNumber = "0" + seasonNumber
                        seasonInfo = "S" + seasonNumber + "E" + episodeNumber
                    else:
                        seasonNumber = "01"
                        episodeNumber = seasonInfo[seasonInfo.index("E")+1:3]
                    episodeInfo = requests.request("GET", TV_SHOWS_EPISODE_URL.format(id, seasonNumber, episodeNumber))
                    if episodeInfo.status_code == 200:
                        responseEpisodeInfo = episodeInfo.json()
                        episodeName = responseEpisodeInfo["name"]
                        # Remove characters that are not allowed in file names
                        episodeName = re.sub(r'[^\w\s]', ' ', episodeName)
                        
                        if extension in VALID_SUBTITLE_EXTENSIONS:
                            if subsExtension != "":
                                fullName = "{} - {} - {}.{}{}".format(name, seasonInfo, episodeName, subsExtension, extension)
                            else:
                                fullName = "{} - {} - {}{}".format(name, seasonInfo, episodeName, extension)
                        else:
                            fullName = "{} - {} - {}{}".format(name, seasonInfo, episodeName, extension)
                        if os.path.isfile(fullName):
                            # print("{} is fine".format(fullName))
                            continue
                        else:
                            os.rename(file, fullName)
                    else:
                        namesErrors.append(file)
                else:
                    namesErrors.append(file)
    if len(namesErrors) > 0:
        print("The following files have no episode name: {}".format(namesErrors))
        print("Please validate that the file name contains the season and the episode as follows: S01E01")
    else:
        print("All files have been renamed")

def main():
    try:
        if info.status_code == 200:
            response = info.json()
            global name
            if len(response) == 1 and type(response) == list:
                id = response[0]["show"]["id"]
                name = response[0]["show"]["name"]
                name = re.sub(r'[^\w\s]', ' ', name.replace(":", ""))
                rename(id, name)
            elif len(response) > 1 and type(response) == list:
                if year.isnumeric():
                    flag = False
                    for i in response:
                        if name.lower() in i["show"]["name"].lower() and i["show"]["premiered"][:4] == year:
                            id = i["show"]["id"]
                            name = i["show"]["name"]
                            flag = True
                            break  
                    if flag:
                        name = re.sub(r'[^\w\s]', ' ',  name.replace(":", ""))
                        rename(id, name)
                else:
                    print("There is more than one option, please specify a release year as follows: ({} 2016) or use the IMDb search".format(name))
                    exit()
            elif len(response) > 1 and type(response) == dict:
                id = response["id"]
                name = response["name"]
                name = re.sub(r'[^\w\s]', ' ',  name.replace(":", ""))
                rename(id, name)
            else:
                print("No shows found")
                print("Please check the name or IMDb id and try again")
                exit()
        else:
            if info.status_code == 404:
                print("The show was not found")
                print("Please check the name or IMDb id and try again")
            else:
                print("Error: {}".format(info.status_code))
    except Exception as err:
        if FileNotFoundError:
            print("The path was not found")
        else:
            print(err)

if __name__ == '__main__':
    main()
    input("Press enter to exit")