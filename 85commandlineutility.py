import argparse  # Terminal se positional aur optional arguments pakadne ke liye
import requests  # Internet se file download karne wali library

# STEP 1: Ek function banaya jo internet se file download karega
def download_file(url, local_filename):
    if local_filename is None:
        # Agar user ne naya naam nahi diya, toh URL ke aakhri hisse ko hi naam bana lo
        local_filename = url.split('/')[-1]
        
    # Internet se file ka data lekar aao
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        # Us data ko apne computer mein local_filename ke naam se save kar do
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename


# STEP 2: Main logic jahan argparse ka setup hota hai
if __name__ == '__main__':
    # 1. Ek parser machine (instance) banayi
    parser = argparse.ArgumentParser(description="Terminal se Internet ki koi bhi file download karein")

    # 2. REQUIRED ARGUMENT: Computer ko bataya ki 'url' dena compulsory hai
    parser.add_argument("url", help="Jis file ko download karna hai uska URL/Link dalein")

    # 3. OPTIONAL ARGUMENT: Flag lagaya (-o ya --output). Yeh dena zaroori nahi hai
    parser.add_argument("-o", "--output", help="Downloaded file ka naya naam kya rakhna hai", default=None)

    # 4. Terminal se aaye hue saare inputs ko read (parse) kar liya
    args = parser.parse_args()

    # Check karne ke liye print kiya ki terminal se kya inputs aaye hain
    print(f"URL received: {args.url}")
    print(f"Output filename received: {args.output}")

    # 5. Asli download karne wala function chala diya
    download_file(args.url, args.output)
    print("\nFile successfully download ho gayi hai! ")
