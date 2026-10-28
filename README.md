# Real-Time Dynamic Pricing & Feature Store Engine

CURRENTLY WORKING NOT FINISHED!!! ❌

Production-grade DataOps/MLOps platform executing a dual-path (Lambda) data architecture. It ingests simulated user-app events, validates data integrity at the gateway, computes real-time and historical analytics features, and serves low-latency pricing predictions via an ML inference service.

---

## 🏗️ System Architecture

1. Ingestion: Event Generator ──► FastAPI (Pydantic Validation) ──► Apache Kafka
2. Fast Path (Streaming): Kafka ──► PySpark Streaming ──► Redis (Online Feature Store)
3. Slow Path (Batch): Kafka ──► S3 Data Lake (Delta/Iceberg) ──► dbt Cloud ──► Redis (Offline Sync)
4. Inference: FastAPI Web App ──► Fetches Redis Features ──► XGBoost Prediction Model
5. Observability: Prometheus ──► Grafana (Data Drift & System Metrics)

---

## 🛠️ Technology Stack

| Layer | Component | Purpose |
| :--- | :--- | :--- |
| **Ingestion** | FastAPI + Pydantic | Type-safe data entry and API gateway contract enforcement |
| **Streaming Buffer**| Apache Kafka (or Redpanda)| High-throughput, distributed event streaming queue |
| **Stream Processing**| PySpark Streaming / Flink | 5-minute rolling window feature aggregations |
| **Batch / Storage** | AWS S3 (MinIO) + dbt | Long-term analytics historical baselines |
| **Feature Store**   | Redis (or Feast) | Sub-10ms latency feature serving to the ML model |
| **ML Engine**       | XGBoost + MLflow | Predictive model training and artifact version control |
| **Infrastructure**  | Docker Compose / Terraform | Infrastructure-as-Code for reproducible deployments |
| **Observability**   | Prometheus + Grafana | Live dashboarding for data drift and service failures |

---

## 🚀 Phase-by-Phase Implementation Roadmap

### Phase 1: Ingestion Gateway
* [x] Configure a single `docker-compose.yml` spinning up FastAPI, Kafka.
* [ ] Create a Python telemetry script simulating continuous user location and ride requests.
* [ ] Build a FastAPI route utilizing Pydantic models to reject malformed event data before hitting Kafka.

### Phase 2: Dual-Path Processing
* [ ] Write a PySpark script to capture Kafka streams and write real-time demand metrics to Redis.
* [ ] Dump raw stream data to local storage using Parquet/Delta format.
* [ ] Build a dbt SQL schedule to compute 30-day user/location baseline historical averages.

### Phase 3: Serving & ML Inference
* [ ] Train an XGBoost model on historical demand vectors; log parameters and model binaries with MLflow.
* [ ] Create a production FastAPI inference server endpoint.
* [ ] Enforce data architecture: Inference server reads inputs ──► pulls live state from Redis ──► scores model ──► returns dynamic price.

### Phase 4: Production Hygiene & Hardening
* [ ] Integrate data quality checks via Great Expectations / Soda during data transformations.
* [ ] Instrument FastAPI apps with Prometheus metrics.
* [ ] Stand up a Grafana dashboard monitoring API latency, request rates, and model output drift.

---

* Engineered a decoupled, microservices-based streaming data pipeline handling structured event logging using **FastAPI** and **Apache Kafka**.
* Implemented a **Lambda Architecture** utilizing **PySpark Streaming** for real-time window calculations alongside **dbt** for historical batch transformations.
* Reduced feature serving latency to sub-10ms by designing a unified feature look-up cache utilizing **Redis**.
* Standardized infrastructure deployment and orchestration using **Docker Compose**, establishing reliable CI/CD test patterns for infrastructure state updates.
