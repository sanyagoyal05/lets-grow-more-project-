from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Load the video file
video_clip = VideoFileClip("your_video_file.mp4")

# Define the start and end time for the GIF
start_time = 5  # in seconds
end_time = 10   # in seconds

# Create a subclip of the video
gif_clip = video_clip.subclip(start_time, end_time)

# Add text to the clip
txt_clip = TextClip("My GIF", fontsize=70, color='white')
txt_clip = txt_clip.set_position('center').set_duration(end_time - start_time)

# Composite the video clip with the text clip
video_with_text = CompositeVideoClip([gif_clip, txt_clip])

# Resize the clip
resized_clip = video_with_text.resize(height=300)  # maintain aspect ratio

# Write the GIF to a file
resized_clip.write_gif("output_with_text.gif")

print("GIF with text created successfully!")
