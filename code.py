import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

parser = argparse.ArgumentParser(
    description="Convert temperatures between Celsius and Fahrenheit.",
    epilog="Example: python temp_convert.py 100 --to-fahrenheit"
)
parser.add_argument(
    "temperature",
    type=float,
    help="Temperature value to convert"
)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    "-c", "--to-celsius",
    action="store_true",
    help="Convert from Fahrenheit to Celsius"
)
group.add_argument(
    "-f", "--to-fahrenheit",
    action="store_true",
    help="Convert from Celsius to Fahrenheit"
)

args = parser.parse_args()

if args.to_celsius:
    result = fahrenheit_to_celsius(args.temperature)
    print(f"{args.temperature}°F is {result:.2f}°C")
elif args.to_fahrenheit:
    result = celsius_to_fahrenheit(args.temperature)
    print(f"{args.temperature}°C is {result:.2f}°F")