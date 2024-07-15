class Patient:
    def __init__(self, name, surname, pesel, age, gender, arrival_time):
        self.name = name
        self.surname = surname
        self.pesel = pesel
        self.age = age
        self.gender = gender
        self.arrival_time = arrival_time
        self.next = None

class PatientQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_patients(self):
        curr = self.head
        while curr is not None:
            print(curr.name, curr.surname, curr.pesel)
            curr = curr.next

    def add_patient(self, patient):
        # Dodaj pacjenta na koniec listy oczekujących
        if self.tail is None:
            self.head = patient
            self.tail = patient
        else:
            self.tail.next = patient
            self.tail = patient

    def add_priority_patient(self, patient, position):
        # Jeśli lista jest pusta, dodaj pacjenta na początek
        if self.head is None:
            self.head = patient
            self.tail = patient
            return

        # Jeśli pacjent ma być dodany na początek listy, ustaw go jako głowę
        if position == 0:
            patient.next = self.head
            self.head = patient
            return

        # W przeciwnym razie, znajdź odpowiednią pozycję w liście i wstaw pacjenta
        curr = self.head
        for i in range(position - 1):
            curr = curr.next
            if curr is None:
                break
        patient.next = curr.next
        curr.next = patient

    def remove_patient(self, position):
        # Jeśli lista jest pusta, nie ma pacjenta do usunięcia
        if self.head is None:
            return

        # Jeśli pacjent ma być usunięty z początku listy, ustaw nową głowę
        if position == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        # W przeciwnym razie, znajdź pacjenta do usunięcia
        curr = self.head
        for i in range(position - 1):
            curr = curr.next
            if curr is None:
                return
        curr.next = curr.next.next
        if curr.next is None:
            self.tail = curr


def add_patient_from_keyboard():
    name = input("Podaj imię pacjenta: ")
    surname = input("Podaj nazwisko pacjenta: ")
    pesel = input("Podaj PESEL pacjenta: ")
    while not pesel.isdigit() or len(pesel) != 11:
        print("PESEL musi składać się z 11 cyfr!")
        pesel = input("Podaj PESEL pacjenta: ")
    age = input("Podaj wiek pacjenta: ")
    while not age.isdigit():
        print("Wiek musi być liczbą!")
        age = input("Podaj wiek pacjenta: ")
    age = int(age)
    gender = input("Podaj płeć pacjenta (M/F): ")
    while gender != "M" and gender != "F":
        print("Płeć musi być M lub F!")
        gender = input("Podaj płeć pacjenta (M/F): ")
    arrival_time = input("Podaj godzinę przyjęcia pacjenta: ")
    patient = Patient(name, surname, pesel, age, gender, arrival_time)
    return patient


queue = PatientQueue()

while True:
    print("1. Dodaj pacjenta na koniec kolejki")
    print("2. Dodaj pacjenta priorytetowego")
    print("3. Usunąć pacjenta z kolejki")
    print("4. Wypisać pacjentów w kolejce")
    print("5. Zakończyć działanie programu")
    choice = input("Wybierz opcję: ")

    if choice == "1":
        patient = add_patient_from_keyboard()
        queue.add_patient(patient)
    elif choice == "2":
        patient = add_patient_from_keyboard()
        position = input("Podaj pozycję pacjenta w kolejce: ")
        while not position.isdigit():
            print("Pozycja musi być liczbą!")
            position = input("Podaj pozycję pacjenta w kolejce: ")
        position = int(position)
        queue.add_priority_patient(patient, position)
    elif choice == "3":
        position = input("Podaj pozycję pacjenta do usunięcia: ")
        while not position.isdigit():
            print("Pozycja musi być liczbą!")
            position = input("Podaj pozycję pacjenta do usunięcia")
            position = int(position)
            queue.remove_patient(position)
    elif choice == "4":
        queue.print_patients()
    elif choice == "5":
        break
    else:
        print("Nieprawidłowy wybór!")


add_patient_from_keyboard()
