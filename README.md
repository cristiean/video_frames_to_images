# Save video frames as images

- Copy videos to a folder `videos/`
- You should end up with something like this:
  ```
  \_video_frames_to_images.py
  \_videos
    \_video1.mp4
    \_video2.mp4
    \_video3.mov
  \_README.md
  ```
- Run `python3 video_frames_to_images.py` to process the videos. This will output all frames as .jpg in a new folder `images/`
- **Frame step**- an integer argument ***n*** that will only save every ***n***-th frame. 
