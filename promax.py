def moyenne(nombres):
    return sum(nombres) / len(nombres)

def maximum(nombres):
    return max(nombres)




if __name__ == "__main__":
    donnees = [4, 8, 15, 16, 23, 42]
    print("Moyenne:", moyenne(donnees))
    print("Max:", maximum(donnees))

