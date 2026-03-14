import sys


def counseling(question: str, credential: str):
    print("Counseling question is: " + question)
    if credential is None:
        return "Please enter your counseling credential"
    return "my answer is : just keep calm"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    question = sys.argv[1]
    credential = sys.argv[2]
    counseling(question, credential)

