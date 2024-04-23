import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.OTSSearchSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OTSSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OTSSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClause, ipOrderNum, ipOrderLine, ipOrderRelNum, ipPageSize, ipabsolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This method will try to mirror the functionality of the base GetRows method but since we are populating
a temp table (BOLSlip) we need our own public method.
Code is based on GetSlips from bo/BOL/BOL.p
   OperationID: Get_GetRows
      :param whereClause: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param ipOrderNum: Desc: Order Num   Required: True
      :param ipOrderLine: Desc: Order Line   Required: True
      :param ipOrderRelNum: Desc: Order Rel Num   Required: True
      :param ipPageSize: Desc: The page size, used only for UI adaptor   Required: True
      :param ipabsolutePage: Desc: The absolute page, used only for the UI adaptor   Required: True
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
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipOrderNum=" + ipOrderNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipOrderLine=" + ipOrderLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipOrderRelNum=" + ipOrderRelNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipPageSize=" + ipPageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipabsolutePage=" + ipabsolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OTSSearchSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_OTSSearchRow:
   def __init__(self, obj):
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  Address 1  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      self.OTSAddress3:str = obj["OTSAddress3"]
      self.OTSCity:str = obj["OTSCity"]
      self.OTSContact:str = obj["OTSContact"]
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      self.OTSName:str = obj["OTSName"]
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      self.OTSResaleID:str = obj["OTSResaleID"]
      self.OTSState:str = obj["OTSState"]
      self.OTSZIP:str = obj["OTSZIP"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OTSSearchTableset:
   def __init__(self, obj):
      self.OTSSearch:list[Erp_Tablesets_OTSSearchRow] = obj["OTSSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetRows_input:
   """ Required : 
   whereClause
   ipOrderNum
   ipOrderLine
   ipOrderRelNum
   ipPageSize
   ipabsolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The where clause to restrict data for  """  
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  Order Num  """  
      self.ipOrderLine:int = obj["ipOrderLine"]
      """  Order Line  """  
      self.ipOrderRelNum:int = obj["ipOrderRelNum"]
      """  Order Rel Num  """  
      self.ipPageSize:int = obj["ipPageSize"]
      """  The page size, used only for UI adaptor  """  
      self.ipabsolutePage:int = obj["ipabsolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OTSSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMorePages:bool = obj["opMorePages"]
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

