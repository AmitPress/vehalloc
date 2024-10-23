print('########### MONGO INIT DATABASE ###########');
db = db.getSiblingDB('backend');
db.createCollection('products');
db.createCollection('users');
db.createCollection('dailylogs');
db.createCollection('monthlylogs');