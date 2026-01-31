import streamlit as st
import psutil
import heapq
import time
import random

st.set_page_config(page_title="DynamicLoad Dashboard", layout="wide")

st.title("🚀 DynamicLoad: Hardware-Aware Balancer")
st.markdown("### Real-time System Telemetry & Min-Heap Routing")

status_placeholder = st.empty()
decision_placeholder = st.empty()

nodes = ["Node_Alpha", "Node_Beta", "Node_Gamma"]

while True:
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    
    status_placeholder.metric("Local CPU Usage", f"{cpu}%")
    
    min_heap = []
    display_list = []
    
    for node in nodes:
        load = (cpu * 0.7 + mem * 0.3) if node == "Node_Alpha" else random.randint(10, 90)
        heapq.heappush(min_heap, (load, node))
        display_list.append(f"{node}: {load:.2f}% Load")
    
    best_load, best_node = heapq.heappop(min_heap)
    
    with decision_placeholder.container():
        st.write("---")
        st.write("### Current Server Status (Min-Heap View)")
        for item in display_list:
            st.text(item)
            
        st.success(f"**Target Node Selected:** {best_node}")
        st.info(f"**Decision Logic:** Found minimum Resource Pressure ({best_load:.2f}%) using Min-Heap.")
        
    time.sleep(1)
