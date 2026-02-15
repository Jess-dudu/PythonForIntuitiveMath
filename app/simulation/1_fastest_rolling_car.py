import streamlit as st

st.title("Fastest Rolling Car Competition")

st.write(""" The competition is to design the fastest rolling car along a sloped track. 
         The car will start from rest at the top of the track and roll down under the influence 
         of gravity. The goal is to minimize the time it takes for the car to reach the bottom 
         of the track.""")

st.subheader("Minimizing Rotational Kinetic Energy")

col1, col2 = st.columns([1, 1])

with col1:
    st.write(""" Minimizing rotational kinetic energy can resule in more translational kinetic energy
         and thus a faster car. Lighter big wheels and heavier thin axle are recommended for faster cars.
         However, an easier way is to use a light can full of drink since water is heavy and will not 
         rotate much. A comparison video is shown.
         """)

with col2:
    # Use HTTPS and a standard YouTube watch/embed URL. For Shorts use the video ID.
    video_id1 = "QHD0o-345aA"
    # Streamlit's st.video accepts a watch URL; this will embed the player.
    st.video(f"https://www.youtube.com/watch?v={video_id1}")

st.subheader("Fastest Descending Curve")

col1, col2 = st.columns([1, 1])

with col1:
    st.write(""" If we can curve the track to minimize the running time, the optimal curve is called 
             the brachistochrone curve. This problem was posed by Johann Bernoulli 
            in 1696 and famously solved in one night by Isaac Newton in 1697. Here is an video showing the
            difference between different curves.
            """)

with col2:
    # Use HTTPS and a standard YouTube watch/embed URL. For Shorts use the video ID.
    video_id2 = "H-qNPV4WSsE"
    # Streamlit's st.video accepts a watch URL; this will embed the player.
    st.video(f"https://www.youtube.com/watch?v={video_id2}")

st.subheader("Faster on Straight Slope ?")

col1, col2 = st.columns([1, 1])

with col1:
    st.write(""" We can exploit similar ideas to minimize the time on a straight track by having an off-center mass distribution.
            The rolling will have a wobbling motion but it can start with a faster initial acceleration and slower acceleration when
             mass is rotated to the lowest point (similar to brachistochrone curve effect). To achieve this, the off-center mass 
             should be tilt up and forward at starting point. Here is a video showing such a wheel vs. full coke can.
            """)

with col2:
    # Use HTTPS and a standard YouTube watch/embed URL. For Shorts use the video ID.
    video_id3 = "WsiUnYtABiM"
    # Streamlit's st.video accepts a watch URL; this will embed the player.
    st.video(f"https://www.youtube.com/watch?v={video_id3}")
