import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.WhsePartWhseSearchSvc
# Description: This object replaces the current Warehouse object in some cases
when building the combo-boxes/searches.  This is a non-standard
object that will include shared warehouses in the result list.
This will call PartWhseSearch is partnum is passed, otherwise
it will call WarehseSearch.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhsePartWhseSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhsePartWhseSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhsePartWhseSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhsePartWhseSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: This method returns a list of warehouses (including shared warehouses)
available for a plant.
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhsePartWhseSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForDefinedPlantOrPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForDefinedPlantOrPartNum
   Description: This method returns a list of warehouses (including shared warehouses)
available for a plant. Created for usage at the MetaFx
   OperationID: GetListForDefinedPlantOrPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForDefinedPlantOrPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForDefinedPlantOrPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhsePartWhseSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhsePartWhseSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhsePartWhseSearchListRow] = obj["value"]
      pass

class Erp_Tablesets_WhsePartWhseSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Description:str = obj["Description"]
      self.IsUserAllowed:bool = obj["IsUserAllowed"]
      """  Determines if a User has the rights to perform Adjustments on this Warehouse  """  
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.RemotePlant:str = obj["RemotePlant"]
      """  Indicate which is the Shared Site for the Shared Warehouse. If is empty is because is not a Shared Warehouse.  """  
      self.SharedWarehouse:bool = obj["SharedWarehouse"]
      """  Determine if this Warehouse is a Shared Warehouse  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_WhsePartWhseSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Description:str = obj["Description"]
      self.IsUserAllowed:bool = obj["IsUserAllowed"]
      """  Determines if a User has the rights to perform Adjustments on this Warehouse  """  
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.RemotePlant:str = obj["RemotePlant"]
      """  Indicate which is the Shared Site for the Shared Warehouse. If is empty is because is not a Shared Warehouse.  """  
      self.SharedWarehouse:bool = obj["SharedWarehouse"]
      """  Determine if this Warehouse is a Shared Warehouse  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhsePartWhseSearchListTableset:
   def __init__(self, obj):
      self.WhsePartWhseSearchList:list[Erp_Tablesets_WhsePartWhseSearchListRow] = obj["WhsePartWhseSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetListForDefinedPlantOrPartNum_input:
   """ Required : 
   plantId
   partNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.plantId:str = obj["plantId"]
      """  Plant ID  """  
      self.partNum:str = obj["partNum"]
      """  Part ID  """  
      self.pageSize:int = obj["pageSize"]
      """  page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolute Page  """  
      pass

class GetListForDefinedPlantOrPartNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WhsePartWhseSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  PartNum to search the warehouses for, blank for all warehouses  """  
      self.pageSize:int = obj["pageSize"]
      """  page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolute Page  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WhsePartWhseSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

