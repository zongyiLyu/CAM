import os
import json

def find_max_total_runs(folder_path):
    """Find max total_runs in output_log.jsonl within a log_ folder"""
    log_file = os.path.join(folder_path, "output_log.jsonl")
    if not os.path.exists(log_file):
        return None
    
    max_runs = None
    with open(log_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                if "total_runs" in entry:
                    val = entry["total_runs"]
                    if max_runs is None or val > max_runs:
                        max_runs = val
            except json.JSONDecodeError:
                continue
    return max_runs

def scan_folders(root_dir):
    results = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        folder_name = os.path.basename(dirpath)
        if folder_name.startswith("log_"):
            max_runs = find_max_total_runs(dirpath)
            if max_runs is not None:
                results[dirpath] = max_runs

    return results

def main(root_dir):
    results = scan_folders(root_dir)
    
    if not results:
        print("No log_ folders with valid output_log.jsonl found.")
        return
    
    print(f"Found {len(results)} log_ folder(s):\n")
    for path, max_runs in results.items():
        print(f"  {path}: max total_runs = {max_runs}")
    
    avg = sum(results.values()) / len(results)
    print(f"\nAverage of max total_runs across all folders: {avg:.2f}")

if __name__ == "__main__":
    import sys
    root = '.'
    main(root)