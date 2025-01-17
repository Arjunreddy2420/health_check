# HTTP Endpoint Health Monitor

A Python application that monitors HTTP endpoints and tracks their availability percentage over time. The program performs health checks every 15 seconds and displays the availability statistics for each domain[1].

## Features

**The monitor checks if endpoints are:**
* Responding with **200-299** status codes
* Responding within **500ms** latency threshold
* Accessible via **GET** and **POST** methods
* Supporting custom headers and request bodies[1]

## Requirements

**Core Requirements:**
* Python 3.7+
* Required packages:
```bash
PyYAML
requests
```

## Installation

**Setup Steps:**
1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```



## Configuration

A sample YAML configuration file (`config.yaml`) is already included in the repository. You can edit this file to add or modify the endpoints you want to monitor. The format of the file is as follows:

```yaml
- name: My Website
  url: https://example.com
  method: GET
  headers:
    user-agent: my-monitor
```

**Required fields:**
* **name**: Description of the endpoint
* **url**: The HTTP/HTTPS endpoint to monitor

**Optional fields:**
* **method**: HTTP method (defaults to GET)
* **headers**: Custom HTTP headers
* **body**: JSON request body for POST requests

## Usage

Run the monitor with:
```bash
python main.py config.yaml
```

**The program will:**
* Load endpoints from your YAML file
* Run health checks every **15 seconds**
* Display availability percentages for each domain
* Continue until manually stopped (**CTRL+C**)

## Example Output
```text
example.com has 100% availability percentage
api.example.com has 85% availability percentage
```

## How It Works

**Endpoint Status:**
* **UP**: Response code 200-299 and latency < 500ms
* **DOWN**: Any other response

**Availability Calculation:**
```
Availability % = (UP requests / Total requests) × 100
```

