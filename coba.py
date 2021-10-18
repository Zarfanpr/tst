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

@app.delete('/menu/remove/{item_id}')
async def delete_menu(item_id:int):
	new_list=[]
	for menu_item in data['menu']:
		if menu_item['id']!=item_id:
			new_list.append({"id":menu_item['id'],"name":menu_item['name']})
	data_dummy={"menu":new_list}
	with open('menu.json', 'w') as outfile:
		json.dump(data_dummy, outfile)
	return data_dummy

@app.put('/menu/update/{item_id}/{item_name}')
async def update_menu(item_id:int,item_name:str):
	new_list=[]
	for menu_item in data['menu']:
		if menu_item['id']==item_id:
			menu_item['name']=item_name
		new_list.append(menu_item)
	data_dummy={"menu":new_list}
	with open('menu.json', 'w') as outfile:
		json.dump(data_dummy, outfile)
	return data_dummy
    
@app.post('/menu/add/{item_id}/{item_name}')
async def add_menu(item_id:int,item_name:str):
	data['menu'].append({'id':item_id,'name':item_name})
	with open('menu.json', 'w') as outfile:
		json.dump(data, outfile)
	return data