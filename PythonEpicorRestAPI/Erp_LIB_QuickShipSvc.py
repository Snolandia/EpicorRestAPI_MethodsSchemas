import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.LIB.QuickShipSvc
# Description: QuickShip library
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.LIB.QuickShipSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.LIB.QuickShipSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetQuickShipURL(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQuickShipURL
   OperationID: GetQuickShipURL
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuickShipURL_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuickShipURL_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.LIB.QuickShipSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetQuickShipURL_input:
   """ Required : 
   packNum
   launchedFromType
   quickShipPage
   urlOverride
   shipVia
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      self.launchedFromType:str = obj["launchedFromType"]
      self.quickShipPage:str = obj["quickShipPage"]
      self.urlOverride:str = obj["urlOverride"]
      self.shipVia:str = obj["shipVia"]
      pass

class GetQuickShipURL_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.quickShipURL:str = obj["parameters"]
      pass

      """  output parameters  """  

