# Calculate the total time by adding the individual times
def calculate_total_time(swimming_time, cycling_time, running_time):
    total_time = swimming_time + cycling_time + running_time
    return total_time

def determine_award(total_time):
    qualifying_time = 100
# Set the award based on the total time
    if total_time <= qualifying_time:
        return "Provincial colours"
    elif total_time <= qualifying_time + 5:
        return "Provincial half colours"
    elif total_time <= qualifying_time + 10:
        return "Provincial scroll"
    else:
        return "No award"

def main():
    try:
         # Get input for each event times
        swimming_time = float(input("Enter swimming time (minutes): "))
        cycling_time = float(input("Enter cycling time (minutes): "))
        running_time = float(input("Enter running time (minutes): "))

        # Calculate the total time
        total_time = calculate_total_time(swimming_time, cycling_time, running_time)
        award = determine_award(total_time)
        # Display the results
        print(f"Total time: {total_time} minutes")
        print(f"Award: {award}")

    except ValueError:
        print("Invalid input. Please enter valid numerical values for time.")

if __name__ == "__main__":
    main()
