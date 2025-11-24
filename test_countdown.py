import requests

COUNTDOWN_URL = "http://127.0.0.1:5002/countdown"

def main():
    print("=== Countdown Microservice Test ===")
    date_str = input("Enter a deadline (YYYY-MM-DD or YYYY-MM-DDTHH:MM): ").strip()

    try:
        resp = requests.get(COUNTDOWN_URL, params={"date": date_str}, timeout=5)
    except Exception as e:
        print("Could not reach countdown service:", e)
        return

    print("\nStatus Code:", resp.status_code)
    try:
        data = resp.json()
    except Exception:
        print("Invalid JSON:", resp.text)
        return

    print("\nRaw JSON:", data)

    if resp.status_code == 200:
        print("\nHuman-readable:", data.get("human", ""))
    else:
        print("\nError:", data)

if __name__ == "__main__":
    main()
