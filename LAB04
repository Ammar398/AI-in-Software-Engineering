//Lab Task 1: Convert the program to a Three-Room Environment

# three_room_environment.py

from room import Room
from environment import Environment
from vacuum_agent import VacuumAgent

class ThreeRoomVacuumCleanerEnvironment(Environment):
    def __init__(self, agent):
        self.rooms = {
            'A': Room('A', 'dirty'),
            'B': Room('B', 'dirty'),
            'C': Room('C', 'dirty')
        }
        self.agent = agent
        self.currentRoom = self.rooms['A']
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res

            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                if self.currentRoom.location == 'A':
                    self.currentRoom = self.rooms['B']
                elif self.currentRoom.location == 'B':
                    self.currentRoom = self.rooms['C']
            elif res == 'left':
                if self.currentRoom.location == 'C':
                    self.currentRoom = self.rooms['B']
                elif self.currentRoom.location == 'B':
                    self.currentRoom = self.rooms['A']

            self.displayAction()
            self.step += 1

    def displayPerception(self):
        print(f"Perception at step {self.step}: [{self.currentRoom.status}, {self.currentRoom.location}]")

    def displayAction(self):
        print(f"------- Action taken at step {self.step}: [{self.action}]")

Lab Task 2: Convert to an n-Room Environment

class NRoomVacuumCleanerEnvironment(Environment):
    def __init__(self, agent, n):
        self.rooms = [Room(chr(65 + i), 'dirty') for i in range(n)]  # A, B, C, ...
        self.agent = agent
        self.currentRoomIndex = 0
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res

            if res == 'clean':
                self.rooms[self.currentRoomIndex].status = 'clean'
            elif res == 'right' and self.currentRoomIndex < len(self.rooms) - 1:
                self.currentRoomIndex += 1
            elif res == 'left' and self.currentRoomIndex > 0:
                self.currentRoomIndex -= 1

            self.displayAction()
            self.step += 1

    def displayPerception(self):
        room = self.rooms[self.currentRoomIndex]
        print(f"Perception at step {self.step}: [{room.status}, {room.location}]")

    def displayAction(self):
        print(f"------- Action taken at step {self.step}: [{self.action}]")

Lab Task 3: Does the agent ever stop? Can you make it stop?

def executeStep(self, n=1):
    for _ in range(n):
        if all(room.status == 'clean' for room in self.rooms):
            print("All rooms are clean. Stopping.")
            break


Lab Task 4: Add scoring system

class NRoomVacuumCleanerEnvironment(Environment):
    def __init__(self, agent, n):
        ...
        self.score = 0

    def executeStep(self, n=1):
        for _ in range(n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res

            if res == 'clean':
                self.score += 25
                self.rooms[self.currentRoomIndex].status = 'clean'
            elif res == 'right' or res == 'left':
                self.score -= 1

            for room in self.rooms:
                if room.status == 'dirty':
                    self.score -= 10

            self.displayAction()
            print(f"Score after step {self.step}: {self.score}")
            self.step += 1

Lab Task 5: Reflex Agent with a Model, and Without Sensors
class ModelReflexVacuumAgent(Agent):
    def __init__(self, n):
        self.model = ['dirty'] * n
        self.current_index = 0

    def sense(self, env):
        self.current_index = env.currentRoomIndex
        self.model[self.current_index] = env.rooms[self.current_index].status

    def act(self):
        if self.model[self.current_index] == 'dirty':
            return 'clean'
        elif self.current_index < len(self.model) - 1:
            return 'right'
        elif self.current_index > 0:
            return 'left'
        return 'no_op'


