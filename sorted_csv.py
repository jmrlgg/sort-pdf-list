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
    :return: A list of matched categories.
    """
    filename_lower = filename.lower()  # Convert filename to lowercase to ensure case-insensitive matching
    
    # List comprehension to check if any keyword appears in the filename
    matched_categories = [
        category for category, keywords in CATEGORIES.items()
        if any(keyword in filename_lower for keyword in keywords)
    ]
    
    return matched_categories if matched_categories else ["Uncategorized"]

def save_files_to_categorized_csv(folder_path, output_folder):
    """
    Scans a folder for .pdf and .epub files, categorizes them, 
    and saves the data to separate CSV files by category.
    
    :param folder_path: The path to the folder containing the files.
    :param output_folder: The folder where categorized CSVs will be saved.
    """
    try:
        # Ensure output directory exists
        os.makedirs(output_folder, exist_ok=True)
        
        # List all files in the folder
        files = os.listdir(folder_path)
        
        # Filter only .pdf and .epub files and sort them alphabetically
        sorted_files = sorted(
            [f for f in files if f.lower().endswith(('.pdf', '.epub')) and os.path.isfile(os.path.join(folder_path, f))]
        )
        
        # Dictionary to hold file lists for each category
        categorized_files = {category: [] for category in CATEGORIES.keys()}
        categorized_files["Uncategorized"] = []
        
        # Process each file and categorize it
        for title in sorted_files:
            categories = categorize_file(title)
            for category in categories:
                categorized_files[category].append(title)
        
        # Write categorized files to separate CSVs
        for category, files in categorized_files.items():
            if files:  # Only create a CSV if there are files in that category
                csv_filename = os.path.join(output_folder, f"{category}_files.csv")
                with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Filename"])  # Write header row
                    for filename in files:
                        writer.writerow([filename])
        
        print(f"Categorized CSV files saved in: {output_folder}")
    except FileNotFoundError:
        print("Folder not found. Please check the path and try again.")
    except Exception as e:
        print(f"Error: {str(e)}")  # Catch and display any unexpected errors

# Example usage
folder_path = "./"  # Replace with the actual folder path
output_folder = "./categorized_csvs"  # Output folder for category-specific CSV files
save_files_to_categorized_csv(folder_path, output_folder)  # Run the function
