import os
import time
import re
import sys
import requests
import json

dep_dic={
   "AE": "Aerospace Engineering",
   "AG": "Agricultural & Food Engineering",
   "AR": "Architecture & Regional Planning",
   "BT": "Biotechnology",
   "CH": "Chemical Engineering",
   "CY": "Chemistry",
   "CE": "Civil Engineering",
   "CS": "Computer Science & Engineering",
   "CR": "Cryogenic Engineering",
   "ED": "Center for Educational Technology",
   "EE": "Electrical Engineering",
   "EC": "Electronics & Electrical Communication Engineering",
   "GS": "G S Sanyal School of Telecommunications",
   "GG": "Geology & Geophysics",
   "HS": "Humanities & Social Sciences",
   "IE": "Instrumentation Engineering",
   "IM": "Industrial & Systems Engineering",
   "IT": "Information Technology",
   "MS": "Materials Science",
   "MA": "Mathematics",
   "ME": "Mechanical Engineering",
   "MD": "Medical Science & Technology",
   "MT": "Metallurgical & Materials Engineering",
   "MI": "Mining Engineering",
   "NA": "Ocean Engineering & Naval Architecture",
   "CL": "Oceans, Rivers, Atmosphere and Land Sciences",
   "PH": "Physics",
   "PK": "P K Sinha Centre for Bio Energy",
   "EP": "Rajendra Mishra School of Engineering Entrepreneurship",
   "IP": "Rajiv Gandhi School of Intellectual Property Law",
   "ID": "Ranbir and Chitra Gupta School of Infrastructure Design and Management",
   "RE": "Reliability Engineering Centre",
   "RT": "Rubber Technology Centre",
   "RD": "Rural Development Centre",
   "BS": "School of Bioscience",
   "ES": "School of Energy Science & Engineering",
   "EF": "School of Environmental Science and Technology",
   "NT": "School of Nano-Science and Technology",
   "WM": "School of Water Resources",
   "SM": "Vinod Gupta School of Management"
}

def get_syllabus(subject_code,subject_name):
    pdf_file_name = "{0}.pdf".format(subject_code)
    text_file_name= "{0}.txt".format(subject_code)

    if not os.path.isfile(text_file_name):
        url = 'https://erp.iitkgp.ernet.in/ERPWebServices/curricula/commonFileDownloader.jsp'
        data={}
        data['fileFullPath']='/DATA/ARCHIVE/SUBJECT/SYLLABUS/2009/{0}/{0}_1.pdf'.format(subject_code)
        data['pageno']='0'
        data['docId']=''
        #t=1
        while True:
            try:
                #time.sleep(t)
                response=requests.post(url,data)
                break
            except Exception, e:
                print(subject_code,t,e.message)
                exit()
                t=t*2
                continue
        if(response.status_code !=200 or response.apparent_encoding=='ascii'): #when file is not available, we get html response
            #print(response.status_code)
            #print(response.text)
            return
        with open(pdf_file_name,"wb") as handle:
            for data in response.iter_content():
                handle.write(data)
        os.system("pdftotext {0} {1}".format(pdf_file_name,text_file_name))

    with open(text_file_name, 'r') as content_file:
        content = content_file.read()
        try:
            m=re.search('LTP- (.*?),CRD- (.)(.*?)SYLLABUS :(.*?)(\s*)\Z',content,re.DOTALL)
            dic={}
            dic['LTP']=m.group(1)
            dic['Credits']=m.group(2)
            dic['Syllabus']=m.group(4)
            dic['Department']=dep_dic[subject_code[:2]]
            dic['Name']=subject_name
            dic['Code']=subject_code
        except Exception, e:
            print(subject_code,e.message)
            return
        #print(dic)
        return dic

if __name__ == '__main__':
    courses=[]
    with open("subjects.json",'r') as subject_file:
        subjects_dic=json.load(subject_file)
        for code in subjects_dic:
            print(code)
            res=get_syllabus(code,subjects_dic[code][0])
            if(res):
                print("success",code)
                courses.append(res)
            else:
                print("fail",code)

    with open("syllabus.json","w") as result_file:
        json.dump(courses,result_file)


    print(sys.argv)
    if(len(sys.argv)>1):
        print(get_syllabus(sys.argv[1]))
