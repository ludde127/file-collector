import sys
import os

def collect_files():
    # Ensure minimum required arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python collect.py <directory_path> <ext1> [ext2 ...]")
        print("Example: python collect.py ~/files .py .md")
        sys.exit(1)

    # Parse arguments
    target_dir = os.path.expanduser(sys.argv[1])
    
    # Ensure extensions start with a dot and are lowercase for consistent matching
    extensions = tuple(
        ext.lower() if ext.startswith('.') else f".{ext.lower()}" 
        for ext in sys.argv[2:]
    )
    
    output_filename = "collected.txt"

    # --- Check for existing file and ask for confirmation ---
    if os.path.exists(output_filename):
        response = input(f"'{output_filename}' already exists. Overwrite? [y/N]: ").strip().lower()
        if response not in ('y', 'yes'):
            print("Operation cancelled.")
            sys.exit(0)

    # Validate directory
    if not os.path.isdir(target_dir):
        print(f"Error: The directory '{target_dir}' does not exist.")
        sys.exit(1)

    processed_count = 0

    try:
        # Open the output file in write mode
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            
            # Walk through the directory tree
            for root, _, files in os.walk(target_dir):
                for file in files:
                    if file.lower().endswith(extensions):
                        full_path = os.path.abspath(os.path.join(root, file))
                        
                        try:
                            # Read the content of the matched file
                            with open(full_path, 'r', encoding='utf-8') as infile:
                                content = infile.read()
                            
                            # Write the formatted output
                            outfile.write("=====================\n")
                            outfile.write(f"BEGIN: {full_path}\n")
                            outfile.write("=====================\n")
                            outfile.write(content)
                            
                            # Ensure there's a newline before the ending block if the file didn't end with one
                            if not content.endswith('\n'):
                                outfile.write('\n')
                                
                            outfile.write("=====================\n")
                            outfile.write(f"END: {full_path}\n")
                            outfile.write("=====================\n\n")
                            
                            processed_count += 1
                            
                        except UnicodeDecodeError:
                            print(f"Skipping {full_path}: Not a standard UTF-8 text file.")
                        except Exception as e:
                            print(f"Skipping {full_path}: Could not read file ({e})")
                            
        print(f"Done! Successfully collected {processed_count} files into '{output_filename}'.")
        
    except Exception as e:
        print(f"Fatal error writing to {output_filename}: {e}")

if __name__ == "__main__":
    collect_files()
