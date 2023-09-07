
import argparse
import json
import os
import pathlib as path
import requests
import shutil
import sys
import time
import traceback
import re
from multiprocessing      import cpu_count
from multiprocessing.pool import ThreadPool

# *****************************************************************************

BASE_URL    = "https://intellij-icons.jetbrains.design/icons"
MAX_RETRIES = 10

# *****************************************************************************

def clean_url(url: str) -> str:
    # Define a regular expression pattern to match double slashes that are not at the beginning of the URL
    pattern = r'(?<!:)//'

    # Use the sub() function from the re module to replace matched patterns with a single slash
    return re.sub(pattern, '/', url)

def download_icon(icon: dict, retries: int=0):

    try:
        variants = [""]
        if (icon["dark"]): variants.append("_dark")

        for variant in variants:
            for i, _size in enumerate(icon["sizes"]):
                size_mult = f'@{i*2}x' if i else ''
                relative_path = f'{icon["set"]}/{icon["section"]}/{icon["name"]}{size_mult}{variant}.{icon["kind"]}'

                fp = download_dir / relative_path
                if (fp.exists()):
                    if (os.stat(fp).st_size == 0):
                        print(f'Found empty file {fp}')
                        return False
                    return True
                if not (fp.parent.exists()):
                    fp.parent.mkdir(parents=True, exist_ok=True)

                time.sleep(0.05)
                print(f'Downloading {relative_path}')
                url = clean_url(f'{BASE_URL}/{relative_path}')
                r = requests.get(url, allow_redirects=True)

                with open(fp, 'wb') as f:
                    f.write(r.content)

    except requests.exceptions.ConnectionError as e:
        retries += 1
        if (retries > MAX_RETRIES):
            raise e

        time.sleep(5)
        print("Connection error... retrying")
        return download_icon(icon)

    except:
        traceback.print_exc()
        return False

    time.sleep(0.1)
    return True

# *****************************************************************************

def main() -> int:
    global download_dir

    parser = argparse.ArgumentParser()
    parser.add_argument("download_dir")
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()

    download_dir = path.Path(args.download_dir)
    if (not download_dir.parent.exists()):
        raise RuntimeError("Parent dir does not exist!")

    if args.clean:
        if (download_dir.exists()):
            shutil.rmtree(download_dir)

    download_dir.mkdir(parents=False, exist_ok=True)

    data: dict
    with open(path.Path(__file__).parent / "data.json", 'r') as f:
        data = json.load(f)
    
    threads = cpu_count() - 1

    for set in data:
        n_downloaded = 0
        n_icons = len(set["icons"])

        while (n_downloaded < n_icons):
            batch_size = min(threads, n_icons-n_downloaded)
            pool = ThreadPool(batch_size) 

            results = []
            for i in range(n_downloaded, n_downloaded+batch_size):
                results.append(
                    pool.apply_async(download_icon, args=(set["icons"][i],))
                )

            n_downloaded += batch_size

            stop = False
            for result in results:
                result.wait()
                if not result.get():
                    stop = True

            pool.close()
            pool.join()

            if stop:
                return 1

    return 0

# *****************************************************************************

if __name__ == "__main__":
    sys.exit(main())
