class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        cost_start = car.comfort_class
        cost_progress1 = cost_start * (self.clean_power - car.clean_mark)
        cost_progress2 = cost_progress1 * self.average_rating
        cost_final = cost_progress2 / self.distance_from_city_center
        return round(cost_final, 1)

    def serve_cars(self, cars_list: list) -> float:
        price = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                price += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, single_rate: float) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings
                                     + single_rate)
                                    / (self.count_of_ratings
                                       + 1), 1)
        self.count_of_ratings += 1
