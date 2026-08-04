import pandas as pd 

df = pd.read_csv("dataset.csv")

# primer vistazo
print("HEAD")
print(df.head())

print("--------------------------------------")

print("TAIL")
print(df.tail())

print("--------------------------------------")

print("SHAPE")
print(df.shape)

print("--------------------------------------")

print("COLUMNS")
print(df.columns)

print("--------------------------------------")

print("INFO")
print(df.info())

print("--------------------------------------")

# tipos de datos
# memoria utilizada
# columnas
# valores no nulos

 #   Column          Non-Null Count   Dtype  
""" ---  ------          --------------   -----  
 0   PatientId       110527 non-null  float64
 1   AppointmentID   110527 non-null  int64  
 2   Gender          110527 non-null  str    
 3   ScheduledDay    110527 non-null  str    
 4   AppointmentDay  110527 non-null  str    
 5   Age             110527 non-null  int64  
 6   Neighbourhood   110527 non-null  str    
 7   Scholarship     110527 non-null  int64  
 8   Hipertension    110527 non-null  int64  
 9   Diabetes        110527 non-null  int64  
 10  Alcoholism      110527 non-null  int64  
 11  Handcap         110527 non-null  int64  
 12  SMS_received    110527 non-null  int64  
 13  No-show         110527 non-null  str   """

 # no tiene valores nulos
print("DESCRIBE")
print(df.describe())

""" 
          PatientId  AppointmentID            Age    Scholarship   Hipertension       Diabetes     Alcoholism        Handcap   SMS_received
count  1.105270e+05   1.105270e+05  110527.000000  110527.000000  110527.000000  110527.000000  110527.000000  110527.000000  110527.000000
mean   1.474963e+14   5.675305e+06      37.088874       0.098266       0.197246       0.071865       0.030400       0.022248       0.321026
std    2.560949e+14   7.129575e+04      23.110205       0.297675       0.397921       0.258265       0.171686       0.161543       0.466873
min    3.921784e+04   5.030230e+06      -1.000000       0.000000       0.000000       0.000000       0.000000       0.000000       0.000000
25%    4.172614e+12   5.640286e+06      18.000000       0.000000       0.000000       0.000000       0.000000       0.000000       0.000000
50%    3.173184e+13   5.680573e+06      37.000000       0.000000       0.000000       0.000000       0.000000       0.000000       0.000000
75%    9.439172e+13   5.725524e+06      55.000000       0.000000       0.000000       0.000000       0.000000       0.000000       1.000000
max    9.999816e+14   5.790484e+06     115.000000       1.000000       1.000000       1.000000       1.000000       4.000000       1.000000
 """