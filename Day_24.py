
# Ex1
thisdic = {'brand': 'Ford',
           'model': 'Mustang',
           'year': 1964}
mydict = thisdic.copy()
print(mydict)
dict2 = dict(thisdic)
print(dict2)
print("-------------------------")

# Ex2
myFamily = {
    'Child1': {
        'name': 'Fahd'
        , 'age': 18}
    , 'Child2': {
        'name': 'Ahmed'
        , 'age': 7}
    , 'Child3': {
        'name': 'Khalid'
        , 'age': 30}
        }
print(myFamily)
print("-------------------------")

# Ex3
Child1 = {
        'name': 'Fahd'
        , 'age': 18}
Child2 = {
        'name': 'Ahmed'
        , 'age': 7}
Child3 = {
        'name': 'Khalid'
        , 'age': 30}
myFamily = {
    'Child1': Child1
    , 'Child2': Child2
    , 'Child3': Child3
}
print(myFamily)
print("-------------------------")

# Ex4
thisdic2 = dict(brand='Ford', model='Mustang', year=1964)
print(thisdic2)
print("-------------------------")

