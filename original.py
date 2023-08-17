import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import pandas
from datetime import datetime

# Create a window
cv2.namedWindow("Face Attendance", cv2.WINDOW_NORMAL)

# Get the screen resolution
screen_width, screen_height = 1024, 576  # Replace with your desired screen resolution

# Resize the window to fit the screen
cv2.resizeWindow("Face Attendance", screen_width, screen_height)

# imgBackground = cv2.imread('Resources/background.png')
imgBackground = cv2.imread('Resources/img.png')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# # Importing the student images into a list
folderModePath = 'Database/Images'
modePathList = os.listdir(folderModePath)
imagesStudent = {}
for path in modePathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    imagesStudent[path] = img

# importing attendance sheet
data = pandas.read_csv("Database/attendance.csv")
print(data)

# Load the encoding file
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                print("Known Face Detected")
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = studentIds[matchIndex]
                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

        if counter != 0:

            if counter == 1:
                imgStudent = imagesStudent[f"{id}.png"]
                id_str = int(id)
                last_attendance_date = data.loc[data['id'] == id_str]['last_attendance_date'].values[0]
                today = datetime.now().strftime('%Y-%m-%d')
                if last_attendance_date.split()[0] != (today).split()[0]:
                    attendance_count = int(data.loc[data['id'] == id_str]['total_attendance'].values[0]) + 1
                    attendance_count_str = str(attendance_count)

                    # Update the 'Total Attendance' and 'Last Attendance Date' columns for the row
                    data.loc[data['id'] == id_str, 'total_attendance'] = attendance_count_str
                    data.loc[data['id'] == id_str, 'last_attendance_date'] = datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S")

                    # Save the changes back to the CSV file
                    data.to_csv("Database/attendance.csv", index=False)

                else:
                    modeType = 3
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

            if modeType != 3:

                if 10 < counter < 20:
                    modeType = 2

                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

                if counter <= 10:
                    # id = int(id)
                    id_str = int(id)
                    cv2.putText(imgBackground, str(data.loc[data['id'] == id_str]['total_attendance'].values[0]),
                                (861, 125),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(data.loc[data['id'] == id_str]['major'].values[0]), (1006, 550),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(id), (1006, 493),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(data.loc[data['id'] == id_str]['year'].values[0]), (1025, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(data.loc[data['id'] == id_str]['starting_year'].values[0]),
                                (1125, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                    (w, h), _ = cv2.getTextSize(data.loc[data['id'] == id_str]['name'].values[0],
                                                cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset = (414 - w) // 2
                    cv2.putText(imgBackground, str(data.loc[data['id'] == id_str]['name'].values[0]),
                                (808 + offset, 445),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)

                    imgBackground[175:175 + 216, 909:909 + 216] = imgStudent

                counter += 1

                if counter >= 20:
                    counter = 0
                    modeType = 0
                    # studentInfo = {}
                    imgStudent = []
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
    else:
        modeType = 0
        counter = 0

    cv2.imshow("Face Attendance", imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
