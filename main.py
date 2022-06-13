from data import fetch_data
from elastic import savedata
from schedule import check_time


def main():
    data = fetch_data()
    savedata(data)


if __name__ == "__main__":
    if check_time():
        main()
        print("done!")
