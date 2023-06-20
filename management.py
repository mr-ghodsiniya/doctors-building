class DoctorManagement:
    
    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.id = id
        self.is_logged_in = False
        self.last_password_changed_by = None
        
    def login(self, email, id):
        if self.email == email and self.id == id:
            self.is_logged_in = True
            return f"Hi {self.name} your welcome."
        else:
            return f"Hi {self.name} sth is wrong."

    def change_password(self, old_pass, new_pass):
        if self.is_logged_in:
            if old_pass == self.id:
                self.id == new_pass
                self.last_password_changed_by = self.name
                return "Password changed."
            else:
                return "Incorrect old password."
        else:
            return "You are not logged in."
        
    def get_last_password_changed_by(self):
        return self.last_password_changed_by
    

class DoctorPrescriptionManagement(DoctorManagement):
    
    def __init__(self, name, email, id):
        super().__init__(name, email, id)
        self.prescriptions = {}
        
    def add_prescription(self, patient_name, medication):
        if self.is_logged_in:
            if patient_name not in self.prescriptions:
                self.prescriptions[patient_name] = []
            self.prescriptions[patient_name].append(medication)
            return f"Prescription added for {patient_name}: {medication}"
        else:
            return "You are not logged in."
        
    def edit_prescription(self, patient_name, old_medication, new_medication):
        if self.is_logged_in:
            if patient_name in self.prescriptions:
                if old_medication in self.prescriptions[patient_name]:
                    index = self.prescriptions[patient_name].index(old_medication)
                    self.prescriptions[patient_name][index] = new_medication
                    return f"Prescription edited for {patient_name}."
                else:
                    return f"No matching prescription found for {patient_name}."
            else:
                return f"No prescriptions found for {patient_name}."
        else:
            return "You are not logged in."
        

class PatientManagement:
    
    def __init__(self):
        self.patients = []
        self.appointments = {}
        
    def register_patient(self, name, age, gender, phone):
        patient = {
            "name": name,
            "age": age,
            "gender": gender,
            "phone": phone
        }
        self.patients.append(patient)
        return f"Patient {name} registered successfully."
        
    def view_patient_info(self, patient_name):
        for patient in self.patients:
            if patient["name"] == patient_name:
                info = f"Patient Information => Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Phone: {patient['phone']}"
                return info
        return "Patient not found."
        
    def schedule_appointment(self, patient_name, doctor_name, date, time):
        for patient in self.patients:
            if patient["name"] == patient_name:
                if doctor_name not in self.appointments:
                    self.appointments[doctor_name] = []
                appointment = {
                    "patient_name": patient_name,
                    "date": date,
                    "time": time,
                    "appointments_fee": 8*5*3,
                }
                self.appointments[doctor_name].append(appointment)
                return f"Appointment scheduled successfully with {doctor_name} for {patient_name}."
            else:
                return "Make info in account and try again"
    
    def get_appointment_fee(self, patient_name, date, time):
        for appointments in self.appointments.values():
            for appointment in appointments:
                if appointment["patient_name"] == patient_name and appointment["date"] == date and appointment["time"] == time:
                    return appointment["appointments_fee"]
                return "Appointment not found."
    
    def view_appointments(self):
        appointments_info = "Appointments => "
        for doctor, appointments in self.appointments.items():
            appointments_info += f"Doctor: {doctor} => "
            for appointment in appointments:
                appointments_info += f"Patient => {appointment['patient_name']}, Date: {appointment['date']}, Time: {appointment['time']}"
        return appointments_info