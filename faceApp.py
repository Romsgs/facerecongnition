from deepface import DeepFace
import os
from itertools import combinations
dirname = os.path.dirname(__file__)
foto1 = dirname + '/romulo1.jpg'
foto2 = dirname + "/romulo5.jpg"
print(dirname)
print(foto1)
print(foto2)
# df = DeepFace.find(img_path = foto1, db_path = dirname)
# result = DeepFace.verify(detector_backend='retinaface',enforce_detection=False,img1_path = foto1, img2_path = foto2, model_name='Facenet512', distance_metric='euclidean_l2')
# print(df)
# print(result)

def verify(file1, file2):
  print(file1)
  print(file2)
  result = DeepFace.verify(detector_backend='mtcnn',enforce_detection=False,img1_path = file1, img2_path = file2, model_name='Facenet512', distance_metric='euclidean_l2')

  return result
  
