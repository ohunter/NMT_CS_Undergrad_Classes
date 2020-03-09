import os

if __name__ == "__main__":
    comp_flags = [("-l", "Project/test/expected_output/lexer"), ("-t", "Project/test/expected_output/parser"), ("-a", "Project/test/expected_output/ast")]
    comp_flags = [comp_flags[1]]
    for root, tmp, files in os.walk("Project/test/programs"):
        for file in files:
            for flag in comp_flags:
                print(file)
                test = os.popen(f"python Project/src/run.py {flag[0]} {root}/{file}").read()
                with open(f"{flag[1]}/{file.split('.')[0]}", "w") as fi:
                    fi.write(test[:-1])
                print("\n")