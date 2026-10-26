import cv2
import face_recognition
import os
import numpy as np
import datetime

known_faces_dir = 'known_faces'
if not os.path.exists(known_faces_dir):
    os.makedirs(known_faces_dir)

# 📁 Загрузка известных лиц
def load_known_faces():
    encodings = []
    names = []
    for filename in os.listdir(known_faces_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(path)
            face_encs = face_recognition.face_encodings(image)
            if face_encs:
                encodings.append(face_encs[0])
                names.append(os.path.splitext(filename)[0])
    return encodings, names

known_face_encodings, known_face_names = load_known_faces()

# 📷 Веб-камера
cap = cv2.VideoCapture(0)

print("Нажмите 'r' чтобы зарегистрировать новое лицо.")
print("Нажмите 'q' чтобы выйти.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
        name = "Неизвестен"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if face_distances.size > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

        # Логируем в консоль
        print(f"[{datetime.datetime.now()}] Распознано: {name}")

    cv2.imshow('Face ID', frame)

    key = cv2.waitKey(1) & 0xFF

    # Регистрируем новое лицо
    if key == ord('r'):
        if len(face_locations) == 1:  # только если одно лицо в кадре
            face_image = frame[top:bottom, left:right]
            new_name = input("Введите имя для регистрации: ").strip()
            if new_name:
                file_path = os.path.join(known_faces_dir, f"{new_name}.jpg")
                cv2.imwrite(file_path, face_image)
                print(f"Лицо сохранено как {file_path}")

                # Обновляем базу лиц
                known_face_encodings, known_face_names = load_known_faces()
            else:
                print("Имя не введено, регистрация отменена.")
        else:
            print("Для регистрации должно быть только одно лицо в кадре!")

    # Выход по 'q'
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
 