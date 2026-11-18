"Задание 1. Класс Appointment (запись клиента)"

class Master:
    def __init__(self, master_id: int, name: str):
        self.master_id = master_id
        self.name = name


class Service:
    def __init__(self, service_id: int, name: str):
        self.service_id = service_id
        self.name = name


masters = [Master(1, "Мастер 1"), Master(2, "Мастер 2")]
services = [Service(1, "Стрижка"), Service(2, "Окрашивание")]


def get_master(master_id: int):
    for master in masters:
        if master.master_id == master_id:
            return master
    return None


def get_service(service_id: int):
    for service in services:
        if service.service_id == service_id:
            return service
    return None


class Appointment:

    def __init__(self, id: int, client_name: str, master_id: int, service_id: int, time: str):
        self.id = id
        self.client_name = client_name
        self.master_id = master_id
        self.service_id = service_id
        self.time = time

    def __repr__(self):
        return (f"Appointment(id={self.id}, client_name='{self.client_name}', "
                f"master_id={self.master_id}, service_id={self.service_id}, "
                f"time='{self.time}')")


appointments = []


def create_appointment(client_name: str,
                       master_id: int,
                       service_id: int,
                       time: str) -> Appointment | None:

    if not client_name or not time:
        return None

    master = get_master(master_id)
    service = get_service(service_id)

    if master is None or service is None:
        return None

    appointment = Appointment(
        id=len(appointments) + 1,
        client_name=client_name,
        master_id=master.master_id,
        service_id=service.service_id,
        time=time,
    )
    appointments.append(appointment)
    return appointment

if __name__ == "__main__":
    # Тест 1: создаём 2 валидные записи
    first_appointment = create_appointment("Иванова А.А.", 1, 1, '10:00')
    second_appointment = create_appointment("Петрова А.А.", 1, 1, '11:00')

    print("Список записей:")
    for appointment in appointments:
        print(appointment.client_name, appointment.time)

    # Тест 2: частично не заполнены поля
    no_correct_appointment = create_appointment("", 1, 1, '12:00')
    print(len(appointments))