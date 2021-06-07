from csp import Constraint, CSP
from typing import Dict, List, Optional
import random as rand

class DapatRapatConstraint(Constraint[str,str]):
    def __init__(self, jadwalMahasiswa: List[str]):
        hari=[]
        for i in jadwalMahasiswa:
            hari.append(i.split(".")[0])
        super().__init__(hari)
        self.jadwalMahasiswa=jadwalMahasiswa
    def satisfied(self, assignment: Dict[str,str]):
        for key,val in assignment.items():
            if(f"{key}.{val}" in self.jadwalMahasiswa):
                return False
        return True

def generateJadwal(n: int):
    hari = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
    sesi = [1,2,3,4,5]
    res=[]
    for i in range(n):
        ses = f"{rand.choice(hari)}.Sesi{rand.choice(sesi)}"
        while ses in res:
            ses = f"{rand.choice(hari)}.Sesi{rand.choice(sesi)}"
        res.append(ses)
    return res

if __name__ == "__main__":
    rand.seed(123)
    jadwalTidakBisa = {
        "Ihza" : generateJadwal(10),
        "Azam" : generateJadwal(12),
        "Zahlul": generateJadwal(14),
        "Caca" : generateJadwal(15),
        "Sasa": generateJadwal(9),
        "Alfatah":generateJadwal(10)
    }
    print(jadwalTidakBisa)

    domains: Dict[str, List[str]]={}
    variabels = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
    for variabel in variabels:
        domains[variabel] = ["Sesi1","Sesi2","Sesi3","Sesi4","Sesi5",'-']

    csp: CSP[str,str] = CSP(variabels, domains)
    
    for key, value in jadwalTidakBisa.items():
        csp.add_constraint(DapatRapatConstraint(value))
    
    solution: Optional[Dict[str,str]] = csp.backtracking_search()
    
    if solution is None:
        print("Solusi ada")
    else:
        print(solution)


    

