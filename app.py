import streamlit as st
import psutil
import heapq
import time
import random
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="DynamicLoad: High-Availability Balancer", layout="wide")
st.title("🛡️ DynamicLoad: Fault-Tolerant Balancer")
st.markdown("---")

# 2. Sidebar for Manual Control (The "Crash Simulation")
st.sidebar.header("🕹️ Control Panel")
simulation_mode = st.sidebar.toggle("Simulate Network Fluctuations", value=True)
nodes_to_list = ["Node_Alpha (Local)", "Node_Beta", "Node_Gamma", "Node_Delta"]
crashed_node = st.sidebar.selectbox("Simulate a Node Crash:", ["None"] + nodes_to_list)

# 3. Placeholders for clean UI updates (Prevents scrolling/infinite printing)
placeholder = st.empty()

while True:
    # --- STEP 1: Telemetry (The Sensory Unit) ---
    local_cpu = psutil.cpu_percent(interval=1)
    
    # --- STEP 2: The Heartbeat & Guardrails (The Brain) ---
    min_heap = []
    full_status_report = []
    
    for node in nodes_to_list:
        # Check if node is 'Alive' based on user selection
        is_alive = False if node == crashed_node else True
        
        # Calculate Load: Real for local, Simulated for others
        if "Local" in node:
            load = local_cpu
        else:
            load = random.randint(20, 80) if simulation_mode else 50
        
        # THE GUARDRAIL: Only push to Heap if the 'Heartbeat' is healthy
        if is_alive:
            heapq.heappush(min_heap, (load, node))
            status = "🟢 Online"
        else:
            status = "🔴 Offline (Crashed)"
            # Note: We set load to 0 for display, but it's ignored by the heap
            load = 0 
            
        full_status_report.append({"Server": node, "Load (%)": load, "Status": status})

    # --- STEP 3: The Face (UI Updates inside the Placeholder) ---
    with placeholder.container():
        # Metric Row
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🖥️ Local CPU Usage", f"{local_cpu}%", delta=f"{local_cpu-50}%", delta_color="inverse")
        with col2:
            st.metric("📡 Active Nodes", f"{len(min_heap)} / {len(nodes_to_list)}")

        st.divider()

        # Decision Logic & Error Handling for "All Server Crash"
        st.subheader("⚖️ Decision Engine")
        if min_heap:
            best_load, best_node = heapq.heappop(min_heap)
            st.success(f"🎯 **Targeting: {best_node}**")
            st.info(f"The algorithm selected the healthiest node with **{best_load}%** load.")
        else:
            st.error("🚨 **CRITICAL SYSTEM FAILURE: NO NODES AVAILABLE**")
            st.warning("All heartbeats failed. Incoming traffic is being queued.")

        # Status Table
        st.write("### 📊 Network Status Report")
        st.table(pd.DataFrame(full_status_report))

    # Time delay is handled by psutil.cpu_percent(interval=1)
