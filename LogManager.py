from datetime import datetime

class LogManager:
    def console_log(self, amount_packages, time_elapsed):
        print(
            "Execution time for "
            + str(amount_packages)
            + " packages: "
            + str(time_elapsed)
            + " seconds"
        )

    def log_result(self, path, data):
        last_line = ""
        with open(path, "r") as f:
            last_line = f.readlines()[-1]
        f = open(path, "w")
        last_char = last_line[-1]
        last_line += str(data) if last_char == " " else ", " + str(data)
        f.write(last_line)
        f.close()

    def end_line(self, path):
        last_line = ""
        with open(path, "r") as f:
            last_line = f.readlines()[-1]
        f = open(path, "w")
        f.write(last_line + "\n")
        f.close()

    def new_execution(self, path):
        f = open(path, "a")
        prefix = str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")) + ": "
        f.write(prefix)
        f.close()
