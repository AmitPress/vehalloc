print('########### MONGO INIT DATABASE ###########');
db = db.getSiblingDB('vehalloc');
db.createCollection('allocations');
db.createCollection('drivers');
db.createCollection('employees');
db.createCollection('vehicles');