"""Repository."""


class Car(object):
    """Class practice."""

    condition = "new"

    def __init__(self, model, color, mpg):
        """Class practice."""
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        """Class practice."""
        return "This is a %s %s with %s MPG." % \
            (self.color, self.model, str(self.mpg))


my_car = Car("DeLorean", "silver", 88)

print(my_car.display_car())
