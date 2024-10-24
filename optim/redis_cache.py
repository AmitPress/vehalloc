from fastapi import FastAPI
from redis import Redis
from conf.settings import env
from datetime import date
client = Redis(host=env.REDIS_HOST, port=6379, db=0)

# cache the allocated employees and vehicles in redis for faster access
def is_employee_available(employee_id: str, date: date):
    if not client.sismember("allocated_employees",f"{str(date)}-{employee_id}"):
        return True
    else:
        return False
def allocate_employee(employee_id: str, date: date):
    client.sadd("allocated_employees",f"{str(date)}-{employee_id}")

def is_vehicle_available(vehicle_id: str, date: date):
    if not client.sismember("allocated_vehicles",f"{str(date)}-{vehicle_id}"):
        return True
    else:
        return False

def allocate_vehicle(vehicle_id: str, date: date):
    client.sadd("allocated_vehicles",f"{str(date)}-{vehicle_id}")


# cache the unallocated employees and vehicles in redis for faster access

# for employees
def cache_unallocated_employees(employee_ids: list):
    for employee_id in employee_ids:
        if is_employee_available(employee_id, date):
            client.sadd("unallocated_employees", f"{employee_id}")

def get_unallocated_employee(employee_id: str, date: date):
    available_employee = client.spop(f"unallocated_employees")
    if available_employee:
        allocate_employee(employee_id=employee_id, date=date)
    return available_employee

# this recursive function will get an employee from cache or db if cache is empty
def get_employee_from_cache_or_db(app: FastAPI, employee_id: str, date: date):
    employee_id = get_unallocated_employee(employee_id=employee_id, date=date)
    if employee_id:
        return employee_id
    employees = app.mongodb["employees"].aggregate([{"$sample": {"size": 100}}, {'$project': {'_id': 1 }}])
    employee_ids = [employee['_id'] for employee in employees]
    cache_unallocated_employees(employee_ids)
    get_employee_from_cache_or_db(app=app, employee_id=employee_id, date=date)

# for vehicles
def cache_unallocated_vehicles(vehicle_ids: list, date: date):
    for vehicle_id in vehicle_ids:
        if is_vehicle_available(vehicle_id, date):
            client.sadd("unallocated_vehicles", f"{str(date)}-{vehicle_id}")

def get_unallocated_vehicle(vehicle_id: str, date: date):
    available_vehicle = client.spop(f"unallocated_vehicles")
    if available_vehicle:
        allocate_vehicle(vehicle_id=vehicle_id, date=date)
    return available_vehicle

def get_vehicle_from_cache_or_db(app: FastAPI, vehicle_id: str, date: date):
    vehicle_id = get_unallocated_vehicle(vehicle_id=vehicle_id, date=date)
    if vehicle_id:
        return vehicle_id
    vehicles = app.mongodb["vehicles"].aggregate([{"$sample": {"size": 100}}, {'$project': {'_id': 1 }}])
    vehicle_ids = [vehicle['_id'] for vehicle in vehicles]
    cache_unallocated_vehicles(vehicle_ids, date)
    get_vehicle_from_cache_or_db(app=app, vehicle_id=vehicle_id, date=date)

# resetter
def reset_allocated_employees():
    if client.exists("allocated_employees"):
        client.delete("allocated_employees")

def reset_allocated_vehicles(): 
    if client.exists("allocated_vehicles"):
        client.delete("allocated_vehicles")
def reset_all_allocated():
    reset_allocated_employees()
    reset_allocated_vehicles()

def reset_unallocated_employees():
    if client.exists("unallocated_employees"):
        client.delete("unallocated_employees")

def reset_unallocated_vehicles():
    if client.exists("unallocated_vehicles"):
        client.delete("unallocated_vehicles")

def reset_all_unallocated():
    reset_unallocated_employees()
    reset_unallocated_vehicles()