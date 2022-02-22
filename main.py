
def print_start():
    print("##########################")
    print("######  UtilityBot  ######")
    print("##########################\n")
    print("Choose an option:")
    print_options(0)

def print_options(type):
    if type == 0:
        with open("options/main_options.txt") as opt:
            options = opt.read().splitlines()
        for i in range(len(options)):
            print(str(i+1) + ". " + options[i])
        print("-1. Abort")
        opt.close()

print_start()