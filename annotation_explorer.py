# -*- coding: utf-8 -*-
"""
@author: Ilker Atik
"""
import os
import sys
class AnnotationExplorer:
    def __init__(self):
        self.res_files = []
        self.annotation_files = []
        self.id_class_dict = { # define your annotation ids and names here 
                    "0": ["Ignore",0],
                    "1": ["Pedesterian",0],
                    "2": ["People",0],
                    "3": ["Bicyle",0],
                    "4": ["Car",0],
                    "5": ["Van",0],
                    "6": ["Truck",0],
                    "7": ["Tricyle",0],
                    "8": ["Awn",0],
                    "9": ["Bus",0],
                    "10":["Motor",0],
                    "11":["Other",0]
                    }
    
    def getAnnotationFiles(self, folderPath):
        self.folderPath = folderPath
        for file in os.listdir(folderPath):
            if file.endswith(".txt"):
                if file == "classes.txt":
                    pass
                else:
                    self.annotation_files.append(file)
                
                
    def findAnnnotations(self, annotation_id, bound):
        """
        annotation_id: id in classes.txt, bound: minimum number of an annotation count that you want in a file.

        Returns
        -------
        returns files that has requested annotation more than 'bound' times.

        """
        ids_encountered = 0
        for file in self.annotation_files:
            
            text = open(os.path.join(self.folderPath, file), 'r')
            for line in text.read().split('\n'):
                class_id = line.split(" ")[0]
                if class_id == annotation_id:
                    ids_encountered += 1
                
            if ids_encountered > bound:
                self.res_files.append(file)
            ids_encountered = 0
        
        return self.res_files
    
    def numberOfEachAnnotation(self):
        for each in self.res_files:
            text = open(os.path.join(self.folderPath, each), 'r')
            for line in text.read().split('\n'):
                class_id = line.split(" ")[0]
                if class_id == '': #to ignore the last new line
                   pass
                else:
                   self.id_class_dict[class_id][1] = self.id_class_dict.get(class_id)[1]+1
                
    def addToDataset():
        pass
    def deleteFromDataset():
        pass
                
if __name__ == "__main__":
    inst = AnnotationExplorer()
    inst.getAnnotationFiles("C:\\Users\\atik_\\Downloads\\VisDrone2019-DET-train\\images_new")
    res_files = inst.findAnnnotations('10',50)
    inst.numberOfEachAnnotation()
    print(inst.id_class_dict.values())
        
        