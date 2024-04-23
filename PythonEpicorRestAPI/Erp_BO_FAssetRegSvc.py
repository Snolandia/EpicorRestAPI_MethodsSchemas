import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FAssetRegSvc
# Description: Fixed Asset Register
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FAssetRegs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FAssetRegs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAssetRegs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/FAssetRegs",headers=creds) as resp:
           return await resp.json()

async def post_FAssetRegs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAssetRegs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAssetRegRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAssetRegRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/FAssetRegs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FAssetRegs_Company_AssetRegID(Company, AssetRegID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAssetReg item
   Description: Calls GetByID to retrieve the FAssetReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/FAssetRegs(" + Company + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FAssetRegs_Company_AssetRegID(Company, AssetRegID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FAssetReg for the service
   Description: Calls UpdateExt to update FAssetReg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAssetReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAssetRegRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/FAssetRegs(" + Company + "," + AssetRegID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FAssetRegs_Company_AssetRegID(Company, AssetRegID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FAssetReg item
   Description: Call UpdateExt to delete FAssetReg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAssetReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/FAssetRegs(" + Company + "," + AssetRegID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetRegListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFAssetReg, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFAssetReg=" + whereClauseFAssetReg
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(assetRegID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "assetRegID=" + assetRegID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultFAssetReg(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultFAssetReg
   Description: This method returns ID of the dafault Asset Register.
   OperationID: GetDefaultFAssetReg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultFAssetReg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBookID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBookID
   Description: This method is called when the BookID changes.  This validates if the
GL Book is valid and if book's calendar can be defaulted to asset register.
   OperationID: OnChangeBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCalendarID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCalendarID
   Description: This method is called when the CalendarID changes.  This validates if the
Calendar has an open Asset Fiscal Period that can be used as default.
   OperationID: OnChangeCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFAssetReg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFAssetReg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAssetReg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAssetReg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAssetReg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetRegSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetRegListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAssetRegListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetRegRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAssetRegRow] = obj["value"]
      pass

class Erp_Tablesets_FAssetRegListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.Description:str = obj["Description"]
      """  Asset Register description.  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the Asset Calendar used when posting asset activities.  This calendar could be different from the G/L Book Fiscal Calendar.  """  
      self.DefaultReg:bool = obj["DefaultReg"]
      """  Indicates if the asset register is the default register.  """  
      self.CurrentFiscalYear:int = obj["CurrentFiscalYear"]
      """  The current fiscal year for assets.  """  
      self.CurrentFiscalPeriod:int = obj["CurrentFiscalPeriod"]
      """  The current fiscal period of assets.  """  
      self.CurrentFiscalYearSuffix:str = obj["CurrentFiscalYearSuffix"]
      """  Current fiscal year suffix.  """  
      self.RetroAdjust:bool = obj["RetroAdjust"]
      """  Flag to indicate if the changes in asset depreciation costs, due to an adjustment of asset cost or depreciation parameters, will affect the current year depreciation calculation.  """  
      self.DepRevalueMethod:str = obj["DepRevalueMethod"]
      """   Default Revaluation Method.  Possible values are:
NETVAL - Restate Net Value
GROSSVAL - Restate Gross Value and Depreciation  """  
      self.AllowUpwardRevalue:bool = obj["AllowUpwardRevalue"]
      """  Allow upward asset cost revaluation.  """  
      self.TransRevalSurplus:bool = obj["TransRevalSurplus"]
      """  Flag to indicate if the Revaluation Surplus should be automatically transferred to retained earnings account at full disposal of the asset.  """  
      self.DynamicDepYear:bool = obj["DynamicDepYear"]
      """  Flag to indicate if dynamic depreciation year should be used instead of the Fiscal Year to influence the depreciation schedule.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAssetRegRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.Description:str = obj["Description"]
      """  Asset Register description.  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the Asset Calendar used when posting asset activities.  This calendar could be different from the G/L Book Fiscal Calendar.  """  
      self.DefaultReg:bool = obj["DefaultReg"]
      """  Indicates if the asset register is the default register.  """  
      self.CurrentFiscalYear:int = obj["CurrentFiscalYear"]
      """  The current fiscal year for assets.  """  
      self.CurrentFiscalPeriod:int = obj["CurrentFiscalPeriod"]
      """  The current fiscal period of assets.  """  
      self.CurrentFiscalYearSuffix:str = obj["CurrentFiscalYearSuffix"]
      """  Current fiscal year suffix.  """  
      self.RetroAdjust:bool = obj["RetroAdjust"]
      """  Flag to indicate if the changes in asset depreciation costs, due to an adjustment of asset cost or depreciation parameters, will affect the current year depreciation calculation.  """  
      self.DepRevalueMethod:str = obj["DepRevalueMethod"]
      """   Default Revaluation Method.  Possible values are:
NETVAL - Restate Net Value
GROSSVAL - Restate Gross Value and Depreciation  """  
      self.AllowUpwardRevalue:bool = obj["AllowUpwardRevalue"]
      """  Allow upward asset cost revaluation.  """  
      self.TransRevalSurplus:bool = obj["TransRevalSurplus"]
      """  Flag to indicate if the Revaluation Surplus should be automatically transferred to retained earnings account at full disposal of the asset.  """  
      self.DynamicDepYear:bool = obj["DynamicDepYear"]
      """  Flag to indicate if dynamic depreciation year should be used instead of the Fiscal Year to influence the depreciation schedule.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   assetRegID
   """  
   def __init__(self, obj):
      self.assetRegID:str = obj["assetRegID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FAssetRegListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.Description:str = obj["Description"]
      """  Asset Register description.  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the Asset Calendar used when posting asset activities.  This calendar could be different from the G/L Book Fiscal Calendar.  """  
      self.DefaultReg:bool = obj["DefaultReg"]
      """  Indicates if the asset register is the default register.  """  
      self.CurrentFiscalYear:int = obj["CurrentFiscalYear"]
      """  The current fiscal year for assets.  """  
      self.CurrentFiscalPeriod:int = obj["CurrentFiscalPeriod"]
      """  The current fiscal period of assets.  """  
      self.CurrentFiscalYearSuffix:str = obj["CurrentFiscalYearSuffix"]
      """  Current fiscal year suffix.  """  
      self.RetroAdjust:bool = obj["RetroAdjust"]
      """  Flag to indicate if the changes in asset depreciation costs, due to an adjustment of asset cost or depreciation parameters, will affect the current year depreciation calculation.  """  
      self.DepRevalueMethod:str = obj["DepRevalueMethod"]
      """   Default Revaluation Method.  Possible values are:
NETVAL - Restate Net Value
GROSSVAL - Restate Gross Value and Depreciation  """  
      self.AllowUpwardRevalue:bool = obj["AllowUpwardRevalue"]
      """  Allow upward asset cost revaluation.  """  
      self.TransRevalSurplus:bool = obj["TransRevalSurplus"]
      """  Flag to indicate if the Revaluation Surplus should be automatically transferred to retained earnings account at full disposal of the asset.  """  
      self.DynamicDepYear:bool = obj["DynamicDepYear"]
      """  Flag to indicate if dynamic depreciation year should be used instead of the Fiscal Year to influence the depreciation schedule.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAssetRegListTableset:
   def __init__(self, obj):
      self.FAssetRegList:list[Erp_Tablesets_FAssetRegListRow] = obj["FAssetRegList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FAssetRegRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.Description:str = obj["Description"]
      """  Asset Register description.  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the Asset Calendar used when posting asset activities.  This calendar could be different from the G/L Book Fiscal Calendar.  """  
      self.DefaultReg:bool = obj["DefaultReg"]
      """  Indicates if the asset register is the default register.  """  
      self.CurrentFiscalYear:int = obj["CurrentFiscalYear"]
      """  The current fiscal year for assets.  """  
      self.CurrentFiscalPeriod:int = obj["CurrentFiscalPeriod"]
      """  The current fiscal period of assets.  """  
      self.CurrentFiscalYearSuffix:str = obj["CurrentFiscalYearSuffix"]
      """  Current fiscal year suffix.  """  
      self.RetroAdjust:bool = obj["RetroAdjust"]
      """  Flag to indicate if the changes in asset depreciation costs, due to an adjustment of asset cost or depreciation parameters, will affect the current year depreciation calculation.  """  
      self.DepRevalueMethod:str = obj["DepRevalueMethod"]
      """   Default Revaluation Method.  Possible values are:
NETVAL - Restate Net Value
GROSSVAL - Restate Gross Value and Depreciation  """  
      self.AllowUpwardRevalue:bool = obj["AllowUpwardRevalue"]
      """  Allow upward asset cost revaluation.  """  
      self.TransRevalSurplus:bool = obj["TransRevalSurplus"]
      """  Flag to indicate if the Revaluation Surplus should be automatically transferred to retained earnings account at full disposal of the asset.  """  
      self.DynamicDepYear:bool = obj["DynamicDepYear"]
      """  Flag to indicate if dynamic depreciation year should be used instead of the Fiscal Year to influence the depreciation schedule.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAssetRegTableset:
   def __init__(self, obj):
      self.FAssetReg:list[Erp_Tablesets_FAssetRegRow] = obj["FAssetReg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtFAssetRegTableset:
   def __init__(self, obj):
      self.FAssetReg:list[Erp_Tablesets_FAssetRegRow] = obj["FAssetReg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   assetRegID
   """  
   def __init__(self, obj):
      self.assetRegID:str = obj["assetRegID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FAssetRegTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FAssetRegTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FAssetRegTableset] = obj["returnObj"]
      pass

class GetDefaultFAssetReg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFAssetRegID:str = obj["parameters"]
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
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FAssetRegListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFAssetReg_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAssetRegTableset] = obj["ds"]
      pass

class GetNewFAssetReg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetRegTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFAssetReg
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFAssetReg:str = obj["whereClauseFAssetReg"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FAssetRegTableset] = obj["returnObj"]
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

class OnChangeBookID_input:
   """ Required : 
   ipBookID
   ds
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  The proposed BookID  """  
      self.ds:list[Erp_Tablesets_FAssetRegTableset] = obj["ds"]
      pass

class OnChangeBookID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetRegTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCalendarID_input:
   """ Required : 
   ipCalendarID
   ds
   """  
   def __init__(self, obj):
      self.ipCalendarID:str = obj["ipCalendarID"]
      """  The proposed CalendarID  """  
      self.ds:list[Erp_Tablesets_FAssetRegTableset] = obj["ds"]
      pass

class OnChangeCalendarID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetRegTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFAssetRegTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFAssetRegTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAssetRegTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetRegTableset] = obj["ds"]
      pass

      """  output parameters  """  

