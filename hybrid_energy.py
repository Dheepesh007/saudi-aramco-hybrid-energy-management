# SESSION 29 – SAUDI ARAMCO (Hybrid Energy)

def check_battery_mode(battery_level, threshold=20):
    if battery_level < threshold:
        return "Switch to Charging Mode"
    else:
        return "Normal Operation"

def main():
    battery_level = 18  # in percentage

    mode = check_battery_mode(battery_level)

    print("Battery Level:", battery_level, "%")
    print("Mode:", mode)

if __name__ == "__main__":
    main()
