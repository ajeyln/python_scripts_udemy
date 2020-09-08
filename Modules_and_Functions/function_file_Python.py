def personal_details(*args, sep=" ", end='\n', file=None, flush=False):
    per_det = []
    for arg in args:
        per_det.append(arg)
    
    print(per_det)
    return("First Name:{}, First Name:{}, Age:{}, Gender: {}".format(per_det[0], per_det[1], per_det[2], per_det[3]))

    
with open("Personal_information", "w") as person_info:
    personal_details("Radha", "Prabhu", 68, "Female", sep=":", file=person_info)
    personal_details("Vasudeva", "Nayak", 35, "Male", sep=":", file=person_info)
    personal_details("Ajey", "Nayak", 29, "Male", sep=":", file=person_info)
    personal_details("Ramanath", "Nayak", 27, "Male", sep=":", file=person_info)