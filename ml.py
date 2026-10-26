import subprocess

while True:
    p = input("Вы: ")

    result = subprocess.run(
        ["ollama", "run", "gemma3:4b"],
        input=p.encode("utf-8"),   # подаём в utf-8
        capture_output=True
    )

    print("ИИ:", result.stdout.decode("utf-8"))

