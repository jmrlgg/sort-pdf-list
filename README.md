# Sort Your PDFs and EPUBs with a Keyword  

This script scans for PDF and EPUB files, then labels each one with a keyword of your choice.  Each Category has it's on CSV

## Steps to Use  

1. **Change Directory**  
   Modify the working directory in the script. By default, it operates in the directory where the file resides.  

2. **Customize Keywords**  
   Edit the keyword categories to fit your needs.  

3. **Run the Script**  
   Execute the following command:  

   ```sh
   python sort_csv_keyword.py


```python
CATEGORIES = {
    "Art": [
        "painting", "oil painting", "water color", "watercolor", "landscape", 
        "sketching", "drawing", "art", "manga", "vision", "architectural", 
        "design", "create", "develop", "method", "character", "artist", 
        "perspective", "light", "color", "paintings", "painters", "cartooning", 
        "cartoon", "image", "images", "abstract", "alla prima", "anatomy"
    ],
    "Chess": [
        "chess", "pawns", "pawn", "openings", "endgame", "attack", "tactical", 
        "master", "tactics", "games", "players", "positional", "strategy", 
        "repertoire"
    ],
    "Writing": [
        "fiction", "novel", "story", "fantasy", "literature", "essays", 
        "writing", "script", "screenplay"
    ],
    "Programming": [
        "math", "algebra", "calculus", "geometry", "statistics", "programming", 
        "python", "html", "javascript", "js", "django", "css"
    ],
    "Garden": [
        "hydroponic", "garden", "grow", "growing", "permaculture", "cannabis", 
        "marijuana", "no till", "no-till"
    ],
    "Music Guitar": [
        "guitar", "singing", "voice", "song", "riff", "blues", "rock", "music", 
        "songbook"
    ]
}


TODO: 
Create an append feature atm I am deleting and creating new each time
use pages in future
create feature that connects to file server > search for like names > relay such data > present such data > save data 

