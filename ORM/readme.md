# ORM

## HACER UNA INSERION 
```
t = Type()
# #t = Type(name = "Test 1")
# t.name = "Test 1"
# t.save()
```

## HACER UNA MODIFICACION

```
t = Type.objects.get(id=3) # Recuperacion de Objeto
#print(t.name)
t.name = "Test 2"
t.save()
```

## HACER UNA ELIMINACION 

```
t = Type.objects.get(id=3) # Recuperacion de Objeto
t.delete()
```
