# -*- coding: utf-8 -*-
import os.path
import argparse

#----------------------------------------Functions-----------------------------------  
#Dimensions comparison 
def check_image_dimensions(original_file_path,annotation_file_path):
   '''
   The Function compares two images (original and annotation) by height and width dimensions. 
   :param str (original_file_path): The file path of the original file path.
   :param str (annotation_file_path): The file path of the annotation file path.
   :return: True if the comparison was successful or false if failed.   
   '''
   #Checking if PIL is installed
   install_and_import('pillow')
   #importing the Python image Packge
   from PIL import Image
   #Creating image object for both original and annotation images
   img_original = Image.open(original_file_path)
   img_annotation = Image.open(annotation_file_path)
   
   #Extracting the the width and height dimensions into integers.
   width_original, height_original = img_original.size
   width_annotation, height_annotation = img_annotation.size
   
   # Checks if the dimensions are matching 
   if (width_original == width_annotation ) and (height_original == height_annotation ):
       return True
   else:
       return False 
   
#Error list print function  
def print_error_to_file(type_of_error,original_file_path,annotation_file_path,out_file):    
   '''
   The Function prints an the files that are problematics into an error list and it's error too. 
   :param int (type_of_error): The type of error to be documented in the list.
   :param str (original_file_path): The file path of the original file path.
   :param str (annotation_file_path): The file path of the annotation file path.  
   :param str (out_file): The error List file path.
   '''  
   #The Error type sequense
   if type_of_error   == 1:
       string = ('{0},{1},The original file is missing.'.format(original_file_path,annotation_file_path))
   elif type_of_error == 2:
       string = ('{0},{1},The annotation file is missing.'.format(original_file_path,annotation_file_path)) 
   elif type_of_error == 3:
       string = ('{0},{1},Both files are missing.'.format(original_file_path,annotation_file_path)) 
   else:
       string = ('{0},{1},The dimensions are not equal.'.format(original_file_path,annotation_file_path))  
   #Printing the error type into the error list    
   out_file.write('\n{}.'.format(string))

#Checking if the image packge is installed if not -> the function installs it using PIP.
def install_and_import(package):
    import importlib
    try:
        importlib.import_module('PIL')
    except ImportError:
        import pip
        pip.main(['install', package]) 
        
#The main sequence of the script
def main ():
    
    error_list_path = '{}/error_list.csv'.format(dataset_root_path)
    #debug counter = 0
    with open(error_list_path, 'w') as error_list_write, open(pair_file_path, 'r', encoding='utf-8') as pair_file_read:
        error_list_write.write('original photo path, annotation photo path,Error')
        #The loop runs on every line from the pairing file and checks it's validity
        for line in pair_file_read:
            line = line.split()
            #debug counter += 1
            err_count= 0
            original_img_path = dataset_root_path+line[0]
            anno_img_path = dataset_root_path+line[1]
           #debugging print(original_img_path)
            original_exists = os.path.isfile(original_img_path)
            anno_exists = os.path.isfile(anno_img_path)
            #Checks whether one of the image files is missing and categorize them with error codes
            if  not(original_exists) or not(anno_exists):
                if not(original_exists):
                    err_count = 1
                if not(anno_exists):
                    err_count += 2
                print_error_to_file(err_count,original_img_path,anno_img_path,error_list_write)
            #Checks if the dimensions of the files are equal
            if (err_count == 0) and not(check_image_dimensions(original_img_path,anno_img_path)) :
                    print_error_to_file(4,original_img_path,anno_img_path,error_list_write)
    #print (counter)              
    print('\n\nSUCCESS: The operation was successful! \nyou can find the error list in the following path: \n{0}'.format(error_list_path))               
            
#---------------------------------------------------------------------------------------          
    
#----------------------------------------SCRIPT START-----------------------------------        


#setting the arguments that needed to be enterd 
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--pair-file", help="The complete path of the pairs file ",type=str,required=True)
parser.add_argument("-d", "--dataset-root", help="The root folder of the DAVIS dataset",type=str,required=True)
args = parser.parse_args()
#debugging print('\n\n\nPair file {}\n\n dataset root {}\n\n\n\n'.format(args.pair_file,args.dataset_root))

#Solving the problems of compitability between linux and windows paths.
if os.name == 'nt':# nt = windows
    dataset_root_path = r"{}".format(str(args.dataset_root))
    dataset_root_path = dataset_root_path.replace("\\" , '/')
    pair_file_path = r"{}".format(str(args.pair_file))
    pair_file_path =pair_file_path.replace("\\" , '/')
else:
    dataset_root_path = args.dataset_root 
    pair_file_path = args.pair_file
 
#The flag indicates whether there were user input problems 
err_flag = True
#Checks whether the root directory exists
if not(os.path.isdir(dataset_root_path)):
    print("\nERROR: The provided DAVIS dataset root-folder path is not valid please try again.")
    err_flag = False
#Checks wether the pair file exists
if not(os.path.isfile(pair_file_path)):
    print("\nERROR: The provided pairs file path is not valid please try again.")
    err_flag = False

if err_flag: 
    main()           
  


