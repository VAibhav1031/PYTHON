import math
import  cv2
import numpy as np
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=2)
mp_drawing = mp.solutions.drawing_utils

sample_img = cv2.imread('sample image.jpg')
plt.figure(figsize = [10,10])
plt.title("sample image");plt.axis('off');plt.imshow(sample_img[:,:,::-1]);plt.show()

result = pose.process(cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB))
if result.pose_landmarks.landmark:
    for i in range(2):
      print(f'{mp_pose.PoseLandmark(i).name}:/n{result.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value]}')

image_height, image_width, _ = sample_img.shape
if result.pose_landmarks:
  for i in range(2):
    print(f'{mp_pose.PoseLandmark(i).name}:')
    print(f'x:{result.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value].x*image_width}')
   print(f'y:{result.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value].y*image_width}')
    print(f'z:{result.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value].z*image_width}')
    print(f'visibility:{result.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value].visibility}\n')

img_copy = sample_img.copy()
if result.pose_landmarks:
  mp_drawing.draw_landmarks(image=img_copy, landmark_list=result.pose_landmarks,connections=mp_pose.POSE_CONNECTIONS)
  fig= plt.figure(figsize = [10,10])
  plt.title("output");plt.axis('off');plt.imshow(img_copy[:,:,::-1]);plt.show()

mp_drawing.plot_landmarks(result.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

def detectpose(image,pose,display=True):
  output_image = image.copy()
  imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  result = pose.process(imageRGB)
  height, width,_ = image.shape
  landmarks = []
  if result.pose_landmarks:
    mp_drawing.draw_landmarks(image=output_image, landmark_list= result.pose_landmarks, connections= mp_pose.POSE_CONNECTIONS)
    for landmark in result.pose_landmarks.landmark:
      landmarks.append((int(landmark.x*width),(landmark.y*height),(landmark.z*width)))
      if display:
        plt.figure(figsize=[22,22])
        plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title("Original Image");plt.axis('off');
        plt.subplot(122);plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis('off');
        mp_drawing.plot_landmarks(result.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

      else:
          return output_image,

pose_video = mp_pose.Pose(static_image_mode=False , min_detection_confidence=0.5, model_complexity=1)
video = cv2.VideoCapture(0)
cv2.namedWindow('pose detection', cv2.WINDOW_NORMAL)
video.set(3,1280)
video.set(4,960)
time1 = 0
while video.isOpened():
  ok, frame = video.read()
  if not ok:
    break
  frame = cv2.flip(frame,1)
  frame_height, frame_width,_ = frame.shape
  frame = cv2.resize(frame,(int(frame_width* (640/ frame_height)),640))
  frame, _ = detectpose(frame, pose_video, display=False)
  time2 = time()
  if(time2-time1)>0:
    frames_per_second = 1.0/(time2-time1)
    cv2.putText(frame, 'FPS: {}'.format(int(frames_per_second)),(10,30),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),3)
    time1 = time2
  cv2.imshow('pose detection',frame)
  k = cv2.waitKey(1) &0xFF
  if (k==27):
    break
    video.release()
    cv2.destroyAllWindows()
