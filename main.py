from fastapi import FastAPI
import json

with open("menu.json","r") as read_file:
	data=json.load(read_file)
app=FastAPI()

@app.get('/menu/{item_id}')
async def read_menu(item_id:int):
	for menu_item in data['menu']:
		if menu_item['id']==item_id:
			return menu_item
	raise HTTPException(
		status_code=404,detail=f'Item not found'
	)

@app.put('/menu/{item_id}')
async def update_menu(item_id:int,item_name:str):
    listmenu=[]
    for menu_item in data['menu']:
        if menu_item['id']==item_id:
            menu_item['name']=item_name
        listmenu.append(menu_item)
    data['menu']=listmenu
    with open('menu.json', 'w') as tambahdata:
        json.dump(data, tambahdata)
    return data

@app.delete('/menu')
async def delete_menu(item_id:int, item_name:str):
    delmenu=[]
    for menu_item in data['menu']:
        if (menu_item['id']==item_id and menu_item['name']==item_name):
            continue
        else:
            delmenu.append(menu_item)
    data['menu']=delmenu
    with open('menu.json', 'w') as tambahdata:
        json.dump(data, tambahdata)
    return data       

@app.post('/menu')
async def add_menu(item_id:int,item_name:str):
    data['menu'].append({'id':item_id,'name':item_name})
    with open ('menu.json','w') as tambahdata:
        json.dump(data, tambahdata)
    return data
