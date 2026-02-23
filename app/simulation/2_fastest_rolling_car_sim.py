import math

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Fastest Rolling Car Simulation")

st.write(""" This is a physics simulation of an off-center wheel rolling down 
         a sloped track. We can simulate to find out the best time to 
         reach finish line with configurable track length, track slope, 
         and the off-center weight distance ratio and most importantly, 
         off-center angle, tilting up (0 degree) and forward (90 degree). 
         """)

# Simulation parameters
mass = 10
simulation_time = 15
wheel_radius = 2.0

col1, col2 = st.columns([1, 1])
with col1:
    slope_length = st.slider("Track length", 1, 5, 2)
    center_offset = st.slider("Weight offset from center", 0.0, 1.0, 0.0)

with col2:
    slope_angle = st.slider("Slope angle (degrees)", 5, 45, 15)
    weight_start_angle = st.slider("Weight start angle (degrees)", -180, 180, 40)

# track length is multiple of wheel circumference
slope_length = slope_length * 2 * math.pi * wheel_radius
center_offset = center_offset * wheel_radius  # convert to actual distance


# Physics simulation
def simulate_rolling_wheel(
    angle_deg,
    radius,
    offset,
    mass,
    target_distance,
    max_duration,
    start_angle_deg=0,
):
    angle_rad = math.radians(angle_deg)
    g = 9.81
    dt = 0.001
    max_steps = int(max_duration / dt)

    # Initial conditions
    x, v, angular_vel = 0, 0, 0
    theta = math.radians(
        start_angle_deg
    )  # Wheel rotation angle (start position of off-center weight)

    # Store history
    times = []
    positions = []
    velocities = []
    rotations = []

    for i in range(max_steps):
        # Moment of inertia (disk + point mass offset)
        I = mass * offset**2

        # Forces and torques
        gravity_component = mass * g * math.sin(angle_rad)
        # torque from off-center weight (depends on wheel rotation angle)
        torque_weight = mass * g * offset * math.sin(theta)
        # convert torque to an equivalent tangential force at rim
        force_from_torque = torque_weight / radius

        # include rotational inertia by adding I/r^2 to effective mass
        effective_mass = mass + I / (radius**2)

        # net force along slope includes gravity component, torque-contribution, minus resistance
        net_force = gravity_component + force_from_torque

        # acceleration accounting for rotational inertia
        acceleration = net_force / effective_mass
        v += acceleration * dt
        x += v * dt

        # Angular velocity from rolling constraint and update rotation
        angular_vel = v / radius
        theta += angular_vel * dt

        times.append(i * dt)
        positions.append(x)
        velocities.append(v)
        # store cumulative rotation (radians) so total rotations is the full number
        rotations.append(theta - math.radians(start_angle_deg))

        # stop if we've reached the end of the slope
        if x >= target_distance:
            finish_time = (i + 1) * dt
            break
    else:
        finish_time = None

    return (
        np.array(times),
        np.array(positions),
        np.array(velocities),
        np.array(rotations),
        finish_time,
    )


# Run simulation
times, positions, velocities, rotations, finish_time = simulate_rolling_wheel(
    slope_angle,
    wheel_radius,
    center_offset,
    mass,
    slope_length,
    simulation_time,
    weight_start_angle,
)

# Display Simulation Result
st.subheader("Simulation Result")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Time to Finish", f"{finish_time:.3f} s")
col2.metric("Final Distance", f"{positions[-1]:.3f} m")
col3.metric("Total Rotations", f"{rotations[-1] / (2 * np.pi):.2f}")
col4.metric("Final Velocity", f"{velocities[-1]:.3f} m/s")

# Display results
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distance vs Time")
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(times, positions, "b-", linewidth=2)
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Distance down slope (m)")
    ax1.grid(True, alpha=0.3)
    st.pyplot(fig1)

with col2:
    st.subheader("Velocity vs Time")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.plot(times, velocities, "r-", linewidth=2)
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Velocity (m/s)")
    ax2.grid(True, alpha=0.3)
    st.pyplot(fig2)
