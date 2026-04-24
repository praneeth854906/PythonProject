import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# -----------------------------
# 1. Classes & Inheritance
# -----------------------------
class Sensor:  # Base Class
    def __init__(self, location):
        self.location = location

    def read_data(self):
        pass


class AirSensor(Sensor):  # Inherited Class
    def read_data(self):
        return {
            "PM2.5": random.randint(10, 150),
            "PM10": random.randint(20, 200),
            "CO": round(random.uniform(0.5, 5.0), 2)
        }


# -----------------------------
# 2. File Handling + Pandas
# -----------------------------
class DataHandler:
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, data):
        df = pd.DataFrame([data])
        df.to_csv(self.filename, mode='a', header=False, index=False)

    def load_data(self):
        try:
            df = pd.read_csv(self.filename)
            df.columns = ["PM2.5", "PM10", "CO"]
            return df
        except FileNotFoundError:
            print("❌ File not found!")
            return pd.DataFrame()


# -----------------------------
# 3. Analysis using NumPy
# -----------------------------
class Analyzer:
    def calculate_average(self, df):
        return {
            "PM2.5_avg": np.mean(df["PM2.5"]),
            "PM10_avg": np.mean(df["PM10"]),
            "CO_avg": np.mean(df["CO"])
        }


# -----------------------------
# 4. Visualization (Matplotlib)
# -----------------------------
class Visualizer:
    def plot_data(self, df):
        plt.figure(figsize=(8, 5))
        plt.plot(df["PM2.5"], label="PM2.5")
        plt.plot(df["PM10"], label="PM10")
        plt.plot(df["CO"], label="CO")
        plt.title("Air Quality Monitoring")
        plt.xlabel("Readings")
        plt.ylabel("Values")
        plt.legend()
        plt.show()


# -----------------------------
# 5. Main Program + Exceptions
# -----------------------------
def main():
    sensor = AirSensor("Hyderabad")
    handler = DataHandler("air_quality.csv")
    analyzer = Analyzer()
    visualizer = Visualizer()

    try:
        # Generate & store data
        for i in range(10):
            data = sensor.read_data()
            handler.save_data(data)

        # Load data
        df = handler.load_data()
        if df.empty:
            print("⚠ No data available!")
            return

        # Analyze data
        avg = analyzer.calculate_average(df)
        print("\n📊 Average Air Quality Values:")
        for key, value in avg.items():
            print(f"{key}: {value:.2f}")

        # Visualization
        visualizer.plot_data(df)

    except Exception as e:
        print("⚠ Error occurred:", e)


# Run program
if __name__ == "__main__":
    main()
