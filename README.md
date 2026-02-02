# 🛡️ HealthAware: Hardware-Centric Distributed Load Balancer

**HealthAware** is a high-availability load balancing engine built with Python. Unlike naive balancers that only look at traffic, HealthAware focuses on the "physical health" of the nodes—utilizing real-time telemetry and a Min-Heap data structure to ensure tasks are only routed to healthy, high-performance servers.

---

## 🚀 Key Features

* **Hardware-Centric Routing:** Interfaces with the OS kernel via `psutil` to fetch live CPU and memory metrics.
* **$O(\log N)$ Algorithmic Logic:** Uses a **Min-Heap** priority queue to identify the healthiest node in constant time ($O(1)$ at the root).
* **Fault Tolerance (Heartbeat):** Implements a pre-processing guardrail that detects and bypasses "Zombie" nodes (crashed servers reporting 0% load).
* **High Observability UI:** A reactive dashboard built with **Streamlit** featuring live telemetry, network status reports, and a manual "Crash Simulation" panel.
* **Fail-Safe Mode:** Graceful degradation logic for scenarios where the entire node registry fails.

---

## 🏗️ System Architecture

1.  **Sensory Layer:** Collects hardware resource data from the local machine and simulates peer nodes via API patterns.
2.  **Logic Layer (The Brain):** Filters nodes based on health status and organizes them into a Min-Heap using **Lexicographical Tuple Comparison**.
3.  **Presentation Layer (The Face):** Provides a Single Page Application (SPA) experience using **Atomic UI Updates** to prevent memory bloat.



---

## 🛠️ Technical Deep Dive

### The "HealthAware" Difference
Most basic balancers fall into the **"Black Hole Trap"**: A crashed server stops processes, leading to 0% CPU usage. A naive balancer sees "0" and incorrectly assumes that server is the best option. 
**HealthAware** avoids this by requiring a **Boolean Heartbeat** before any load data is considered. If a server is offline, it is quarantined from the decision-making engine entirely.

### Complexity Analysis
* **Node Selection:** $O(1)$ (Peeking at the root).
* **Queue Re-balancing:** $O(\log N)$ using `heapq`.
* **Telemetry Fetch:** $O(1)$ per node.

---

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/HealthAware.git](https://github.com/yourusername/HealthAware.git)
   cd HealthAware
