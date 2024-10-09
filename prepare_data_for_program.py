import json
import csv

# Placeholders for the file paths
CSV_FILE_PATH = "csv/5K_GPT4-V.csv"  # Replace with your CSV file path
CAPTIONS_JSON_PATH = (
    "captions_val2014.json"  # Replace with your captions JSON file path
)
OUTPUT_JSON_PATH = (
    "5K_GPT4-V_prepared.json"  # The output will be saved in the running folder
)

# Step 1: Load the captions from the captions_val2014.json file
with open(CAPTIONS_JSON_PATH, "r") as captions_file:
    captions_data = json.load(captions_file)

# Build a dictionary to map image IDs to their captions
image_captions = {}
for annotation in captions_data["annotations"]:
    image_id = annotation["image_id"]
    caption = annotation["caption"]
    if image_id not in image_captions:
        image_captions[image_id] = []
    image_captions[image_id].append(caption)

# Step 2: Read the CSV file and construct the output JSON structure
imgblobs = []

with open(CSV_FILE_PATH, "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        filepath = row["filepath"]
        description = row["description"].replace('"', " ").replace("\\", "").strip()

        # Extract the image ID from the filepath
        # Assuming the filepath is like 'COCO_val2014_000000000042'
        image_id_str = filepath.replace("COCO_val2014_", "").replace(".jpg", "")
        image_id = int(
            image_id_str.lstrip("0")
        )  # Remove leading zeros and convert to int

        # Get the captions for this image ID
        captions = image_captions.get(image_id, [])
        candidatelist = [
            {"text": caption} for caption in captions[:5]
        ]  # Get first five captions

        # Construct the imgblob entry
        imgblob = {
            "candidatelist": candidatelist,
            "img_path": f"{filepath}.jpg",  # Add the '.jpg' extension if not present
            "candidate": {"text": description},
        }

        imgblobs.append(imgblob)

# Step 3: Write the output to a new JSON file
output_data = {"imgblobs": imgblobs}

with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as output_file:
    json.dump(output_data, output_file, ensure_ascii=False, indent=2)

print(f"Output has been saved to {OUTPUT_JSON_PATH}")
