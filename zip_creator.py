import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    # Create the destination path for the zip file
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    # Create and write the zip file
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            # Convert the string filepath to a Path object
            path = pathlib.Path(filepath)
            archive.write(path, arcname=path.name)