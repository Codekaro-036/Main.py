import os.path
import datetime
import subprocess
import pickle

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import face_recognition

import main1

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        self.login_button_main_window = main1.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=300)

        self.register_new_user_button_main_window = main1.get_button(self.main_window, 'register new user', 'gray',
                                                                    self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=400)

        self.webcam_label = main1.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)
         
        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.txt'

        def add_webcam(self, label):
         if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(2)

         self._label = label
         self.process_webcam() 

         def process_webcam(self): 
           ret, frame = self.cap.read()

           self.most_recent_capture_arr = frame
           img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
           self.most_recent_capture_pil = Image.fromarray(img_)
           imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
           self._label.imgtk = imgtk
           self._label.configure(image=imgtk)

           self._label.after(20, self.process_webcam)

    def login(self):
        unknown_img_path = './.tmp.jpg'

cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)        
output = str(subprocess.check_output(['face_recognition', self.db_dir, unknown_img_path]))        
name = output.split(',')[1][:-3]        
name = main1.recognize(self.most_recent_capture_arr, self.db_dir)        
if name in ['unknown_person', 'no_persons_found']:           
   util.msg_box('Ups...', 'Unknown user. Please register new user or try again.')@@ -67,8 +64,6 @@                f.write('{},{}\n'.format(name, datetime.datetime.now()))              
   f.close()        
   os.remove(unknown_img_path)   
   def register_new_user(self):       
     self.register_new_user_window = tk.Toplevel(self.main_window)        
     self.register_new_user_window.geometry("1200x520+370+120")@@ -106,7 +101,10 @@   
     def accept_register_new_user(self):       
         name = self.entry_text_register_new_user.get(1.0, "end-1c")      
         cv2.imwrite(os.path.join(self.db_dir, '{}.jpg'.format(name)),
                      self.register_new_user_capture)      
         embeddings = face_recognition.face_encodings(self.register_new_user_capture)[0]   
         file = open(os.path.join(self.db_dir, '{}.pickle'.format(name)), 'wb')     
         pickle.dump(embeddings, file)      
         util.msg_box('Success!', 'User was registered successfully !')


 


        



        


