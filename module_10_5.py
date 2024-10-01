import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        line = file.readlines()
        all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]
start = datetime.datetime.now()
for file in filenames:
    read_info(file)
end = datetime.datetime.now()
print(f'{end - start} (линейный)')

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'{end - start} (многопроцессорный)')