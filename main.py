import os
import pydicom

def anonymization_and_compression():
    current_dir = r'D:\Slosh AI\SLOSH XRAYS\Ali Medical Data\2000 X-RAY\Sample'
    target_dir = r'D:\Slosh AI\SLOSH XRAYS\Ali Medical Data\2000 X-RAY\Data'
    counter = 1800
    row = 0
    column = 0

    for filename in os.listdir(current_dir):
        f = os.path.join(current_dir+'/', filename)
        if os.path.isfile(f):
            print(f)
            dataset = pydicom.dcmread(f)

            delattr(dataset, 'InstitutionName')
            #delattr(dataset, 'OperatorsName')
            delattr(dataset, 'PatientName')
            counter = counter + 1
            print(counter)
            row += 1
            dataset.save_as(target_dir+'/'+'A-'+str(counter)+".dcm")
anonymization_and_compression()
