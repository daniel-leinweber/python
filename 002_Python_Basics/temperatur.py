#!/usr/bin/env python3


def get_temperature():
    while True:
        celsius = input("Temperature in °C: ")
        try:
            celsius = float(celsius)
            return celsius
        except ValueError:
            print("Please provide a valid temperature")


def convert_to_kelvin(celsius):
    return celsius + 273.15


if __name__ == "__main__":
    celsius = get_temperature()
    kelvin = convert_to_kelvin(celsius)
    print(f"Temperature in Kelvin: {kelvin}")
