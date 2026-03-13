import requests
import time
import numpy as np
from sklearn.ensemble import IsolationForest
import datetime

# Prometheus URL
PROMETHEUS_URL = "http://localhost:9090"

def get_metrics():
    try:
        response = requests.get(
            f"{PROMETHEUS_URL}/api/v1/query",
            params={'query': 'app_request_count_total'}
        )
        data = response.json()
        results = data['data']['result']
        total = sum(float(r['value'][1]) for r in results)
        return total
    except:
        return 0

def detect_anomaly(data):
    if len(data) < 10:
        return False
    model = IsolationForest(contamination=0.1)
    arr = np.array(data).reshape(-1, 1)
    model.fit(arr)
    prediction = model.predict([arr[-1]])
    return prediction[0] == -1

def main():
    print("🤖 AI Monitor Started!")
    metrics_history = []

    while True:
        value = get_metrics()
        metrics_history.append(value)
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{now}] Request count: {value}")

        if detect_anomaly(metrics_history):
            print(f"🚨 ANOMALY DETECTED at {now}! Value: {value}")
        else:
            print(f"✅ Normal at {now}")

        time.sleep(30)

if __name__ == '__main__':
    main()