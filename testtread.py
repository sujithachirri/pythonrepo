import os
import concurrent.futures

def find_files(filename, search_path):
    result = []

    # Walking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root,filename))
    return result
Drives=["C:","D:","E:","F:"]
input_file='demotext.txt'
with concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(find_files,input_file,drive) for drive in Drives]

    for r in concurrent.futures.as_completed(results):
        print(r.result())



#print(find_files("demotext.txt")