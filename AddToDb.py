import os
import pickle
import cv2
import face_recognition
import pandas as pd
from datetime import datetime, timedelta

def saveStudentDetails(key, name, starting_year, year):
    previous_day = datetime.now() - timedelta(days=1)
    previous_day_str = previous_day.strftime('%Y-%m-%d')
    data = {
        "id": [str(key)],
        "name": [name],
        "starting_year": [str(starting_year)],
        "year": [str(year)],
        "major": ["CMSA"],
        "total_attendance": [str(0)],
        "last_attendance_date": [previous_day_str]
    }
    df = pd.DataFrame(data)
    df.to_csv("Database/attendance.csv", mode='a', index=False, header=not os.path.exists("Database/attendance.csv"))
    print("Data saved")

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


def saveStudentImages():
    folderPath = 'Database/Images'
    pathList = os.listdir(folderPath)
    print(pathList)
    imgList = []
    studentIds = []
    for path in pathList:
        imgList.append(cv2.imread(os.path.join(folderPath, path)))
        studentIds.append(os.path.splitext(path)[0])

    print("Encoding Started ...")
    encodeListKnown = findEncodings(imgList)
    encodeListKnownWithIds = [encodeListKnown, studentIds]
    print("Encoding Complete")

    file = open("EncodeFile.p", 'wb')
    pickle.dump(encodeListKnownWithIds, file)
    file.close()
    print("File Saved")



