def http_error(status):
    match status:
        case 400:
            return "solicitu"
        case 300:
            return "jodete jajajja"
        case 6 :
            return "se murio :OOO"
        case _: #caso neutro 
            return "fuera de linea"
        
print(http_error(65))