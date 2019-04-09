import cv2, os, re, sys


# Save every n^th frame of a video as a JPEG
def save_frames_as_jpeg(video_name, video_path, frame_step = 1):
	capture = cv2.VideoCapture(video_path)

	file_name = re.sub(r'\..*', '', video_path)	 # Get rid of extension
	file_name = re.sub(r'(.*\/)*', '', file_name)  # Get rid of directories

	# Make images dir
	try:
		os.makedirs(f'images/{file_name}')
	except FileExistsError:
		pass

	total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

	# Iterate through frames and save each 'frame_step'-th frame
	frame = 0
	success, image = capture.read()
	while success:
		if frame % frame_step == 0:
			cv2.imwrite(f"images/{file_name}/frame_{frame}.jpg", image)  # save frame as JPEG file

		success,image = capture.read()
		frame += 1

		show_progress(frame, total_frames, status = f'frame {frame}/{total_frames} from {video_path}')

# Display progress bar
def show_progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

	#sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.write(f'[{bar}] {percents}% --- {status}\r')
    sys.stdout.flush()  


if __name__ == "__main__":
	try:
		step = int(sys.argv[1])
	except IndexError:
		print('No frame_step argument given. Setting frame_step to 1')
		step = 1
	except ValueError:
		print('Invalid argument given. Expecting frame_step argument of type integer. Quitting...')
		exit()

	for root, dirs, files in os.walk("videos"):
		for name in files:
			if name is '.DS_Store':
				continue
			path = os.path.join(root, name)
			save_frames_as_jpeg(name, path, step)
			print()
