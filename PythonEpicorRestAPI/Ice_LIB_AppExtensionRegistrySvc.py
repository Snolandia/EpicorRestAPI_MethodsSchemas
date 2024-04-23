import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.AppExtensionRegistrySvc
# Description: Represents the Application Extension Registry.
(acts as the REST controller)
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.AppExtensionRegistrySvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.AppExtensionRegistrySvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_SetEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetEntity
   Description: Set the Application Extension Entity.
   OperationID: SetEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.AppExtensionRegistrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetEntities(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetEntities
   Description: Set the Application Extension Entity.
   OperationID: SetEntities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetEntities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetEntities_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.AppExtensionRegistrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEntity
   Description: Get the Application Extension Entity.
   OperationID: GetEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.AppExtensionRegistrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteEntity
   Description: Delete the Application Extension Entity.
   OperationID: DeleteEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.AppExtensionRegistrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEntities(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEntities
   Description: Get the Application Extension Entity.
   OperationID: GetEntities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEntities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEntities_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.AppExtensionRegistrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEntityList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEntityList
   Description: Get the collection of Application Extension Entity Ids.
   OperationID: GetEntityList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEntityList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEntityList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.AppExtensionRegistrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DeleteEntity_input:
   """ Required : 
   id
   type
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      """  The Id for the Extension Entity.  """  
      self.type:str = obj["type"]
      """  The Type of Entity (Extension, Widget, Component).  """  
      pass

class DeleteEntity_output:
   def __init__(self, obj):
      pass

class GetEntities_input:
   """ Required : 
   type
   options
   """  
   def __init__(self, obj):
      self.type:str = obj["type"]
      """  The Type of Entity (Extension, Widget, Component).  """  
      self.options      #schema had no properties on an object.
      pass

class GetEntities_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_AppExtensionRegistry_EntityRequest] = obj["returnObj"]
      """  The EntityRequest that contains the id and entity  """  
      pass

class GetEntityList_input:
   """ Required : 
   type
   options
   """  
   def __init__(self, obj):
      self.type:str = obj["type"]
      """  The Type of Entity (Extension, Widget, Component).  """  
      self.options      #schema had no properties on an object.
      pass

class GetEntityList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  collection of Application Extension Entity Ids.  """  
      pass

class GetEntity_input:
   """ Required : 
   id
   type
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      """  The Id for the Extension Entity.  """  
      self.type:str = obj["type"]
      """  The Type of Entity (Extension, Widget, Component).  """  
      pass

class GetEntity_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_AppExtensionRegistry_EntityRequest] = obj["returnObj"]
      pass

class Ice_Lib_AppExtensionRegistry_EntityRequest:
   def __init__(self, obj):
      self.entity      #schema had no properties on an object.
      pass

class SetEntities_input:
   """ Required : 
   type
   entities
   """  
   def __init__(self, obj):
      self.type:str = obj["type"]
      """  The Type of Entity (Extension, Widget, Component).  """  
      self.entities:list[Ice_Lib_AppExtensionRegistry_EntityRequest] = obj["entities"]
      """  The object that represents the collection of entities.  """  
      pass

class SetEntities_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_AppExtensionRegistry_EntityRequest] = obj["returnObj"]
      """  The EntityRequest that contains the id and entity  """  
      pass

class SetEntity_input:
   """ Required : 
   type
   request
   """  
   def __init__(self, obj):
      self.type:str = obj["type"]
      """  The Type of Entity (Extension, Widget, Component).  """  
      self.request:list[Ice_Lib_AppExtensionRegistry_EntityRequest] = obj["request"]
      pass

class SetEntity_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_AppExtensionRegistry_EntityRequest] = obj["returnObj"]
      pass

