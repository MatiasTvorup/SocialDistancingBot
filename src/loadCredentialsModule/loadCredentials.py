

def loadCredentialsFromFile(credentialFilePath):
  credentialLines = []
  try:
    credentialsFile = open(credentialFilePath)
    credentialLines = credentialsFile.readlines()
    credentialsFile.close()
  except:
    print("File not found")
    return None
  
  if(len(credentialLines) < 2):
    print("Not enough lines in credentials.txt")
    return None
  elif(len(credentialLines) > 2):
    print("Might be too many lines in credentials.txt, returning first 2 lines")
    return [credentialLines[0], credentialLines[1]]
  else:
    return removeNewlines(credentialLines)

def removeNewlines(lines):
  cleanedLines = []
  for line in lines:
    cleaned = line.replace("\n","")
    cleanedLines.append(cleaned)
  return cleanedLines



if __name__ == "__main__":
  loadCredentialsFromFile("../credentials.txt")