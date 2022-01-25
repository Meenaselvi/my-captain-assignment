#clear method
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
car.clear()
print(car)
#item method
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x=car.items()
print(x)
#get method
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x=car.get("model")
print(x)
#form keys
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x=car.keys()
print(x)
#pop method
car={
    "brand":"ford",
    "model":"mustang"
    "year":1964
}
car.pop("model")
print(car)
#pop item method
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
car.popitem()
print(car)
#set default
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x=car.setdefault("model","bronco")
print(X)
#update method
car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
car.update({"color":"white"})
print(car)
#values method
car={
    "brand":"ford",
    "model":"mustard",
    "year":1964
}
x=car.values()
print(x)
