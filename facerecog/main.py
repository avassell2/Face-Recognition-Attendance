import face_recognition #compare faces to that in database
import cv2 #takes input from webcam
import numpy as np
import csv
import os
from datetime import datetime

database="person.db"

video_capture = cv2.VideoCapture(0)

gates_Image = face_recognition.load_image_file("photos/gates.jpg")
gates_encoding = face_recognition.face_encodings(gates_Image)[0]

macfarlane_Image = face_recognition.load_image_file("photos/macfarlane.jpg")
macfarlane_encoding = face_recognition.face_encodings(macfarlane_Image)[0]

trump_Image = face_recognition.load_image_file("photos/trump.jpg")
trump_encoding = face_recognition.face_encodings(trump_Image)[0]

known_face_encoding = [
gates_encoding, macfarlane_encoding, trump_encoding
]

known_faces_names = [
"gates",
"macfarlane",
"trump"
]

students = known_faces_names.copy()

face_locations = []
face_encoding = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")


f = open(current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)


while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]


            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name,current_time])
    cv2.imshow("attendence system",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
