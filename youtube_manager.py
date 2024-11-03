import json  # Import the JSON module to handle JSON data

def load_data():
    """Load video data from 'youtube.txt'."""
    try:
        with open('youtube.txt', 'r') as file:
            content = file.read()  # Read the entire file content
            if content.strip():  # Check if the file is not empty
                return json.loads(content)  # Parse and return the JSON data
            return []  # Return an empty list if the file is empty
    except FileNotFoundError:  # Handle the case where the file does not exist
        return []  # Return an empty list if the file is missing
    except json.JSONDecodeError:  # Handle invalid JSON format
        print("Warning: The content of 'youtube.txt' is not valid JSON. Starting with an empty list.")
        return []  # Return an empty list if JSON is invalid

def save_data_helper(videos):
    """Save video data to 'youtube.txt'."""
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)  # Write the JSON data to the file

def list_all_videos(videos):
    """List all videos in a formatted way."""
    print("\n")
    print("*" * 70)  # Print a separator line
    for index, video in enumerate(videos, start=1):  # Enumerate through the list of videos
        print(f"{index}. {video['name']}, Duration: {video['time']}")  # Display each video
    print("\n")
    print("*" * 70)  # Print another separator line

def add_video(videos):
    """Add a new video to the list."""
    name = input("Enter video name: ")  # Get video name from user
    time = input("Enter video time: ")  # Get video duration from user
    videos.append({'name': name, 'time': time})  # Add new video to the list
    save_data_helper(videos)  # Save the updated list to the file

def update_video(videos):
    """Update an existing video in the list."""
    list_all_videos(videos)  # Show current videos to the user
    index = int(input("Enter the video number to update: "))  # Get the video index
    if 1 <= index <= len(videos):  # Validate index range
        name = input("Enter the new video name: ")  # Get new video name
        time = input("Enter the new video time: ")  # Get new video duration
        videos[index - 1] = {'name': name, 'time': time}  # Update the video
        save_data_helper(videos)  # Save changes to the file
    else:
        print("Invalid index selected")  # Inform the user about invalid selection

def delete_video(videos):
    """Delete a video from the list."""
    list_all_videos(videos)  # Show current videos to the user
    index = int(input("Enter the video number to be deleted: "))  # Get the video index
    if 1 <= index <= len(videos):  # Validate index range
        del videos[index - 1]  # Remove the video from the list
        save_data_helper(videos)  # Save changes to the file
        print(f"Video {index} is successfully deleted!")  # Confirm deletion
    else:
        print("Invalid video index selected")  # Inform about invalid selection

def main():
    """Main function to run the YouTube Manager application."""
    videos = load_data()  # Load existing videos

    while True:  # Infinite loop until user chooses to exit
        print("\nYouTube Manager | Choose an option")
        print("1. List all favourite videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")  # Get user's choice

        match choice:  # Match user's choice to the appropriate case
            case '1':
                list_all_videos(videos)  # List videos
            case '2':
                add_video(videos)  # Add a new video
            case '3':
                update_video(videos)  # Update an existing video
            case '4':
                delete_video(videos)  # Delete a video
            case '5':
                break  # Exit the loop
            case _:
                print("Invalid Choice")  # Handle invalid input
        
if __name__ == "__main__":
    main()  # Run the main function

# Explanation of the __name__ variable:
# In Python, if __name__ is "__main__": checks if the script is being run directly.
# If it is, the main() function will execute. If the script is imported as a module, __name__ will be set to the module name.

