from data import getdata
from elastic import savedata
from schedule import check_time


def main():
    data = getdata()
    savedata(data)


if __name__ == "__main__":
    if check_time():
        main()
        print("done!")
