from loadCredentialsModule import loadCredentials

def main():
  yeet = loadCredentials.loadCredentialsFromFile("credentials.txt")
  print(yeet)


if __name__ == "__main__":
  main()
