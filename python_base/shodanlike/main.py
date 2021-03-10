import geoip2.database
import sys
import socket
import socket
import threading
import socket
from multiprocessing import Pool
class SHODANLIKE():
    def __init__(self,info):
        self.info = info

    def main(self):
        something = self.info
        ip = domain = self.info
        something = something.replace('.','')
        if something.isdigit():
            return ['ip',self.info]
        else:
            try:
                ip = socket.gethostbyname("%s"%domain)
                return ['domen', ip]

            except:
                return "Мутный домен"


    def func(self,ip):
        def try_except(point):
            try:
                len(point)
            except:
                point = " "
            return point


        reader = geoip2.database.Reader('python_base/shodanlike/GeoIP2-City.mmdb')
        try:

            response = reader.city(ip)
            iso = response.country.iso_code
            countryname = response.country.name
            city = response.city.name
            specific = response.subdivisions.most_specific.name
            podsetka = response.traits.network
            latitude = response.location.latitude
            longitude = response.location.longitude


        except:
            iso = " "
            countryname = " "
            city = " "


        iso = try_except(iso)
        countryname = try_except(countryname)
        specific = try_except(specific)
        if iso == " " and countryname == " ":
            first = " "
        else:
            first = iso+"("+countryname+")"

        city = try_except(city)
        #podsetka = try_except(podsetka)

        reader.close()


        try:
            reader = geoip2.database.Reader('python_base/shodanlike/GeoIP2-ISP.mmdb')
            response = reader.isp(ip)
            organiz = response.autonomous_system_organization
            organiz_code = response.autonomous_system_number
            print(organiz_code)
        except:
            organiz = " "
            organiz_code = " "
        organiz = try_except(organiz)
        organiz_code = try_except(organiz_code)
        reader.close()

        try:
            reader = geoip2.database.Reader('python_base/shodanlike/GeoIP2-Connection-Type.mmdb')
            response = reader.connection_type(ip)
            connect = response.connection_type

        except:
            connect = " "
        connect = try_except(connect)
        #podsetka = try_except(podsetka)
        reader.close()

        try:
            reader = geoip2.database.Reader('python_base/shodanlike/GeoIP2-Domain.mmdb')
            response = reader.domain(ip)
            domain = response.domain
        except:
            domain = " "
        domain = try_except(domain)
        reader.close()
        #print(domain)

        return (domain,ip,podsetka,first,city,organiz,organiz_code,connect,specific,latitude,longitude)
