import yaml
import time
import requests
from urllib.parse import urlparse

def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def check_endpoint(endpoint):
    url = endpoint.get('url')
    method = endpoint.get('method', 'GET').upper()
    headers = endpoint.get('headers', {})
    body = endpoint.get('body')

    try:
        start_time = time.time()
        response = requests.request(method, url, headers=headers, data=body, timeout=5)
        latency = (time.time() - start_time) * 1000
        is_up = 200 <= response.status_code < 300 and latency < 500
        return is_up, latency
    except requests.RequestException:
        return False, None

def log_availability(stats):
    for domain, data in stats.items():
        availability = round(100 * data['up'] / data['total'])
        print(f"{domain} has {availability}% availability percentage")

def track_availability(endpoints):
    domain_stats = {}
    while True:
        for endpoint in endpoints:
            url = endpoint['url']
            domain = urlparse(url).netloc

            is_up, _ = check_endpoint(endpoint)
            if domain not in domain_stats:
                domain_stats[domain] = {'up': 0, 'total': 0}
            domain_stats[domain]['total'] += 1
            if is_up:
                domain_stats[domain]['up'] += 1

        log_availability(domain_stats)
        time.sleep(15)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_config>")
        sys.exit(1)

    config_path = sys.argv[1]
    config = load_config(config_path)
    track_availability(config)