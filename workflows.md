
## GitHub Actions Workflow Summary

This repository uses GitHub Actions to automatically test and validate all code changes pushed to the repository. The workflow performs the following actions:

- **Set up Python environment** using version 3.10
- **Install dependencies** listed in `requirements.txt`
- **Run all unit tests** using Python's `unittest` framework
- **Build a release artifact** (zip file) when changes are pushed to the `main` branch

![First Screenshort](https://github.com/user-attachments/assets/c9915005-f524-416e-b0a4-58ff9434410c)
![sec screenshot](https://github.com/user-attachments/assets/2d9a7d46-7845-41c1-b4a1-af795604ed37)

All recent successful runs are visible under the **Actions** tab. Failed CI runs are automatically cleaned up for clarity
