

if __name__ == "__main__":
    following_content = []
    follower_content = []
    with open("follower.txt","r") as f:
        follower_content = f.readlines()
    
    with open("following.txt","r") as f:
        following_content = f.readlines()

    diff = []
    for following in following_content:
        if following not in follower_content:
            diff.append(following)

    print(diff)
    with open("diff.txt","w") as df:
        for i in diff:
            df.write(i)
