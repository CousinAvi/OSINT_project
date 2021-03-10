from googlesearch import search
class Google_Search():
    def __init__(self,number):
        self.number = number

    def VK_func(self):
        number = self.number
        query = "%s site:vk.com"%number
        massiv = []
        for j in search(query, num_results=10):
            massiv.append(j)
        if massiv != []:
            return massiv
        else:
            number = number.replace('+7','8')
            query = "%s site:vk.com"%number
            massiv = []
            for j in search(query, num_results=10):
                massiv.append(j)
            if massiv != []:
                return massiv
            else:
                return []
