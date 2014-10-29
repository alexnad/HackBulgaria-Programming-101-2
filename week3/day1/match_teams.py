import requests
import itertools
import random


class Match():
    def __init__(self):
        self.info = self.__get_info()
        self.courses = self.__get_courses()

    def __get_info(self):
        r = requests.get('https://hackbulgaria.com/api/students', verify=False)
        return r.json()

    def __get_courses(self):
        courses = [person_info['courses'] for person_info in self.info]
        course_names = list({c['name'] for c in itertools.chain(*courses)})
        return course_names

    def print_courses(self):
        for index, course in enumerate(self.courses):
            print(index, course)

    def match_teams(self, course_id, team_size, group_time):
        course = {
            'name': self.courses[int(course_id)],
            'group': int(group_time)
            }

        names = [person['name'] for person in self.info if course in person['courses']]
        groups = self._create_random_groups(names, int(team_size))
        self._print_match(groups)

    def _create_random_groups(self, names, team_size):
        groups = []
        while names:
            group = []

            for i in range(int(team_size) + 1):
                try:
                    name = random.choice(names)
                    group.append(name)
                    names.remove(name)
                    group.append('\n')
                except IndexError:
                    break

            if group:
                groups.append(group)

        return groups

    def _print_match(self, groups):
            for group in groups:
                print('==========\n')
                print(''.join(group))

    def main(self):
        intro = 'Hello, you can use one the following commands:\n\
list_courses - this lists all the courses that are available\
now.\nmatch_teams <course_id>, <team_size>, <group_time>\n\
exit - leave the program\n'
        print(intro)

        running = True
        while running:
            command = input("Enter command>>")
            command = command.split()
            if command[0] == 'list_courses':
                self.print_courses()
            elif command[0] == 'match_teams' and len(command) == 4:
                self.match_teams(command[1], command[2], command[3])
            elif command[0] == 'exit':
                running = False
            else:
                print('Error! Invalid command!')


if __name__ == "__main__":
    Match().main()
