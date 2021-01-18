import filecmp
import os
class Checks():

    def path_length(self,path_input):
        if len(path_input.get()) == 0:
            return 0

    def path_exists(self,path_input):
        if  os.path.exists(path_input.get()):
            return True
        return False

    def path_empty(self,path_input):
        if os.stat(path_input.get()).st_size == 0:
            return True
        return False

    def operation_chosen(self,operation):
        if operation == "":
            return True
        return False

    def file_one_equal_file_two(self,file_one,file_two):
        return (filecmp.cmp(file_one, file_two, shallow=False))
