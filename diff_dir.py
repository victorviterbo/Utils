import os
import hashlib
import argparse

def get_file_hash(filepath):
    """Calculate MD5 hash of a file to detect content differences."""
    hash_md5 = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except (IOError, OSError) as e:
        return f"Error: {str(e)}"

def scan_directory(directory):
    """Scan a directory and return a dictionary of file paths and their hashes."""
    file_map = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, directory)
            file_map[rel_path] = full_path
    return file_map

def compare_directories(dir1, dir2):
    """Compare two directories and report differences."""
    files1 = scan_directory(dir1)
    files2 = scan_directory(dir2)
    
    all_files = sorted(set(files1.keys()) | set(files2.keys()))
    
    print(f"Comparing directories:")
    print(f"  A: {os.path.abspath(dir1)}")
    print(f"  B: {os.path.abspath(dir2)}")
    print("-" * 80)
    
    results = {
        'only_in_a': [],
        'only_in_b': [],
        'different': [],
        'same': []
    }
    
    for rel_path in all_files:
        path1 = files1.get(rel_path)
        path2 = files2.get(rel_path)
        
        if path1 and not path2:
            results['only_in_a'].append(rel_path)
            print(f"ONLY IN A: {rel_path}")
            
        elif path2 and not path1:
            results['only_in_b'].append(rel_path)
            print(f"ONLY IN B: {rel_path}")
            
        elif path1 and path2:
            hash1 = get_file_hash(path1)
            hash2 = get_file_hash(path2)
            
            if hash1 == hash2:
                results['same'].append(rel_path)
                print(f"SAME:      {rel_path}")
            else:
                results['different'].append(rel_path)
                print(f"DIFFERENT: {rel_path}")
                if "Error" in hash1 or "Error" in hash2:
                    print(f"           A: {hash1}")
                    print(f"           B: {hash2}")
                else:
                    print(f"           A: {hash1}")
                    print(f"           B: {hash2}")
    
    print("-" * 80)
    print("Summary:")
    print(f"Files only in A: {len(results['only_in_a'])}")
    print(f"Files only in B: {len(results['only_in_b'])}")
    print(f"Different files: {len(results['different'])}")
    print(f"Identical files: {len(results['same'])}")
    print(f"Total files: {len(all_files)}")
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Compare two directory structures and their files.')
    parser.add_argument('directory1', help='First directory to compare')
    parser.add_argument('directory2', help='Second directory to compare')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.directory1):
        print(f"Error: {args.directory1} is not a valid directory")
        return
    
    if not os.path.isdir(args.directory2):
        print(f"Error: {args.directory2} is not a valid directory")
        return
    
    compare_directories(args.directory1, args.directory2)

if __name__ == "__main__":
    main()