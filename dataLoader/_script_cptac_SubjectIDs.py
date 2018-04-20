import requests, csv

path = "/data/cptac/images/batch5-noscn-manifest.csv"
secondpath = "/data/cptac/images/CPTAC-batch6.csv"
url = "http://172.17.0.4:9099/services/CPTAC_DataLoader/SubjectIDs/submit/json"
apiKey = "4fbb38a3-1821-436c-a44d-8d3bc5efd33e"

with open(path, 'r') as f:
  with open(secondpath, "r") as g:
        reader = csv.DictReader(f)
        a = [row['study_id'] for row in reader]
        reader = csv.DictReader(g)
        b = [row['study_id'] for row in reader]
        study_id_list = list(set(a+b))
        #print(study_id_list)
        # now, let's do this
        headers = {'api_key': apiKey}
        results = [requests.post(url, json={'subject_id': x}, headers=headers) for x in study_id_list]



print([res.status_code for res in results])
