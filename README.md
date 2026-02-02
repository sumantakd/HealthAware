# 🛡️ DynamicLoad: High-Availability Fault-Tolerant Balancer

**DynamicLoad** is a hardware-aware load balancing engine built with Python. It optimizes task routing across distributed network nodes using real-time telemetry and a Min-Heap data structure, ensuring zero-downtime through an integrated "Heartbeat" monitoring system.

---

## 🚀 Key Features

* **Real-Time Telemetry:** Interfaces with the OS kernel via `psutil` to fetch live CPU utilization metrics.
* **$O(\log N)$ Algorithmic Routing:** Utilizes a **Min-Heap** priority queue to instantly identify the healthiest node in the network.
* **Fault Tolerance (Heartbeat):** Implements a pre-processing guardrail that automatically detects and bypasses crashed or unresponsive nodes.
* **High Observability Dashboard:** A reactive UI built with **Streamlit** featuring live metrics, status reports, and a manual "Crash Simulation" control panel.
* **Fail-Safe Logic:** Graceful degradation handling for "Total System Failure" scenarios.

---

## 🏗️ System Architecture

1.  **Sensory Layer:** Collects hardware resource data from the local machine and simulates peer nodes.
2.  **Logic Layer (The Brain):** Filters nodes based on health status (Heartbeat) and organizes them into a Min-Heap using **Lexicographical Tuple Comparison**.
3.  **Presentation Layer (The Face):** Provides a Single Page Application (SPA) experience using **Atomic UI Updates** to prevent memory bloat.



---

## 🛠️ Technical Deep Dive

### The "Black Hole" Prevention
In distributed systems, a crashed server often reports **0% CPU usage**. A naive load balancer would see this "0" as the best option and send all traffic to a dead server. 
**DynamicLoad** solves this by implementing a **Boolean Health Check** before the data enters the Min-Heap. If the Heartbeat fails, the node is quarantined, regardless of its reported load.

### Efficiency
* **Selection:** $O(1)$ to peek at the root.
* **Insertion/Re-balancing:** $O(\log N)$ using `heapq`.

---

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/DynamicLoad.git](https://github.com/yourusername/DynamicLoad.git)
   cd DynamicLoad
