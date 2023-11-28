#Abstract: read yaml file through 3 ways.
#Time: 2023-11-28
#Authour: Aoxiang Zhang

def read_yaml_IO(file_path):
    file = open(file_path)
    a = file.read()
    print(a)
    file.close()


def read_yaml_tryCatch(file_path):
    file = open(file_path)
    try:
        a = file.read()
        print(a)
    except Exception as e:
        print(e)
    finally:
        file.close()


def read_yaml_withOpen(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        a = file.read()
        print(a)


        #read file throug row
        """
        for i in file.readlines():
            print("======")
            print(i)"""


if __name__ == "__main__":
    file_path = "../config/environment.yaml"
    print("read yaml file just IO:")
    read_yaml_IO(file_path)
    print("read yaml file try catch: ")
    read_yaml_tryCatch(file_path)
    print("read yaml file with open: ")
    read_yaml_withOpen(file_path)
