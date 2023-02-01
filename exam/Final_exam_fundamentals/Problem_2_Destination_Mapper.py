def destination_map():
    import re
    data = input()
    pattern = r'\=[A-Z][A-Za-z]{2,}\=|\=[A-Z][A-Za-z]{2,}\s[A-Za-z]+\=|\/[A-Z][A-Za-z]{2,}\/|\/[A-Z][A-Za-z]{2,}\s[A-Za-z]+\/'
    matches = re.findall(pattern, data)
    
    cleli = []
    lenght = 0
    for strma in matches:
      cle = strma[1:-1]
      lenght += len(cle)
      cleli.append(cle)
      
    
    result = ', '.join(cleli)
    print(f"Destinations: {result}")
    print(f"Travel Points: {lenght}")


destination_map()