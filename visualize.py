import matplotlib.pyplot as plt

def plot_file_activity(events):
    """
    Plots File Count vs Time graph
    """

    # If no events, do nothing
    if not events:
        print("No events to visualize")
        return

    # Extract timestamps
    times = [event[0] for event in events]

    # Convert absolute time → relative time
    start_time = times[0]
    relative_times = [t - start_time for t in times]

    # File count increases by 1 for each event
    file_counts = list(range(1, len(events) + 1))

    # Plot graph
    plt.plot(relative_times, file_counts, marker='o')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Number of Files Modified")
    plt.title("File Modification Rate Over Time")

    plt.grid(True)
    plt.show()
