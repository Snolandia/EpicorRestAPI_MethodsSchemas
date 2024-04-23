import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LocationInventorySearchSvc
# Description: Location Inventory Search service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationInventorySearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationInventorySearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLocInvSearch, whereClauseLocInvAddrSearch, whereClauseLocMtl, whereClauseDynAttr, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This methods will return all the LocationInventory records joined with LocationInventoryAddress
This method will try to mirror the functionality of the base GetRows method, but since we are
populating a temp table (LocationInventorySearch) we need our own public method.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "whereClauseLocInvSearch=" + whereClauseLocInvSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLocInvAddrSearch=" + whereClauseLocInvAddrSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLocMtl=" + whereClauseLocMtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDynAttr=" + whereClauseDynAttr
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationInventorySearchSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsWithAttributeList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsWithAttributeList
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause to pass into GetRows
   OperationID: GetRowsWithAttributeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWithAttributeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWithAttributeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationInventorySearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_LocationInventorySearchRow:
   def __init__(self, obj):
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.AddressType:str = obj["AddressType"]
      self.City:str = obj["City"]
      self.Company:str = obj["Company"]
      self.Contact:str = obj["Contact"]
      """  Contact  """  
      self.CountryNum:int = obj["CountryNum"]
      self.CustNum:int = obj["CustNum"]
      self.CustShipToNum:str = obj["CustShipToNum"]
      self.EmailAddress:str = obj["EmailAddress"]
      self.FaxNum:str = obj["FaxNum"]
      self.IDNum:str = obj["IDNum"]
      self.JobNum:str = obj["JobNum"]
      self.LineDesc:str = obj["LineDesc"]
      self.Listing:str = obj["Listing"]
      self.ListingStartDate:str = obj["ListingStartDate"]
      self.LocationNum:int = obj["LocationNum"]
      self.Name:str = obj["Name"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.PackLine:int = obj["PackLine"]
      self.PackNum:int = obj["PackNum"]
      self.PartNum:str = obj["PartNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.Plant:str = obj["Plant"]
      self.SerialNumber:str = obj["SerialNumber"]
      self.State:str = obj["State"]
      self.UseOTS:bool = obj["UseOTS"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      self.WarrantyExpirationDate:str = obj["WarrantyExpirationDate"]
      """  Warranty Expiration Date  """  
      self.WarrantyStartDate:str = obj["WarrantyStartDate"]
      self.Zip:str = obj["Zip"]
      self.LotNum:str = obj["LotNum"]
      self.AddressList:str = obj["AddressList"]
      """  Full address list  """  
      self.Country:str = obj["Country"]
      """  Country description  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationInventorySearchTableset:
   def __init__(self, obj):
      self.LocationInventorySearch:list[Erp_Tablesets_LocationInventorySearchRow] = obj["LocationInventorySearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetRowsWithAttributeList_input:
   """ Required : 
   whereClauseLocInvSearch
   whereClauseLocInvAddrSearch
   whereClauseLocMtl
   whereClauseDynAttr
   attrClassID
   attributeListString
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLocInvSearch:str = obj["whereClauseLocInvSearch"]
      self.whereClauseLocInvAddrSearch:str = obj["whereClauseLocInvAddrSearch"]
      self.whereClauseLocMtl:str = obj["whereClauseLocMtl"]
      self.whereClauseDynAttr:str = obj["whereClauseDynAttr"]
      self.attrClassID:str = obj["attrClassID"]
      """  AttrClassID value  """  
      self.attributeListString:str = obj["attributeListString"]
      """  A list of attributes separated by ~.  Each attribute is made up of the following separated by `:
            1. SysRowID of DynAttrClassDtl record
            2. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
            3. The attribute value to filter on  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsWithAttributeList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LocationInventorySearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseLocInvSearch
   whereClauseLocInvAddrSearch
   whereClauseLocMtl
   whereClauseDynAttr
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLocInvSearch:str = obj["whereClauseLocInvSearch"]
      self.whereClauseLocInvAddrSearch:str = obj["whereClauseLocInvAddrSearch"]
      self.whereClauseLocMtl:str = obj["whereClauseLocMtl"]
      self.whereClauseDynAttr:str = obj["whereClauseDynAttr"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LocationInventorySearchTableset] = obj["returnObj"]
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

