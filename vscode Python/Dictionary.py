dict={'Student': 'Utkarsh','UID': '21BCS11731','Branch': 'CSE','Student1': 'Manas','2nd UID': '21BCS1111','2nd Branch': 'ECE'}
dict1=dict.copy();
del dict['Student1'];
dict['3rd UID']='21BCS1112';
dict.update({'2nd UID': '22BCS1111'});
print(dict);
print(dict1);
