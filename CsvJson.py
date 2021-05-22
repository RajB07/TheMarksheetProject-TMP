
import csv  #need to pip install
import json  #need to pip install
import re   #need to pip install


def dictMake(a):
    a = a.split('|')
    roll = a[0].lstrip().rstrip()
    
    c1_1 = re.findall('\d+',a[1])[0:2]
    c2_1 = re.findall('\d+',a[2])[0:2]
    c3_1 = re.findall('\d+',a[3])[0:2]
    c4_1 = re.findall('\d+',a[4])[0:2]
    
    name = a[1].lstrip().split()[0:3]
    pas = a[5].lstrip()[0]
    
    c1_2 = re.findall('\d+',a[5])[0]
    c2_2 = re.findall('\d+',a[6])[0]
    c3_2 = re.findall('\d+',a[7])[0]
    c4_2 = re.findall('\d+',a[8])[0:2]
    
    college = re.findall('(\s+[A-Z]+)+\s+',a[5])[0].lstrip().rstrip()
    
    c5_1 = re.findall('\d+',a[9])[1:3]
    c6_1 = re.findall('\d+',a[10])[0:2]
    
    c5_2 = re.findall('\d+',a[11])[0:2]
    c7_2 = re.findall('\d+',a[13])[0]
    
    cgp,total_credit = a[14].split()[2] , a[14].split()[1]
    
    d = {'roll':roll,
         'first_name':name[0],
         'midlle_name':name[1],
         'last_name':name[2],
         'college':college,'pass_status':pas,
         'total_gp':total_credit,'CGPA':cgp,
         'c1_theory':c1_1[0],'c1_test':c1_1[1],'c1_oral':c1_2,
         'c2_theory':c2_1[0],'c2_test':c2_1[1],'c2_oral':c2_2,
         'c3_theory':c3_1[0],'c3_test':c3_1[1],'c3_oral':c3_2,
         'c4_theory':c4_1[0],'c4_test':c4_1[1],'c4_oral1':c4_2[0],'c4_oral2':c4_2[1],
         'c5_theory':c5_1[0],'c5_test':c5_1[1],'c5_oral1':c5_2[0],'c5_oral2':c5_2[1],
         'c6_theory':c6_1[0],'c6_test':c6_1[1],
         'c7_term':c7_2
         }
    return d

def dictList(txt_path):
    d = []
    with open(txt_path,'r') as fh:
        data = fh.readlines()
        for line in data:
            try:
                d.append(dictMake(line))
            except:
                continue
    return d
        


def makeCsv(csv_path,d):
    
    try:
        with open(csv_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=list(d[0].keys()))
            writer.writeheader()
    
            writer.writerows(d)
    except IOError:
        print("I/O error")



def makeJson(json_path ,d):
    with open(json_path, "w") as outfile:  
        json.dump(d, outfile)


      
