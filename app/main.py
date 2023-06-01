from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    cleaning_stuff = Cleaner(cleaner)
    for customer in customers:
        customers_list.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers_list, cleaning_stuff)
    pass
