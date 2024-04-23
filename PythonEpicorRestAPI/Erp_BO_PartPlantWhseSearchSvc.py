import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartPlantWhseSearchSvc
# Description: Add your summary for this object here
            If PartNumColumnName is populated with a valid part number and UsePartPlant is true the combo will return warehouses defined in PartWhse, otherwise it will return
            the warehouses defined for the plant including shared wharehouses.
            To conditionally control if a valid part number uses PartWhse, either set UsePartPlant manually or set UsePartPlantValueColumn to the name of a column that contains
            a value and UsePartPlantValue to the string that will determine if PartWhse should be used.
            There are 2 examples of where this code is used.
            One is in the "Passed" section of the UI for InspProcessing.p Under tabs PO Receipts/Detail and
            Materials/Detail. The other is in the DMRprocessing.p under tab Accept/Stock/Detail
           
            The following properties must be set on the combo box along with EpiBinding and PartNumColumnName
            UsePartPlant = True, UsePartPlantValue = STK, UsePartPlantValueColumn = PassedIssuedTo.
           
            There are 2 examples of where this code is used.
            One is in the "Passed" section of the UI for InspProcessing.p Under tabs PO Receipts/Detail and
            Materials/Detail. The other is in the DMRprocessing.p under tab Accept/Stock/Detail
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantWhseSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantWhseSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(vPart, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This method returns a list of warehouses (including shared warehouses)
available for a plant.  The Plant parameter allows the user to search
on just one plant or leave blank to search on all plants.
   OperationID: Get_GetRows
      :param vPart: Desc: Part   Required: True   Allow empty value : True
      :param pageSize: Desc: pageSize   Required: True
      :param absolutePage: Desc: absolutePage   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vPart=" + vPart
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantWhseSearchSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_PartPlantWhseSearchRow:
   def __init__(self, obj):
      self.Description:str = obj["Description"]
      """  Warehouse Description  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse Code  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartPlantWhseSearchTableset:
   def __init__(self, obj):
      self.PartPlantWhseSearch:list[Erp_Tablesets_PartPlantWhseSearchRow] = obj["PartPlantWhseSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetRows_input:
   """ Required : 
   vPart
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.vPart:str = obj["vPart"]
      """  Part  """  
      self.pageSize:int = obj["pageSize"]
      """  pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartPlantWhseSearchTableset] = obj["returnObj"]
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

