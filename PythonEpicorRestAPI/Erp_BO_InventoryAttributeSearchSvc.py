import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.InventoryAttributeSearchSvc
# Description: Service to search attribute sets and part bin if qualified
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InventoryAttributeSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDynAttrValueSet, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This service will return all attribute sets based on AttrClassID and joining PartBin.
This method will try to mirror the functionality of the base GetList method, but since we are
populating a temp table (InventoryAttributeSearch) we need our own public method.
   OperationID: Get_GetRows
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
   params += "whereClauseDynAttrValueSet=" + whereClauseDynAttrValueSet
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClauseDynAttrValueSet, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: This service will return all attributes sets based on AttrClassID and attribute values
This method will try to mirror the functionality of the base GetList method, but since we are
populating a temp table (InventoryAttributeSearchList) we need our own public method.
   OperationID: Get_GetList
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDynAttrValueSet=" + whereClauseDynAttrValueSet
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListWithAttributeList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListWithAttributeList
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause to pass into GetList
   OperationID: GetListWithAttributeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListWithAttributeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListWithAttributeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForLotTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForLotTracker
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause to pass into GetList
   OperationID: GetListForLotTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForLotTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForLotTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsPartLotDynAttrValueSetView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsPartLotDynAttrValueSetView
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause to pass into GetList
   OperationID: GetRowsPartLotDynAttrValueSetView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsPartLotDynAttrValueSetView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPartLotDynAttrValueSetView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAttrClassID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAttrClassID
   Description: Returns AttrClassID for a Part
   OperationID: GetAttrClassID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttrClassID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttrClassID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryAttributeSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InventoryAttributeSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InventoryAttributeSearchListRow] = obj["value"]
      pass

class Erp_Tablesets_InventoryAttributeSearchListRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Company:str = obj["Company"]
      """  Company identifier.  """  
      self.Description:str = obj["Description"]
      """  Description of attribute set.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  Short Decription of attribute set.  """  
      self.PlanningAttributeSetSeq:int = obj["PlanningAttributeSetSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_InventoryAttributeSearchListRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Company:str = obj["Company"]
      """  Company identifier.  """  
      self.Description:str = obj["Description"]
      """  Description of attribute set.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  Short Decription of attribute set.  """  
      self.PlanningAttributeSetSeq:int = obj["PlanningAttributeSetSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InventoryAttributeSearchListTableset:
   def __init__(self, obj):
      self.InventoryAttributeSearchList:list[Erp_Tablesets_InventoryAttributeSearchListRow] = obj["InventoryAttributeSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InventoryAttributeSearchRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Company:str = obj["Company"]
      """  Company identifier.  """  
      self.Description:str = obj["Description"]
      """  Description of attribute set.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  Short Decription of attribute set.  """  
      self.PlanningAttributeSetSeq:int = obj["PlanningAttributeSetSeq"]
      """  The unique identifier of the Dynamic Attribute Planning Set.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  Total on hand qty for a specific part/lot  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InventoryAttributeSearchTableset:
   def __init__(self, obj):
      self.InventoryAttributeSearch:list[Erp_Tablesets_InventoryAttributeSearchRow] = obj["InventoryAttributeSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAttrClassID_input:
   """ Required : 
   company
   partNum
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.partNum:str = obj["partNum"]
      pass

class GetAttrClassID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetListForLotTracker_input:
   """ Required : 
   whereClauseDynAttrValueSet
   attrClassID
   attributeListString
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrValueSet:str = obj["whereClauseDynAttrValueSet"]
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

class GetListForLotTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAttributeSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListWithAttributeList_input:
   """ Required : 
   whereClauseDynAttrValueSet
   attrClassID
   attributeListString
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrValueSet:str = obj["whereClauseDynAttrValueSet"]
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

class GetListWithAttributeList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAttributeSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClauseDynAttrValueSet
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrValueSet:str = obj["whereClauseDynAttrValueSet"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAttributeSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsPartLotDynAttrValueSetView_input:
   """ Required : 
   whereClauseDynAttrValueSet
   attrClassID
   attributeListString
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrValueSet:str = obj["whereClauseDynAttrValueSet"]
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

class GetRowsPartLotDynAttrValueSetView_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAttributeSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDynAttrValueSet
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrValueSet:str = obj["whereClauseDynAttrValueSet"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryAttributeSearchTableset] = obj["returnObj"]
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

