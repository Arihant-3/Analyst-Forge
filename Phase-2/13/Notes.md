### Answer

1. Done

2. Done

3. Done

4. - Total anomalies detected: 8

- Top 3 anomalies with largest deviations:
      |    Date	    |  Sensor_Value	    |       Z       |
      | ----------- | ----------------- | ------------- |
	  | 2023-02-01	|  89.261391	    |    5.864843   |
	  | 2023-09-06	|  88.827271	    |    5.799547   |
	  | 2023-11-22	|  18.929057	    |   -4.713814   |

5.  - Z-Score Thresholding
        - Use a rolling window to adaptively calculate the mean and standard deviation, then flag values that deviate too much.  
        🔹 Why it's good: Reacts to shifts in the data, unlike static thresholds  
        🔹 Best for: Gradually drifting data or seasonal trends
    - Isolation Forest (Machine Learning Approach)
        - Train a model that learns the "normal behavior" of the sensor and flags unusual patterns.  
        🔹 Why it's good: Doesn’t assume normal distribution  
        🔹 Best for: Complex patterns or multidimensional sensor data

---

- **What is the range of normal variation?**  
Range of normal variation (approx): 30.30 to 70.24

- **Could time-of-day or seasonality explain the anomalies?**  
No, time-of-day or seasonality doesn't explain the anomalies.

- **How would you build an alerting rule?**  

    1. Z-score Thresholds:
    - Automatically alert if |z| > 3, and flag higher-priority alerts at |z| > 4.

    2. Moving Average Window:
    - Use rolling mean & standard deviation to detect local anomalies (helps adapt to gradual drift).

    3. Rate of Change Alert:
    - Trigger alerts if value changes more than X% within Y minutes (for real-time sensors).

    4. Anomaly + Frequency:
    - If more than 2 anomalies are detected in a 7-day period → raise system health alert.


