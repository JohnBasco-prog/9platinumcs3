class Patient:
  def __init__(self,name,bill_amount):
    self.name = name
    self.bill_amount = 15000
   
  def set_name(self, name):
    self.name = name

  def get_name(self):
    return f" {self.name}"
    
  def set_bill_amount(self,bill_amount):
    self.bill_amount = bill_amount
  
  def get_bill_amount(self):
    return self.bill_amount

  def calculate_bill(self):
    return self.get_bill_amount()

  def display_patient_type(self):
   return "Regular patient"

class Senior_patient(Patient):
   def calculate_bill(self):
    return self.get_bill_amount() * 0.80

   def display_patient_type(self):
    return "Senior patient"

class Philhealth_patient(Patient):
   def calculate_bill(self):
    return self.get_bill_amount() * 0.85

   def display_patient_type(self):
    return "Philhealth patient"

patient = Patient("Juan Dela Cruz",15000)
senior = Senior_patient("Maria Santos",15000)
philhealth = Philhealth_patient("Pedro Reyes",15000)
print("Hospital Billing System")
print("-----------------------")
print(f"Patient Name: {patient.get_name()}")
print(f"Patient Type: {patient.display_patient_type()}")
print("Original Bill: 15000")
print(f"Final Bill: {patient.calculate_bill()}")
print("")
print(f"Patient Name: {senior.get_name()}")
print(f"Patient Type: {senior.display_patient_type()}")
print("Original Bill: 15000")
print(f"Final Bill: {senior.calculate_bill()}")
print("")
print(f"Patient Name: {philhealth.get_name()}")
print(f"Patient Type: {philhealth.display_patient_type()}")
print("Original Bill: 15000")
print(f"Final Bill: {philhealth.calculate_bill()}")
