def main():

    print("I will tell you a story, but I need some information first.")
    character = input("What is the main character called?")
    job = input("What is their job?")
    print("Here is the story:")
    print("Once upon a time there was " + character + ", who was " + job)
    print("On the way to work, " + character + " reflected on life.")
    print("Perhaps " + character + " will not be " + job + " forever.")

if __name__ == '__main__':
    main()
