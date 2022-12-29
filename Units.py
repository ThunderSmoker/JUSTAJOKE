#include <iostream>
#include <string>

// Base class for year
class Year {
protected:
  int year;  // Year number
  float rate;  // Rate per unit

public:
  // Constructor
  Year(int year, float rate) : year(year), rate(rate) {}

  // Calculate charges function
  virtual float calculateCharges(int units) {
    return units * rate;
  }
};

// Month class derived from Year
class Month : public Year {
protected:
  std::string month;  // Month name

public:
  // Constructor
  Month(int year, float rate, std::string month) : Year(year, rate), month(month) {}
};

// Day class derived from Month
class Day : public Month {
protected:
  int day;  // Day of the month

public:
  // Constructor
  Day(int year, float rate, std::string month, int day) : Month(year, rate, month), day(day) {}

  // Override calculate charges function
  float calculateCharges(int units) {
    // Calculate charges for the current day
    float charges = units * rate;

    // Return the charges for the current day along with any surcharge
    return charges + calculateSurcharge(charges);
  }

  // Function to calculate surcharge
  virtual float calculateSurcharge(float charges) {
    return 0.0;  // No surcharge by default
  }
};

int main() {
  // Create a Day object for January 1st, 2020
  Day day(2020, 0.50, "January", 1);

  // Calculate charges for 100 units
  float charges = day.calculateCharges(100);

  std::cout << "Total charges: " << charges << std::endl;

  return 0;
}
