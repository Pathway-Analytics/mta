# Project Icons and Logos

This project contains all the icons and logos used for the project, organized into the following directories:
- `bimi/`: BIMI-related assets.
- `icons/`: Favicon and other small icons.
- `logo/`: Logos in various formats and sizes.

The project also includes an `index.html` file that displays all the images in a gallery format for easy preview.  
The gallery is hosted at: [http://mta-sts.pathwayanalytics.com/index.html](http://mta-sts.pathwayanalytics.com/index.html)

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
   ```
3. Open the updated `index.html` file in your browser to verify:
   ```bash
   open index.html
   ```

### 3. **Syncing with S3**
The project is automatically synced with the S3 bucket (`mta-sts-pathwayanalytics-com`) whenever changes are pushed to the `main` branch on GitHub.

#### How It Works:
- A GitHub Actions workflow (`.github/workflows/s3-sync.yml`) is configured to sync the repository contents with the S3 bucket.
- The workflow is triggered on every push to the `main` branch.
- The hosted gallery at [http://mta-sts.pathwayanalytics.com/index.html](http://mta-sts.pathwayanalytics.com/index.html) is updated automatically.

---

## Troubleshooting

### No Images in the Gallery
- Ensure the images are in the correct directories (`bimi`, `icons`, or `logo`).
- Verify that the image file extensions are supported (`.png`, `.jpg`, `.svg`, `.tiff`, `.ico`).
- Run the `generate_index.py` script again to regenerate the `index.html`.

### S3 Sync Issues
- Ensure the AWS credentials stored in GitHub Secrets are correct.
- Check the GitHub Actions logs under the **Actions** tab in the repository for errors.

---

## Contributing
- Follow the folder structure and naming conventions when adding new assets.
- Test the `index.html` file after making changes to ensure all images are displayed correctly.

---

## License
This project is licensed under [Your License Here].