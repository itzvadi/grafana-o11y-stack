# Grafana Observability Stack (Alloy + Loki + Mimir)

![Grafana Observability Stack](./diagrams/grafana-olly-stack.jpg)

## Overview

This is a demo observability setup that you can run on either **MacOS** or **Linux**. It uses the latest **Grafana OSS stack**, including:

* **Alloy** (successor to Promtail + Agent) for collecting and forwarding telemetry data
* **Loki** for storing and querying logs
* **Mimir** for storing metrics (Prometheus-compatible)
* **Grafana** for visualization (single pane for metrics + logs)

The goal is to demonstrate how a minimal, self-contained observability stack can be used to collect logs and metrics from a local system using Docker Compose.

---

## Stack Components

| Component         | Role            | Default Port | Description                                           |
| ----------------- | --------------- | ------------ | ----------------------------------------------------- |
| **Alloy**         | Collector       | `12345`      | Central collector and forwarder of logs and metrics   |
| **Loki**          | Logs backend    | `3100`       | Stores and queries log data                           |
| **Mimir**         | Metrics backend | `9009`       | Stores time-series metrics (Prometheus-compatible)    |
| **Grafana**       | Visualization   | `3000`       | Dashboard for viewing metrics and logs                |
| **Node Exporter** | Metrics source  | `9100`       | Collects host-level metrics from the monitored system |

---

## Prerequisites

* Docker
* Docker Compose
* Unix-like system (Linux or MacOS)

---

## Running the Stack

```bash
# Start all services in detached mode
docker compose up -d

# Shut down and remove volumes
docker compose down -v
```

You should wait a few seconds for all services to initialize.

---

## Accessing the Services

| Service               | URL                                                            |
| --------------------- | -------------------------------------------------------------- |
| Grafana               | [http://localhost:3000](http://localhost:3000)                 |
| Mimir (Push Endpoint) | `http://localhost:9009/api/v1/push`                            |
| Loki (Push Endpoint)  | `http://localhost:3100/loki/api/v1/push`                       |
| Node Exporter         | [http://localhost:9100/metrics](http://localhost:9100/metrics) |

---

## Dashboards

### ✅ Node Exporter Full (Auto-Provisioned)

The **Node Exporter Full** dashboard (ID: **1860**) is automatically installed via provisioning using the JSON file placed in the Grafana provisioning folder.

You don’t need to import it manually — simply open Grafana and navigate to the dashboard list to find it ready to use.

This dashboard provides a comprehensive overview of system resource metrics, including:

- CPU usage  
- Memory usage  
- Disk I/O  
- Network throughput  

Ensure your data source is configured to a Mimir or Prometheus-compatible endpoint for the metrics to display correctly.


### 🛠️ Work in Progress: Loki Logs + Python Log Generator

We are currently working on:

* A **Loki-based dashboard** to view logs forwarded by Alloy from `/var/log/*.log`
* A **Python script** to generate sample logs for testing Loki and filtering scenarios

These will be added soon in the `tools/` and `dashboards/` folders.

---

## Project Structure

```
├── diagrams/
│   └── grafana-olly-stack.jpg         # Architecture diagram
├── dashboards/                        # (Planned) Grafana JSON dashboards
├── tools/                             # (Planned) Python log generator script
├── docker-compose.yml                # Full service definition
├── alloy-config.hcl                  # Alloy configuration
└── README.md                         # This file
```

---

## Credits

Created by **itzvadi** for learning and demo purposes.

If you like it, feel free to ⭐️ the repo and fork it!
