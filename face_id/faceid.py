import cv2
import time
from deepface import DeepFace

# Загружаем эталонное фото
reference_image_path = "my.jpg"
reference_img = cv2.imread(reference_image_path)

if reference_img is None:
    print("❌ Ошибка: файл 'my.jpg' не найден.")
    exit()

# Включаем камеру
cap = cv2.VideoCapture(0)
print("📸 Камера запущена. Ожидание...")

recognized = False
checked = False
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Не удалось получить кадр с камеры.")
        break

    # Показываем камеру
    cv2.imshow("Face ID", frame)

    # Проверка через 2 секунды
    if not checked and time.time() - start_time > 2:
        print("🔍 Распознавание (ускоренное)...")
        try:
            result = DeepFace.verify(
            img1_path=frame,
            img2_path=reference_img,
            model_name="Facenet",  # или VGG-Face
            enforce_detection=False
)

            if result["verified"]:
                print("✅ Лицо распознано")
            else:
                print("❌ Лицо не совпадает")

        except Exception as e:
            print("⚠ Ошибка:", e)

        checked = True

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
