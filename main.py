from HeaderFormat import HeaderFormat

if __name__ == "__main__":

    headerFormat = HeaderFormat()

    headerFormat.setHeader1(2, 2, 5)
    headerFormat.setResponse(4, 4)
    headerFormat.setMessageId(5)
    headerFormat.setToken(3)
    headerFormat.buildHeaderFormat()

    headerFormat.print()

