import os

html_file = "index.html"
image_extensions = {".png", ".jpg", ".jpeg", ".tiff", ".ico", ".svg"}

# Directories to scan
directories_to_scan = ["bimi", "icons", "logo"]

# Collect all image files
images = []
for directory in directories_to_scan:
    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                images.append(os.path.join(root, file))

# Generate HTML content
gallery_items = ""
for image in images:
    gallery_items += f"""
    <div class="gallery-item">
      <img src="{image}" alt="{image}">
      <div class="filename">{image}</div>
    </div>
    """

# Insert the gallery items into the HTML template
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Project Icons and Logos</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 20px;
    }}
    h1 {{
      text-align: center;
    }}
    .gallery {{
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: center;
    }}
    .gallery-item {{
      text-align: center;
    }}
    img {{
      max-width: 150px;
      max-height: 150px;
      display: block;
      margin: 0 auto;
    }}
    .filename {{
      margin-top: 10px;
      font-size: 14px;
      color: #555;
    }}
  </style>
</head>
<body>
  <h1>Project Icons and Logos</h1>
  <div class="gallery">
    {gallery_items}
  </div>
</body>
</html>
"""

# Write the HTML content to the file
with open(html_file, "w") as f:
    f.write(html_template)

print(f"Generated {html_file} with {len(images)} images.")