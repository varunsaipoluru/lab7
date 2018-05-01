class Time(object):

        hour = 0 
        minute = 0
        second = 0 

        def print_time(self):
                print('%.2d:%.2d:%.2d' %(self.hour, self.minute, self.second))

        def int_to_time(seconds):

                time = Time()
                minutes, second = divmod(seconds,60)
                time.hour, time.minute = divmod(minutes, 60)
                return time

        def time_to_int(self):
                minutes = self.hour * 60 + self.minute
                seconds = minutes * 60 + self.second
                return seconds

        def add_times(self, time):
                assert self.valid_time() and time.valid_time()
                seconds = self.time_to_int() + time.time_to_int()
                return time.int_to_time(seconds)

        def valid_time(self):
                if self.hour < 0 or self.minute < 0 or self.second < 0:
                        return False
                if self.minute >= 60 or self.second >= 60:
                        return False 
                return True
def main():
        noon_time = time()
        noon_time.hour = 12
        noon_time.minute = 0 
        noon_time.second = 0

        print("starts at") 
        noon_time.print_time()
        movie_minutes = 109
        run_time = time.int_to_time(movie_minutes * 60)
        print("run time")
        run_time.print_time()

        end_time = noon_time.add_times(run_time)
        print("ends at")
        end_time.print_time()

main()
