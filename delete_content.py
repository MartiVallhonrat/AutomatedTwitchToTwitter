import os

def delete_contents_in_directory(directory_path):
    try:
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                delete_contents_in_directory(item_path)
                os.rmdir(item_path)
        print("videos deleted!")
    except Exception as e:
        print(f"An error occurred while deleting contents: {e}")
