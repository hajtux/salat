#!/usr/bin/env python

import re
import json
from urllib2 import urlopen

'''

------------------------ User Interface -------------------------


------------------------- Sample Usage --------------------------


'''

#----------------------- IpInfo Class ------------------------
class IpInfo():

	#------------------------ Constants --------------------------
	url = 'http://ipinfo.io/json'

        #------------------------ Atributs --------------------------
	org = ""
	city = ""
	country = ""
	region = ""
	longitude = 0.0     # Float
	latitude = 0.0      # Float
	ip = ""
	postal = ""

	def __init__(self):
		response = urlopen(self.url)
		data = json.load(response)
	        self.org = data['org']
        	self.city = data['city']
        	self.country = data['country']
        	self.region = data['region']
        	self.longitude = float(data['loc'].split(',')[0])
        	self.latitude = float(data['loc'].split(',')[1])
        	self.ip = data['ip']
        	self.postal = data['postal']


	def getOrg(self):
		return self.org

	def getCity(self):
		return self.city

	def getCountry(self):
		return self.country
	
        def getRegion(self):
		return self.region

        def getLongitude(self):
                return self.longitude

        def getLatitude(self):
                return self.latitude

        def getIp(self):
                return self.ip

        def getHostname(self):
                return self.hostname

        def getPostal(self):
                return self.postal


#---------------------- ipInfo Object -----------------------
ipInfo = IpInfo()


#-------------------------- Test Code --------------------------
# sample code to run in standalone mode only
if __name__ == "__main__":
	print('Infos from my IP : \n'+ ('='* 41))
	print 'Org \t : %s'% ipInfo.getOrg()
        print 'City \t : %s'% ipInfo.getCity()
        print 'Country : %s'% ipInfo.getCountry()
        print 'Region \t : %s'% ipInfo.getRegion()
        print 'Longitude : %f'% ipInfo.getLongitude()
        print 'Latitude : %f'% ipInfo.getLatitude()
        print 'Ip \t : %s'% ipInfo.getIp()
        print 'Postal \t : %s'% ipInfo.getPostal()






 
