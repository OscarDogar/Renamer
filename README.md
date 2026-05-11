<div align="center">

# 🎬 Renamer

### Smart TV Show & Subtitle Renaming Tool

Automatically rename your TV shows, anime episodes, and subtitles using episode metadata from IMDb.

<img src="https://img.shields.io/github/downloads/OscarDogar/Renamer/total?style=for-the-badge&color=38bdf8" />
<img src="https://img.shields.io/github/stars/OscarDogar/Renamer?style=for-the-badge&color=facc15" />
<img src="https://img.shields.io/github/license/OscarDogar/Renamer?style=for-the-badge&color=22c55e" />

</div>

---

# ✨ Features

- 🎞️ Automatically rename TV show episodes
- 📝 Rename subtitle files alongside episodes
- 🔍 Search series by **name** or **IMDb ID**
- 📺 Supports multiple episode naming formats
- ⚡ Lightweight and easy to use
- 🧠 Automatically fetches episode titles from IMDb
- 📂 Batch rename entire seasons instantly

---

# 📦 Installation

## Windows Executable

1. Download the latest release from:

👉 https://github.com/OscarDogar/Renamer/releases

2. Extract the files

3. Open the `Renamer` folder

4. Run the executable file

---

# 🐍 Python Requirements

If you want to run the project manually:

```bash
pip install requests
```

---

# 🚀 Usage

## 1️⃣ Select Your Series Folder

Enter the path containing your video files.

### Example

```txt
C:\TV Shows\The Big Bang Theory Season 1
```

The folder should contain the episodes you want to rename.

---

## 2️⃣ Search the Series

You can search using:

### 🔎 Series Name

```txt
The Big Bang Theory
```

If multiple results exist, include the release year:

```txt
The Big Bang Theory 2007
```

---

### 🎯 IMDb ID

```txt
tt0898266
```

IMDb URL example:

```txt
https://www.imdb.com/title/tt0898266/
```

Only the ID is required.

---

# 📁 Supported File Naming Formats

Renamer detects episodes using common naming conventions.

## ✅ Supported Examples

```txt
The Big Bang Theory S01E01
the.big.bang.theory.s01e01
The Big Bang Theory 1x01
S01E01
1x01
```

---

# 📺 Single Season Shows

If the series contains only one season, the season number can be omitted.

## Example

```txt
The Big Bang Theory E01
```

---

# 📝 Subtitle Support

To rename subtitle files automatically:

- Place subtitles inside a folder named:

```txt
Subtitles
```

or

```txt
Subs
```

Supported subtitle files inside those folders will be renamed together with the episodes.

---

# ✅ Example Result

## Before

```txt
The.Big.Bang.Theory.S01E01.mkv
```

## After

```txt
The Big Bang Theory S01E01 Pilot.mkv
```

---

## Single Season Example

```txt
The Big Bang Theory E01 Pilot.mkv
```

---

# 📂 Recommended Folder Structure

```txt
The Big Bang Theory Season 1/
│
├── The.Big.Bang.Theory.S01E01.mkv
├── The.Big.Bang.Theory.S01E02.mkv
│
├── Subs/
│   ├── subtitle1.srt
│   └── subtitle2.srt
```

---

# ⚠️ Important Notes

- Episode files must contain episode identifiers like:

```txt
S01E01
```

or

```txt
1x01
```

- Internet connection is required to fetch IMDb metadata
- Incorrect or unsupported naming formats may not be detected properly

---

# ❤️ Support the Project

If you find this project useful, consider supporting development.

Your support helps improve the project and create more open-source tools 🚀

<div align="center">

<a href="https://github.com/sponsors/OscarDogar">
  <img src="https://img.shields.io/badge/Sponsor%20on%20GitHub-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" />
</a>

</div>

---

# 🌟 Contributing

Contributions, suggestions, and bug reports are welcome.

Feel free to open an issue or submit a pull request.

---

# 📜 License

This project is open source and available under the MIT License.

---

<div align="center">

### ⭐ If you like this project, consider giving it a star on GitHub!

</div>
