import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.FieldHelpSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.FieldHelpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.FieldHelpSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetFieldHelp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldHelp
   Description: Returns the field help text from the database.
   OperationID: GetFieldHelp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldHelp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldHelp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FieldHelpSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetFieldHelp_input:
   """ Required : 
   systemCode
   dataTableID
   fieldName
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  The SystemCode.  """  
      self.dataTableID:str = obj["dataTableID"]
      """  The DataTableID.  """  
      self.fieldName:str = obj["fieldName"]
      """  The FieldName.  """  
      pass

class GetFieldHelp_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The HelpText from the FieldHelp table.  """  
      pass

