import os
import csv

# Define categories with multiple keywords (case-insensitive matching)
CATEGORIES = {
    "Art": ["painting", "oil painting", "water color", "watercolor", "landscape", "sketching", "drawing", "art", "manga", "vision", "architectural", "design", "create", "develop", "method", "character", "artist", "perspectve", "light", "color", "paintings", "painters", "cartooning", "cartoon", "image", "images", "abstract", "alla prima", "anatonmy"],
    "Chess": ["chess", "pawns", "pawn", "openings", "endgame", "attack", "tactical", "master", "tactics", "games", "players", "positional", "strategy", "repertoire"],
    "Writing": ["fiction", "novel", "story", "fantasy", "literature", "essays", "writing", "script", "screenplay"],
    "Programming": ["math", "algebra", "calculus", "geometry", "statistics", "programming", "python", "html", "javascript", "js", "django", "css"],
    "Garden": ["Hydroponic", "garden", "grow", "growing", "permaculture", "cannabis", "marijuana", "no till", "no-till"],
    "Music Guitar": ["guitar", "singing", "voice", "song", "riff", "blues", "rock", "music", "songbook"]

}

def categorize_file(filename):
    """
    Assigns categories to a file based on matching keywords (case-insensitive).
    
    :param filename: The name of the file to categorize.
    :return: A comma-separated string of matched categories or "Uncategorized".
    """
    filename_lower = filename.lower()  # Convert filename to lowercase to ensure case-insensitive matching

    # List comprehension to check if any keyword appears in the filename
    matched_categories = [
        category for category, keywords in CATEGORIES.items()
        if any(keyword in filename_lower for keyword in keywords)
    ]
    
    # Return matched categories as a comma-separated string, or "Uncategorized" if no match
    return ", ".join(matched_categories) if matched_categories else "Uncategorized"

def save_files_to_categorized_csv(folder_path, output_csv):
    """
    Scans a folder for .pdf and .epub files, categorizes them, and saves the data to a CSV file.
    
    :param folder_path: The path to the folder containing the files.
    :param output_csv: The name of the output CSV file.
    """
    try:
        # List all files in the folder
        files = os.listdir(folder_path)

        # Filter only .pdf and .epub files and sort them alphabetically
        sorted_files = sorted(
            [f for f in files if f.lower().endswith(('.pdf', '.epub')) and os.path.isfile(os.path.join(folder_path, f))]
        )

        # Open the CSV file for writing
        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Filename", "Categories"])  # Write header row

            # Process each file and write its name and categories to the CSV
            for title in sorted_files:
                categories = categorize_file(title)
                writer.writerow([title, categories])

        print(f"CSV file saved: {output_csv}")  # Confirm successful completion
    except FileNotFoundError:
        print("Folder not found. Please check the path and try again.")
    except Exception as e:
        print(f"Error: {str(e)}")  # Catch and display any unexpected errors

# Example usage
folder_path = "./"  # Replace with the actual folder path
output_csv = "categorized_files.csv"  # Output CSV file name
save_files_to_categorized_csv(folder_path, output_csv)  # Run the function
