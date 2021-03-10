import requests



class VK_bond(object):
    def __init__(self,source,destination):
        self.source = source
        self.destination = destination

    def get_friends(self,id_number):
            token = 'YOUR_TOKEN'
            response = requests.get('https://api.vk.com/method/friends.get?v=5.89&access_token=%s&user_id=%s'%(token,id_number)).json()
            return response

    def test_id(self,id_number):
        try:
            token = 'YOUR_TOKEN'
            response = requests.get('https://api.vk.com/method/users.get?v=5.89&access_token=%s&user_ids=%s'%(token,id_number)).json()
            return response
        except:
            return []

    def main(self):
        friend_list_source = self.test_id(self.source)
        friend_list_destination = self.test_id(self.destination)

        source_id = friend_list_source['response'][0]['id']
        source_is_closed = friend_list_source['response'][0]['is_closed']

        dist_id = friend_list_destination['response'][0]['id']
        dist_is_closed = friend_list_destination['response'][0]['is_closed']

        if source_is_closed == False and dist_is_closed == False:
            svyazi = self.algorithm_po_dvum(source_id,dist_id)
            return svyazi


        elif (source_is_closed == False and dist_is_closed == True):
            svyazi = self.algorithm_po_odnomu(source_id,dist_id,0)
            return svyazi



        elif (source_is_closed == True and dist_is_closed == False):
            svyazi = self.algorithm_po_odnomu(dist_id,source_id,1)
            return svyazi

        else:
            return ['Block']

    def algorithm_po_odnomu(self,istochnik,dist_id,invers):
        baza = self.get_friends(istochnik)['response']['items']  #список id друзей источника
        if baza.count(int(dist_id)) != 0:
            mould = [istochnik,dist_id]
            if invers != 0:
                mould.reverse()
            return mould
        else:
            for friend in baza:
                try:
                    first_round_list = self.get_friends(friend)['response']['items']
                    if first_round_list.count(dist_id) != 0:
                        mould = [istochnik,friend,dist_id]
                        if invers != 0:
                            mould.reverse()
                        return mould
                except:
                    continue


    def algorithm_po_dvum(self,source_id,dist_id):
        baza = self.get_friends(source_id)['response']['items']  #список id друзей источника
        baza_destinataion = self.get_friends(dist_id)['response']['items'] #список id друзей цели

        if baza.count(int(dist_id)) != 0:
            return [source_id,dist_id]

        elif list(set(baza_destinataion) & set(baza)) != [] or list(set(baza) & set(baza_destinataion)) != []:
            return [source_id,list(set(baza_destinataion) & set(baza))[0],dist_id]

        else:
            for friend in baza:  #ищем по каждому другу источника
                try:
                    temp = self.get_friends(friend)['response']['items'] #список друзей друга на 2 уровне
                    if list(set(baza_destinataion) & set(temp)) != [] or list(set(temp) & set(baza_destinataion)) != []:
                        return [source_id,friend,list(set(baza_destinataion) & set(temp))[0],dist_id]
                except:
                    continue
            return []
