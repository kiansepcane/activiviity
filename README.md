code
![image](https://github.com/user-attachments/assets/a7ce219e-55be-4651-8fed-65682606b5c2)
![image](https://github.com/user-attachments/assets/cd349174-42f6-4a84-bd6a-23d5e7334e31)



output
![image](https://github.com/user-attachments/assets/f2913ca9-34d0-4ea3-acb9-0d7a38da8873)


explanation
In this Streamlit app, I set up a real-time video capture using OpenCV. The app starts by opening the webcam, and if the webcam is successfully opened, it allows me to toggle the video feed on and off with a button. I also manage the state of the video feed using Streamlit’s session state, so the feed continues to run until I choose to stop it.

Once the video feed is active, the app continuously captures frames from the webcam, converts them from BGR (OpenCV's default) to RGB, and displays them on the app in real-time. I also added a stop button within the loop that lets me stop the feed whenever I want. When the feed is no longer needed, the webcam is released to free up system resources. This makes the app interactive and user-friendly, allowing me to control the video feed with ease!
