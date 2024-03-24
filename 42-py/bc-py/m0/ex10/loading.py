from typing import Generator
import time

def ft_progress(lst :range) -> Generator[int, None, None]:

    # start time
    time_start :float = time.time()

    # initialization
    length :int = len(lst)
    bar_width :int = 26
    pacman :str = "C"
    switch :int = 1

    for elem in lst:

        # progress
        step :int = elem + 1
        percent :int = round((step / length) * 100)

        # time
        time_elapsed :float = round(time.time() - time_start, 2)
        time_remain :float = round((time_elapsed / step) * (length - step), 2)

        # pacman go waka waka
        if not switch == percent:
            switch = percent
            pacman = pacman.swapcase()

        # progress bar generator
        progress :int = round(percent / (100 / bar_width))
        progress_bar :str = f"{'≡' * (progress - 1)}{pacman}{'⊙' * (bar_width - progress)}"

        print(f"ETA: {time_remain:.2f}s [{percent:3}%] [{progress_bar}] {step}/{length} | elapsed time: {time_elapsed:.2f}s ", end="\r")
        yield elem

listy :range = range(1000)
ret :int = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.03)
print()
print(ret)