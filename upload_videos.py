from google.colab import files

os.chdir('/content/keras_Realtime_Multi-Person_Pose_Estimation/sample_videos')

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

os.chdir('..')
