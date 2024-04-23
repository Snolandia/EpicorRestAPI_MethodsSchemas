import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MESMenuSearchSvc
# Description: This object does not have update capabilities.
Only record retrieval is available.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MESMenuSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MESMenuSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MESMenuSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MESMenuRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/MESMenuSearches",headers=creds) as resp:
           return await resp.json()

async def post_MESMenuSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MESMenuSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MESMenuRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MESMenuRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/MESMenuSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MESMenuSearches_Company_MESMenuID(Company, MESMenuID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MESMenuSearch item
   Description: Calls GetByID to retrieve the MESMenuSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MESMenuSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MESMenuID: Desc: MESMenuID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MESMenuRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/MESMenuSearches(" + Company + "," + MESMenuID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MESMenuSearches_Company_MESMenuID(Company, MESMenuID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MESMenuSearch for the service
   Description: Calls UpdateExt to update MESMenuSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MESMenuSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MESMenuID: Desc: MESMenuID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MESMenuRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/MESMenuSearches(" + Company + "," + MESMenuID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MESMenuSearches_Company_MESMenuID(Company, MESMenuID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MESMenuSearch item
   Description: Call UpdateExt to delete MESMenuSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MESMenuSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MESMenuID: Desc: MESMenuID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/MESMenuSearches(" + Company + "," + MESMenuID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MESMenuListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMESMenu, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
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
   params += "whereClauseMESMenu=" + whereClauseMESMenu
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(meSMenuID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "meSMenuID=" + meSMenuID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
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
   params += "whereClause=" + whereClause
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMESMenu(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMESMenu
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMESMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMESMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMESMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MESMenuListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MESMenuListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MESMenuRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MESMenuRow] = obj["value"]
      pass

class Erp_Tablesets_MESMenuListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company, if MESMenu row is generated data. For system data this is empty.  """  
      self.MESMenuID:int = obj["MESMenuID"]
      """  Unique identifier for the record  """  
      self.ParentMESMenuID:int = obj["ParentMESMenuID"]
      """  Unique identifier of the parent record. This is be the menu it will be displayed under on the Handheld MESand in the maintenance program.  """  
      self.MenuType:str = obj["MenuType"]
      """  Type of menu. H = Handheld MES / M = MES  """  
      self.Seq:int = obj["Seq"]
      """  Used to sort the items on the Handheld MES menu. Low to high.  """  
      self.MenuID:str = obj["MenuID"]
      """  The system menu IDof the menu item to invoke when the user selects this item on the menu. Blank for menus.  """  
      self.MenuDesc:str = obj["MenuDesc"]
      """  The description that appears on the Handheld MES menu and in the maintenance program.  """  
      self.Hidden:bool = obj["Hidden"]
      """  True if the item should be hidden from the Handheld MES menu.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  True if row is system data, false for data generated for specific company  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MESMenuRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company, if MESMenu row is generated data. For system data this is empty.  """  
      self.MESMenuID:int = obj["MESMenuID"]
      """  Unique identifier for the record  """  
      self.ParentMESMenuID:int = obj["ParentMESMenuID"]
      """  Unique identifier of the parent record. This is be the menu it will be displayed under on the Handheld MESand in the maintenance program.  """  
      self.MenuType:str = obj["MenuType"]
      """  Type of menu. H = Handheld MES / M = MES  """  
      self.Seq:int = obj["Seq"]
      """  Used to sort the items on the Handheld MES menu. Low to high.  """  
      self.MenuID:str = obj["MenuID"]
      """  The system menu IDof the menu item to invoke when the user selects this item on the menu. Blank for menus.  """  
      self.MenuDesc:str = obj["MenuDesc"]
      """  The description that appears on the Handheld MES menu and in the maintenance program.  """  
      self.Hidden:bool = obj["Hidden"]
      """  True if the item should be hidden from the Handheld MES menu.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  True if row is system data, false for data generated for specific company  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.MESMaterialHandler:bool = obj["MESMaterialHandler"]
      self.MESSupervisor:bool = obj["MESSupervisor"]
      self.MESShipping:bool = obj["MESShipping"]
      self.MESProduction:bool = obj["MESProduction"]
      self.MESService:bool = obj["MESService"]
      self.PCIDInbound:bool = obj["PCIDInbound"]
      self.PCIDOutbound:bool = obj["PCIDOutbound"]
      self.PCIDInventory:bool = obj["PCIDInventory"]
      self.PCIDManufacturing:bool = obj["PCIDManufacturing"]
      self.PCIDQuality:bool = obj["PCIDQuality"]
      self.CurrentEmpAllowed:bool = obj["CurrentEmpAllowed"]
      self.TranslateMenuDesc:str = obj["TranslateMenuDesc"]
      self.DisableRow:bool = obj["DisableRow"]
      """  Indicates if the row is disabled  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   meSMenuID
   """  
   def __init__(self, obj):
      self.meSMenuID:int = obj["meSMenuID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MESMenuListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company, if MESMenu row is generated data. For system data this is empty.  """  
      self.MESMenuID:int = obj["MESMenuID"]
      """  Unique identifier for the record  """  
      self.ParentMESMenuID:int = obj["ParentMESMenuID"]
      """  Unique identifier of the parent record. This is be the menu it will be displayed under on the Handheld MESand in the maintenance program.  """  
      self.MenuType:str = obj["MenuType"]
      """  Type of menu. H = Handheld MES / M = MES  """  
      self.Seq:int = obj["Seq"]
      """  Used to sort the items on the Handheld MES menu. Low to high.  """  
      self.MenuID:str = obj["MenuID"]
      """  The system menu IDof the menu item to invoke when the user selects this item on the menu. Blank for menus.  """  
      self.MenuDesc:str = obj["MenuDesc"]
      """  The description that appears on the Handheld MES menu and in the maintenance program.  """  
      self.Hidden:bool = obj["Hidden"]
      """  True if the item should be hidden from the Handheld MES menu.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  True if row is system data, false for data generated for specific company  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MESMenuListTableset:
   def __init__(self, obj):
      self.MESMenuList:list[Erp_Tablesets_MESMenuListRow] = obj["MESMenuList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MESMenuRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company, if MESMenu row is generated data. For system data this is empty.  """  
      self.MESMenuID:int = obj["MESMenuID"]
      """  Unique identifier for the record  """  
      self.ParentMESMenuID:int = obj["ParentMESMenuID"]
      """  Unique identifier of the parent record. This is be the menu it will be displayed under on the Handheld MESand in the maintenance program.  """  
      self.MenuType:str = obj["MenuType"]
      """  Type of menu. H = Handheld MES / M = MES  """  
      self.Seq:int = obj["Seq"]
      """  Used to sort the items on the Handheld MES menu. Low to high.  """  
      self.MenuID:str = obj["MenuID"]
      """  The system menu IDof the menu item to invoke when the user selects this item on the menu. Blank for menus.  """  
      self.MenuDesc:str = obj["MenuDesc"]
      """  The description that appears on the Handheld MES menu and in the maintenance program.  """  
      self.Hidden:bool = obj["Hidden"]
      """  True if the item should be hidden from the Handheld MES menu.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  True if row is system data, false for data generated for specific company  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.MESMaterialHandler:bool = obj["MESMaterialHandler"]
      self.MESSupervisor:bool = obj["MESSupervisor"]
      self.MESShipping:bool = obj["MESShipping"]
      self.MESProduction:bool = obj["MESProduction"]
      self.MESService:bool = obj["MESService"]
      self.PCIDInbound:bool = obj["PCIDInbound"]
      self.PCIDOutbound:bool = obj["PCIDOutbound"]
      self.PCIDInventory:bool = obj["PCIDInventory"]
      self.PCIDManufacturing:bool = obj["PCIDManufacturing"]
      self.PCIDQuality:bool = obj["PCIDQuality"]
      self.CurrentEmpAllowed:bool = obj["CurrentEmpAllowed"]
      self.TranslateMenuDesc:str = obj["TranslateMenuDesc"]
      self.DisableRow:bool = obj["DisableRow"]
      """  Indicates if the row is disabled  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MESMenuSearchTableset:
   def __init__(self, obj):
      self.MESMenu:list[Erp_Tablesets_MESMenuRow] = obj["MESMenu"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMESMenuSearchTableset:
   def __init__(self, obj):
      self.MESMenu:list[Erp_Tablesets_MESMenuRow] = obj["MESMenu"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   meSMenuID
   """  
   def __init__(self, obj):
      self.meSMenuID:int = obj["meSMenuID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MESMenuSearchTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MESMenuSearchTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MESMenuSearchTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MESMenuListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMESMenu_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MESMenuSearchTableset] = obj["ds"]
      pass

class GetNewMESMenu_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MESMenuSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMESMenu
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMESMenu:str = obj["whereClauseMESMenu"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MESMenuSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMESMenuSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMESMenuSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MESMenuSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MESMenuSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

