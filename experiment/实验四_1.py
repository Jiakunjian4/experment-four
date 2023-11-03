import time
class WaterHeater:
    def __init__(self):
        self.temperature = 20
        self.water_level = 0
        self.power_on = False
        self.broken = False

    def heat_water(self):
        if self.broken:
            print("Water heater is broken. Please repair.")
            return
        if self.water_level < 1:
            print("No water in the tank.")
            return
        self.power_on = True
        while self.temperature < 100 and self.power_on:
            self.temperature += 1
            print(f"Heating water... current temperature: {self.temperature}°C")
            time.sleep(0.5)  # Simulate time it takes to heat water
            # Turn off power if it's 11PM
            if int(time.strftime('%H', time.localtime(time.time()))) == 23:
                self.power_off()
        if self.temperature == 100:
            self.power_off()

    def power_off(self):
        self.power_on = False
        print("Power off.")

    def add_water(self):
        self.water_level += 1
        print("Water level is ", self.water_level)

    def drain_water(self):
        self.water_level -= 1
        print("Drained water level is ", self.water_level)

    def repair(self):
        if not self.broken:
            print("No need for repair.")
            return
        self.broken = False
        self.temperature = 20
        print("Water heater repaired and reset to 20°C.")










water_heater = WaterHeater()
water_heater.add_water()  # Add water to the heater
water_heater.heat_water()  # Start heating water