# DynamicLoad: HealthAware 🚀

A real-time, resource-aware Load Balancer prototype that bridges the gap between high-level routing logic and low-level system telemetry.

## 📌 Project Overview
DynamicLoad is designed to demonstrate how **Data Structures (Min-Heaps)** and **Operating System Metrics** work together to optimize server distribution. It captures real-time CPU and RAM utilization from the host machine to make intelligent routing decisions.

## 🛠️ Key Features
- **Live Hardware Telemetry:** Integrated `psutil` to fetch real-time CPU and Memory pressure.
- **Efficient Routing:** Uses a **Min-Heap (O(log N))** data structure to ensure the "healthiest" node is always selected first.
- **Weighted Heuristics:** Implements a custom health-score formula: `(CPU * 0.7) + (RAM * 0.3)`.
- **Visual Dashboard:** Built with **Streamlit** to provide a real-time observability layer for system administrators.

## 💻 Tech Stack
- **Language:** Python 3.13+
- **Libraries:** Streamlit, Psutil, Pandas, Heapq
- **Concepts:** Distributed Systems, DSA, Operating Systems

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/DynamicLoad.git](https://github.com/YOUR_USERNAME/DynamicLoad.git)
