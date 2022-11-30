# 读取 json 文件
# 

import json

class Dataset:

    def __init__(self,json_file_name) -> None:

        self.json_file_name = json_file_name
        with open(json_file_name) as f:
            self.file = json.load(f)
    
    def __str__(self) -> str:
        return str(self.file)
            
    def append(self,rec):
        rec['id']=len(self.file)
        self.file.append(rec)
        

    def find(self,index):
        
        return self.file[index]
    
    def find_name(self,name):
        name_set = []
        for n in self.file:
            if name == n['name']:
                name_set.append(n)
        return name_set    


    def insert(self,idx,rec):
        rec['id']=idx
        for n in self.file[idx:]:
            n['id'] += 1
            
        self.file = self.file[:idx]+[rec]+self.file[idx:]
        return self.file
    
    def save_json(self):
        with open(self.json_file_name, 'w') as f:
            json.dump(self.file, f)


    def deletebyName(self,idx):
        
        self.file = self.file[:idx] + self.file[idx+1:]
        for i in self.file[idx:]:
            i['id'] -= 1

        return self.file

    def updatebyName(self,idx,rec):
        self.file = self.deletebyName(idx)
        self.file = self.insert(idx,rec)
        return self.file
        



if __name__ == "__main__":
    member = Dataset('C:/Users/yhyxx/Desktop/github_project/project__train/records.json')
    
    # per = member.insert(3, {
    #             "id":3,
    #             "name":"aaa",
    #             "age":22,
    #             "favorite":"music"
    #         },)
    
    # member.save_json()
    update = member.updatebyName(3,{
        "id": 3,
        "name": "zaza",
        "age": 99,
        "favorite": "sleeping"
    },)
    print(update)

