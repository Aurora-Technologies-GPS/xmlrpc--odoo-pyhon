import xmlrpc.client

# url =  'http://10.0.0.28:8069'
# db= 'odoo'
# username='admin'
# password='admin'

url = 'https://domain.do'
db =  'db_name'
username = 'miemail@domain.com'
password ='1234567'

comunication = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = comunication.authenticate(db, username, password, {})

models= xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
print(uid)

#partners= models.execute_kw(db, uid, password, 'res.partner', 'search', [[]])
partners= models.execute_kw(db, uid, password, 'res.partner', 'search', [[]], {'limit': 10})
print(partners)

record = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners])

print(record)

#partners_count= models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])


#print(partners_count)
#record = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners])

#print(record)

#f = open("data.json", "a+")
#f.write("{ \n")
#f.write(f"{record} \n")
#f.write("} \n")
#print("saved")
#f.close()