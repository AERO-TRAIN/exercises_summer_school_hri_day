import rosbag
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

# Path to the rosbag file
rosbag_path = "/home/oem/Downloads/ccgrid.bag"

# Lists to store data
timestamps = []
downlink_delay = []
odom_data = {"estimated": [], "actual": [], "ground_truth": [], "setpoint": []}
odom_timestamps = {"estimated": [], "actual": [], "ground_truth": [], "setpoint": []}

# Open the rosbag
with rosbag.Bag(rosbag_path, 'r') as bag:
    for topic, msg, t in bag.read_messages():
        timestamp = t.to_sec()
        
        if topic == "/downlink_delay":
            timestamps.append(timestamp)
            downlink_delay.append(msg.data)
        
        elif topic == "/estimated_odometry":
            odom_timestamps["estimated"].append(timestamp)
            odom_data["estimated"].append((msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z))
        
        elif topic == "/odometry":
            odom_timestamps["actual"].append(timestamp)
            odom_data["actual"].append((msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z))
        
        elif topic == "/pelican/ground_truth/odometry":
            odom_timestamps["ground_truth"].append(timestamp)
            odom_data["ground_truth"].append((msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z))
        
        elif topic == "/setpoint_position":
            odom_timestamps["setpoint"].append(timestamp)
            odom_data["setpoint"].append((msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z))

# Convert lists to numpy arrays for easy computation
timestamps = np.array(timestamps)
downlink_delay = np.array(downlink_delay)

# Convert odometry data to DataFrames
odom_df = {}
for key in odom_data:
    odom_df[key] = pd.DataFrame(odom_data[key], columns=["x", "y", "z"])
    odom_df[key]["timestamp"] = odom_timestamps[key]

# Interpolate to align timestamps for error calculation
setpoint_interp = odom_df["setpoint"].set_index("timestamp").interpolate().reset_index()

def compute_error(df1, df2):
    """Computes Euclidean error between two odometry datasets"""
    df1_interp = df1.set_index("timestamp").interpolate().reset_index()
    merged = pd.merge(df1_interp, df2, on="timestamp", suffixes=("_1", "_2"))
    return merged["timestamp"], np.sqrt((merged["x_1"] - merged["x_2"])**2 +
                                        (merged["y_1"] - merged["y_2"])**2 +
                                        (merged["z_1"] - merged["z_2"])**2)

# Compute errors
t_odom_error, odom_error = compute_error(odom_df["actual"], setpoint_interp)
t_est_error, est_error = compute_error(odom_df["estimated"], setpoint_interp)

if timestamps.size > 0:
    t0 = timestamps[0]  # Get the first timestamp
    timestamps -= t0

for key in odom_timestamps:
    if len(odom_timestamps[key]) > 0:
        odom_timestamps[key] = np.array(odom_timestamps[key]) - t0  # Adjust each odometry timestamp

t_odom_error -= t0
t_est_error -= t0

with plt.style.context(["science", "ieee"]):
    # 1. Plot Downlink Delay
    plt.figure(figsize=(4, 2))
    plt.plot(timestamps, downlink_delay, color='black')
    plt.xlabel(r"$\text{Time} \,\, (s)$", fontsize=10)
    plt.ylabel(r"$\tau(t) \,\, (s)$", fontsize=10)
    plt.legend()
    plt.grid()
    plt.savefig("/home/oem/Downloads/delay.png", bbox_inches="tight")
    plt.show()

    # 2. Plot Odometry Comparison
    fig, axs = plt.subplots(3, 1, figsize=(4, 4), sharex=True)

    axis_labels = [r"$\text{X-Position} \,\, (m)$", r"$\text{Y-Position} \,\, (m)$", r"$\text{Z-Position} \,\, (m)$"]
    colors = ["r", "b", "g"]  # Colors for different odometry sources
    labels = ["Estimated", "Measured", "Reference"]
    keys = ["estimated", "actual", "setpoint"]

    for i, axis in enumerate(["x", "y", "z"]):
        for key, color, label in zip(keys, colors, labels):
            axs[i].plot(odom_timestamps[key], odom_df[key][axis], label=f"{label} {axis}", color=color)

        axs[i].set_ylabel(f"{axis_labels[i]}", fontsize=10)
        axs[i].legend()
        axs[i].grid()

    axs[-1].set_xlabel(r"$\text{Time} \,\, (s)$", fontsize=10)
    plt.savefig("/home/oem/Downloads/odom.png", bbox_inches="tight")
    plt.show()


    # 3. Plot Errors
    plt.figure(figsize=(4, 2))
    plt.plot(t_odom_error, odom_error, label="Measured", color="blue")
    plt.plot(t_est_error, est_error, label="Estimated", color="red")
    plt.xlabel(r"$\text{Time} \,\, (s)$", fontsize=10)
    plt.ylabel(r"$\text{Position Error} \,\, (m)$", fontsize=10)
    plt.legend()
    plt.grid()
    plt.savefig("/home/oem/Downloads/error.png", bbox_inches="tight")
    plt.show()
