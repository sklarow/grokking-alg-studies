voted = {}

def check_voter(name):
    print(f"Voted: {voted}")
    if name in voted:
        print(f"{name} already voted!")
    else:
        print(f"{name} didn't voted!")
        voted[name] = True


check_voter("Allan")
check_voter("John")
check_voter("Allan")
check_voter("Sofia")
check_voter("Maria")
check_voter("John")
check_voter("Allan")
check_voter("Sofia")
check_voter("Maria")


