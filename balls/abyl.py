from inference_sdk import InferenceHTTPClient
import os
import cv2

image_path = "balls/american1football.jpg"  

print("Файл существует:", os.path.exists(image_path))

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com", 
    api_key="o5zrLS0K3Fax3PBYbvv2"
)

result = client.run_workflow(
    workspace_name="didar",
    workflow_id="classify-and-conditionally-detect-2",
    images={"image": image_path},  
    use_cache=True
)

print("Результат:", result[0]['top_class'])


img = cv2.imread(image_path)
cv2.imshow("classify-and-conditionally-detect-2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
