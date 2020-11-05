#!/usr/bin/env python3
import random
import time
import psutil
import os


def calculations(calculations_ammount):
    for i in range(int(calculations_ammount)):
        base_number = 5
        random_number = random.random()
        result = i * base_number * random_number / 3.21


class cpu_increase:
    """
    Class used to increase usage of CPU to given level.
    """

    def __init__(self, repeats=1000000, cpu_max_usage=25):
        print('You just started a program that will increase your CPU usage!')
        self.repeats = repeats
        self.cpu_max_usage = cpu_max_usage
        self.cycles = 0
        self.cpu_usage = psutil.cpu_percent()

    def get_step(self):
        local_step = self.repeats / 10
        # We need few cycles for the results of cpu_percent() to stabilize.
        # After that we want to adjust our step by calculating the
        # difference between target and current CPU usage.
        if self.cycles > 10:
            local_step = (self.cpu_max_usage - self.cpu_usage) * local_step

        self.step = int(local_step)

    def one_step(self):
        calculations(self.repeats)
        self.cpu_usage = psutil.cpu_percent()
        time.sleep(0.1)
        self.cycles += 1

    def print_results(self):
        print(f'Calculation done in cycle {self.cycles}: {self.repeats}')
        print(f'CPU usage is: {self.cpu_usage}%. Calculations number was increased by {self.step}.')
        print('--------------------------------\n')

    def start_increase(self):
        while True:
            self.get_step()
            self.one_step()
            self.print_results()


test = cpu_increase()
test.start_increase()