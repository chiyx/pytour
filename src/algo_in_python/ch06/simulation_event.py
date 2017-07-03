#! /usr/bin/env python3
# coding=utf-8

# simulation_event.py - 离散事件模拟

from random import randint
from prio_queue import PrioQueue
from collections import deque


class Simulation:

    def __init__(self, duration):
        self._eventq = PrioQueue()
        self._time = 0
        self._duration = duration

    def run(self):
        # 模拟到事件队列为空
        while not self._eventq.is_empty():
            event = self._eventq.dequeue()
            # 事件时间就是当前时间
            self._time = event.time()
            # 时间用完就结束
            if self._time > self._duration:
                break
            # 模拟这个事件，其运行可能产生新事件
            event.run()

    def add_event(self, event):
        self._eventq.enqueue(event)

    def cur_time(self):
        return self._time


class Event:

    def __init__(self, event_time, host):
        self._ctime = event_time
        self._host = host

    def __lt__(self, other_event):
        return self._ctime < other_event._ctime

    def host(self):
        return self._host

    def time(self):
        return self._ctime

    # 具体事件必须定义这个方法
    def run(self):
        pass


class Customs:

    def __init__(self, gate_num, duration,
                 arrive_interval, check_interval):
        self.simulation = Simulation(duration)
        # 用列表模拟队列
        self.waitline = deque()
        self.duration = duration
        self.gates = [0] * gate_num
        self.total_wait_time = 0
        self.total_used_time = 0
        self.car_num = 0
        self.arrive_interval = arrive_interval
        self.check_interval = check_interval

    def wait_time_acc(self, n):
        self.total_wait_time += n

    def total_time_acc(self, n):
        self.total_used_time += n

    def car_increment(self):
        self.car_num += 1

    def add_event(self, event):
        self.simulation.add_event(event)

    def enqueue(self, car):
        self.waitline.append(car)

    def has_queued_car(self):
        return len(self.waitline) > 0

    def next_car(self):
        return self.waitline.popleft()

    def find_gate(self):
        for i in range(len(self.gates)):
            if self.gates[i] == 0:
                self.gates[i] = 1
                return i
        return None

    def free_gate(self, i):
        if self.gates[i] == 1:
            self.gates[i] = 0
        else:
            raise ValueError("Clear gate[%s] error. " % (i))

    def simulate(self):
        Arrive(0, self)
        self.simulation.run()
        self.statistics()

    def statistics(self):
        print("Simulate " + str(self.duration) +
              " minutes, for " + str(len(self.gates)) + " gates")
        print(self.car_num, "cars pass the customs")
        print("Average waiting time:", self.total_wait_time / self.car_num)
        print("Average passing time:", self.total_used_time / self.car_num)
        i = len(self.waitline)
        print(i, "cars are in waiting line.")


class Car:

    def __init__(self, arrive_time):
        self.time = arrive_time

    def arrive_time(self):
        return self.time


class Arrive(Event):
    "汽车到达事件"

    def __init__(self, arrive_time, customs):
        super().__init__(arrive_time, customs)
        customs.add_event(self)

    def run(self):
        time, customs = self.time(), self.host()
        # 生成下一个事件
        Arrive(time + randint(*customs.arrive_interval), customs)
        # 下面是本到达车辆事件的行为
        car = Car(time)
        # 有车辆在等，进入等待队列
        if customs.has_queued_car():
            customs.enqueue(car)
            return
        # 检查空闲通道
        i = customs.find_gate()
        # 有通道，进入检查
        if i is not None:
            event_log(time, "car check")
            Leave(time + randint(*customs.check_interval), i, car, customs)
        else:
            customs.enqueue(car)


class Leave(Event):
    "汽车离开事件"

    def __init__(self, leave_time, gate_num, car, customs):
        super().__init__(leave_time, customs)
        self.car = car
        self.gate_num = gate_num
        customs.add_event(self)

    def run(self):
        time, customs = self.time(), self.host()
        event_log(time, "car leave")
        customs.free_gate(self.gate_num)
        customs.car_increment()
        customs.total_time_acc(time - self.car.arrive_time())
        if customs.has_queued_car():
            car = customs.next_car()
            i = customs.find_gate()
            event_log(time, "car check")
            customs.wait_time_acc(time - car.arrive_time())
            Leave(time + randint(*customs.check_interval),
                  self.gate_num, car, customs)


def event_log(time, name):
    print("Event: " + name + ", happens at " + str(time))


def main():
    car_arrive_interval = (1, 2)
    car_check_interval = (3, 5)
    cus = Customs(3, 480, car_arrive_interval, car_check_interval)
    cus.simulate()

if __name__ == '__main__':
    main()
