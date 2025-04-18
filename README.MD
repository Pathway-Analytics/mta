# Project Icons and Logos

This project contains all the icons and logos used for the project, organized into the following directories:
- `bimi/`: BIMI-related assets.
- `icons/`: Favicon and other small icons.
- `logo/`: Logos in various formats and sizes.

The project also includes an `index.html` file that displays all the images in a gallery format for easy preview.

---

## How to Maintain This Project

### 1. **Adding New Images**
- Place new images in the appropriate directory (`bimi`, `icons`, or `logo`).
- Supported image formats:
  - `.png`
  - `.jpg` / `.jpeg`
  - `.svg`
  - `.tiff`
  - `.ico`

### 2. **Updating the Gallery**
After adding or removing images, regenerate the `index.html` file to reflect the changes.

#### Steps to Regenerate:
1. Ensure you have Python installed on your system.
2. Run the `generate_index.py` script:
   ```bash
   python3 generate_index.py