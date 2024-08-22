class Filament:
    def __init__(self, color, material, total_rolls, unopened, full, useable, unuseable):
        self.color = color
        self.material = material
        self.total_rolls = total_rolls
        self.unopened = unopened
        self.full = full
        self.useable = useable
        self.unuseable = unuseable

    def get_inventory_report(self):
        report = f"{self.color},{self.material}:\n\tTotal Rolls:{self.total_rolls}\nOpened:{self.unopened}\nFull:{self.full}\nUseable:{self.useable}\nUnuseable:{self.unuseable}"
        return report
    

Filament_colors = ('Black','abs',1,2,1,4)

print(f"Filament report: ")