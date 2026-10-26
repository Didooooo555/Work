from ultralytics import YOLO
import cv2

# Загружаем YOLOv8 модель (можно заменить на yolov8s.pt, yolov8m.pt и т.д.)
model = YOLO('yolov8n.pt')  # nano-версия (быстрая)

# Открываем видео
cap = cv2.VideoCapture("ty.mp4")  

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Обработка кадра через YOLO
    results = model(frame, conf=0.4)  # conf — минимальная уверенность

    # Получаем информацию о найденных объектах
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]
            if class_name == "car":  # Показываем только машины
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                label = f"{class_name} {confidence:.2f}"
                
                # Рисуем прямоугольник
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                cv2.putText(frame, label, (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Показываем результат
    cv2.imshow("Car Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

