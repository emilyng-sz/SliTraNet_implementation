import cv2
import torch
from moviepy.editor import VideoFileClip

def get_frames_as_tensor(path, library="MoviePy", height = None, width = None, frame_per_sec= None):
    '''
    input: video path name
    output: list of video frames in tensor format
    '''
    frame_as_tensor = []

    if library=="MoviePy":
        
        # Create a VideoFileClip object from the input video
        video_clip = VideoFileClip(path) # returns video.io VideoFileClip 

        if not frame_per_sec:
            frame_per_sec = video_clip.fps 
            print(f"Video default fps is {frame_per_sec}")

        for frame in video_clip.iter_frames(fps=frame_per_sec):
            if height or width:
                frame = cv2.resize(frame, (width, height))
            
            frame_as_tensor.append(torch.as_tensor(frame))
    
    elif library=='cv2': #cv2
        cap = cv2.VideoCapture(path)
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
        for i in range(length):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i) # starts counting from 0
            ret, frame = cap.read()
            frame_as_tensor.append(torch.as_tensor(frame))
    
    else:
        raise ValueError("set library='MoviePy' or 'cv2' ")
    print(f"number of frames as tensors returned are {len(frame_as_tensor)}")
    return frame_as_tensor
