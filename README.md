# Save video frames as images

## Requirements
- OpenCV. You can install it by running `$ pip install opencv-python`
- Copy videos to a folder called `videos/`
  - You should end up with a folder structure similar to this:
    ```
.
├── README.md
├── requirements.txt
├── video_frames_to_images.py
└── videos
    ├── video1.mp4
    ├── video2.mp4
    └── video3.mp4
    ```
## Run from terminal
`$ python3 video_frames_to_images.py` will output all frames as .jpg in a new folder `images/`

## Arguments
- **Frame step**- an integer argument **n** that will only save every **n**-th frame. For example, running `$ python3 video_frames_to_images.py 30` will save every 30th frame of the video.
