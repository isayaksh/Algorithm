import sys
import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--param1')
    args = parser.parse_args()

    my_variable = args.param1  # 명령줄 인수로 전달한 변수

    # 환경 변수로부터 변수 값을 읽을 수도 있습니다.
    # my_variable = os.environ.get('MY_VARIABLE')

    # 이제 my_variable을 사용하여 원하는 작업을 수행합니다.
    print("Received variable:", my_variable)

if __name__ == "__main__":
    main()
