import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FARevalueRegSearchSvc
# Description: class FARevalueRegSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FARevalueRegSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FARevalueRegSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FARevalueRegSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueRegSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/FARevalueRegSearches",headers=creds) as resp:
           return await resp.json()

async def post_FARevalueRegSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FARevalueRegSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FARevalueRegSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FARevalueRegSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/FARevalueRegSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FARevalueRegSearches_Company_AssetNum_RevalueNum_AssetRegID(Company, AssetNum, RevalueNum, AssetRegID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FARevalueRegSearch item
   Description: Calls GetByID to retrieve the FARevalueRegSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalueRegSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FARevalueRegSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/FARevalueRegSearches(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FARevalueRegSearches_Company_AssetNum_RevalueNum_AssetRegID(Company, AssetNum, RevalueNum, AssetRegID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FARevalueRegSearch for the service
   Description: Calls UpdateExt to update FARevalueRegSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FARevalueRegSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FARevalueRegSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/FARevalueRegSearches(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FARevalueRegSearches_Company_AssetNum_RevalueNum_AssetRegID(Company, AssetNum, RevalueNum, AssetRegID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FARevalueRegSearch item
   Description: Call UpdateExt to delete FARevalueRegSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FARevalueRegSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param RevalueNum: Desc: RevalueNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/FARevalueRegSearches(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueRegListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFARevalueRegSearch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFARevalueRegSearch=" + whereClauseFARevalueRegSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(assetNum, revalueNum, assetRegID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
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
   params += "assetNum=" + assetNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "revalueNum=" + revalueNum
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFARevalueRegSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFARevalueRegSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFARevalueRegSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFARevalueRegSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFARevalueRegSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FARevalueRegListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FARevalueRegSearchRow] = obj["value"]
      pass

class Erp_Tablesets_FARevalueRegListRow:
   def __init__(self, obj):
      self.AssetNum:str = obj["AssetNum"]
      """  Asset Number  """  
      self.RevalueNum:int = obj["RevalueNum"]
      """  Unique number to identify the Revaluation activity of an asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Uniquue identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FARevalueRegSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset Number  """  
      self.RevalueNum:int = obj["RevalueNum"]
      """  Unique number to identify the Revaluation activity of an asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.OrigCurrentCost:int = obj["OrigCurrentCost"]
      """  The original Current Asset Cost in base currency before running the Asset Revaluation process.  """  
      self.DocOrigCurrentCost:int = obj["DocOrigCurrentCost"]
      """  The original Current Asset Cost in document currency before running the Asset Revaluation process.  """  
      self.Rpt1OrigCurrentCost:int = obj["Rpt1OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.Rpt2OrigCurrentCost:int = obj["Rpt2OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.Rpt3OrigCurrentCost:int = obj["Rpt3OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.OrigBookValue:int = obj["OrigBookValue"]
      """  Book Value before revaluation in base currency.  """  
      self.DocOrigBookValue:int = obj["DocOrigBookValue"]
      """  Book Value before revaluation in document currency.  """  
      self.Rpt1OrigBookValue:int = obj["Rpt1OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.Rpt2OrigBookValue:int = obj["Rpt2OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.Rpt3OrigBookValue:int = obj["Rpt3OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.OrigTotalDepn:int = obj["OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in base curreny.  """  
      self.DocOrigTotalDepn:int = obj["DocOrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in document curreny.  """  
      self.Rpt1OrigTotalDepn:int = obj["Rpt1OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.Rpt2OrigTotalDepn:int = obj["Rpt2OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.Rpt3OrigTotalDepn:int = obj["Rpt3OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.RevalueGainLoss:int = obj["RevalueGainLoss"]
      """  Revaluation Gain or Loss in base currency. The difference between Original Book Value and New Book Value  """  
      self.DocRevalueGainLoss:int = obj["DocRevalueGainLoss"]
      """  Revaluation Gain or Loss in document currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt1RevalueGainLoss:int = obj["Rpt1RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt2RevalueGainLoss:int = obj["Rpt2RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt3RevalueGainLoss:int = obj["Rpt3RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.RevalueSurplus:int = obj["RevalueSurplus"]
      """  Revaluation Surplus in base currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.DocRevalueSurplus:int = obj["DocRevalueSurplus"]
      """  Revaluation Surplus in document currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt1RevalueSurplus:int = obj["Rpt1RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt2RevalueSurplus:int = obj["Rpt2RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt3RevalueSurplus:int = obj["Rpt3RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in base currency.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in document currency.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.GrantDepnAmt:int = obj["GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in base currency.  """  
      self.DocGrantDepnAmt:int = obj["DocGrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in document currency.  """  
      self.Rpt1GrantDepnAmt:int = obj["Rpt1GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt2GrantDepnAmt:int = obj["Rpt2GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt3GrantDepnAmt:int = obj["Rpt3GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.UnusedGrantAmt:int = obj["UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in base currency.  """  
      self.DocUnusedGrantAmt:int = obj["DocUnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in document currency.  """  
      self.Rpt1UnusedGrantAmt:int = obj["Rpt1UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.Rpt2UnusedGrantAmt:int = obj["Rpt2UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.Rpt3UnusedGrantAmt:int = obj["Rpt3UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.PostedFutrDepnAmt:int = obj["PostedFutrDepnAmt"]
      """  The Depreciation value in the base currency posted to the GL after Revaluation Date.  """  
      self.DocPostedFutrDepnAmt:int = obj["DocPostedFutrDepnAmt"]
      """  The Depreciation value in the documnet currency posted to the GL after Revaluation Date.  """  
      self.Rpt1PostedFutrDepnAmt:int = obj["Rpt1PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt2PostedFutrDepnAmt:int = obj["Rpt2PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt3PostedFutrDepnAmt:int = obj["Rpt3PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.PostedFutrGrantDepnAmt:int = obj["PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the base currency posted to the GL  after Revaluation Date.  """  
      self.DocPostedFutrGrantDepnAmt:int = obj["DocPostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the document currency posted to the GL  after Revaluation Date.  """  
      self.Rpt1PostedFutrGrantDepnAmt:int = obj["Rpt1PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt2PostedFutrGrantDepnAmt:int = obj["Rpt2PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt3PostedFutrGrantDepnAmt:int = obj["Rpt3PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.NewAssetLife:int = obj["NewAssetLife"]
      """  New Estimated Life  """  
      self.NewLifeModifier:str = obj["NewLifeModifier"]
      """  New Life Modifier. Available Values (PERIODS or YEARS)  """  
      self.NewResidualValue:int = obj["NewResidualValue"]
      """  New Residual value of the asset in base currency. By default it is equaled current value.  """  
      self.DocNewResidualValue:int = obj["DocNewResidualValue"]
      """  New Residual value of the asset in document currency. By default it is equaled current value.  """  
      self.Rpt1NewResidualValue:int = obj["Rpt1NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.Rpt2NewResidualValue:int = obj["Rpt2NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.Rpt3NewResidualValue:int = obj["Rpt3NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision Identifier for this row. It is incremented upon oach write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Uniquue identifier for this row. The value is a GUID.  """  
      self.DepOnDisposal:int = obj["DepOnDisposal"]
      """  Value of Depreciation on Disposal/Revaluation setting of the asset, that was used to create the Revaluation.  """  
      self.OrigCurrPerDepn:int = obj["OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation.  """  
      self.DocOrigCurrPerDepn:int = obj["DocOrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in document currency.  """  
      self.Rpt1OrigCurrPerDepn:int = obj["Rpt1OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt2OrigCurrPerDepn:int = obj["Rpt2OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt3OrigCurrPerDepn:int = obj["Rpt3OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.OrigCurrPerGrantDepn:int = obj["OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation.  """  
      self.DocOrigCurrPerGrantDepn:int = obj["DocOrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in document currency.  """  
      self.Rpt1OrigCurrPerGrantDepn:int = obj["Rpt1OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt2OrigCurrPerGrantDepn:int = obj["Rpt2OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt3OrigCurrPerGrantDepn:int = obj["Rpt3OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocNewBookValue:int = obj["DocNewBookValue"]
      self.NewBookValue:int = obj["NewBookValue"]
      self.Rpt1NewBookValue:int = obj["Rpt1NewBookValue"]
      self.Rpt2NewBookValue:int = obj["Rpt2NewBookValue"]
      self.Rpt3NewBookValue:int = obj["Rpt3NewBookValue"]
      self.BitFlag:int = obj["BitFlag"]
      self.FARevalueReadyToPost:bool = obj["FARevalueReadyToPost"]
      self.FARevaluePostedBy:str = obj["FARevaluePostedBy"]
      self.FARevalueDocNewBookValue:int = obj["FARevalueDocNewBookValue"]
      self.FARevaluePosted:bool = obj["FARevaluePosted"]
      self.FARevalueRpt3NewBookValue:int = obj["FARevalueRpt3NewBookValue"]
      self.FARevalueDescription:str = obj["FARevalueDescription"]
      self.FARevaluePostDate:str = obj["FARevaluePostDate"]
      self.FARevalueNewBookValue:int = obj["FARevalueNewBookValue"]
      self.FARevalueCurrencyCode:str = obj["FARevalueCurrencyCode"]
      self.FARevalueValuationDate:str = obj["FARevalueValuationDate"]
      self.FARevalueApplyDate:str = obj["FARevalueApplyDate"]
      self.FARevalueRpt2NewBookValue:int = obj["FARevalueRpt2NewBookValue"]
      self.FARevalueRpt1NewBookValue:int = obj["FARevalueRpt1NewBookValue"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   assetNum
   revalueNum
   assetRegID
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.revalueNum:int = obj["revalueNum"]
      self.assetRegID:str = obj["assetRegID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FARevalueRegListRow:
   def __init__(self, obj):
      self.AssetNum:str = obj["AssetNum"]
      """  Asset Number  """  
      self.RevalueNum:int = obj["RevalueNum"]
      """  Unique number to identify the Revaluation activity of an asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Uniquue identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FARevalueRegSearchListTableset:
   def __init__(self, obj):
      self.FARevalueRegList:list[Erp_Tablesets_FARevalueRegListRow] = obj["FARevalueRegList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FARevalueRegSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset Number  """  
      self.RevalueNum:int = obj["RevalueNum"]
      """  Unique number to identify the Revaluation activity of an asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.OrigCurrentCost:int = obj["OrigCurrentCost"]
      """  The original Current Asset Cost in base currency before running the Asset Revaluation process.  """  
      self.DocOrigCurrentCost:int = obj["DocOrigCurrentCost"]
      """  The original Current Asset Cost in document currency before running the Asset Revaluation process.  """  
      self.Rpt1OrigCurrentCost:int = obj["Rpt1OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.Rpt2OrigCurrentCost:int = obj["Rpt2OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.Rpt3OrigCurrentCost:int = obj["Rpt3OrigCurrentCost"]
      """  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  """  
      self.OrigBookValue:int = obj["OrigBookValue"]
      """  Book Value before revaluation in base currency.  """  
      self.DocOrigBookValue:int = obj["DocOrigBookValue"]
      """  Book Value before revaluation in document currency.  """  
      self.Rpt1OrigBookValue:int = obj["Rpt1OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.Rpt2OrigBookValue:int = obj["Rpt2OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.Rpt3OrigBookValue:int = obj["Rpt3OrigBookValue"]
      """  Book Value before revaluation in reporting currency.  """  
      self.OrigTotalDepn:int = obj["OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in base curreny.  """  
      self.DocOrigTotalDepn:int = obj["DocOrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in document curreny.  """  
      self.Rpt1OrigTotalDepn:int = obj["Rpt1OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.Rpt2OrigTotalDepn:int = obj["Rpt2OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.Rpt3OrigTotalDepn:int = obj["Rpt3OrigTotalDepn"]
      """  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  """  
      self.RevalueGainLoss:int = obj["RevalueGainLoss"]
      """  Revaluation Gain or Loss in base currency. The difference between Original Book Value and New Book Value  """  
      self.DocRevalueGainLoss:int = obj["DocRevalueGainLoss"]
      """  Revaluation Gain or Loss in document currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt1RevalueGainLoss:int = obj["Rpt1RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt2RevalueGainLoss:int = obj["Rpt2RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.Rpt3RevalueGainLoss:int = obj["Rpt3RevalueGainLoss"]
      """  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  """  
      self.RevalueSurplus:int = obj["RevalueSurplus"]
      """  Revaluation Surplus in base currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.DocRevalueSurplus:int = obj["DocRevalueSurplus"]
      """  Revaluation Surplus in document currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt1RevalueSurplus:int = obj["Rpt1RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt2RevalueSurplus:int = obj["Rpt2RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.Rpt3RevalueSurplus:int = obj["Rpt3RevalueSurplus"]
      """  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in base currency.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in document currency.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.GrantDepnAmt:int = obj["GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in base currency.  """  
      self.DocGrantDepnAmt:int = obj["DocGrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in document currency.  """  
      self.Rpt1GrantDepnAmt:int = obj["Rpt1GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt2GrantDepnAmt:int = obj["Rpt2GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.Rpt3GrantDepnAmt:int = obj["Rpt3GrantDepnAmt"]
      """  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  """  
      self.UnusedGrantAmt:int = obj["UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in base currency.  """  
      self.DocUnusedGrantAmt:int = obj["DocUnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in document currency.  """  
      self.Rpt1UnusedGrantAmt:int = obj["Rpt1UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.Rpt2UnusedGrantAmt:int = obj["Rpt2UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.Rpt3UnusedGrantAmt:int = obj["Rpt3UnusedGrantAmt"]
      """  Grant Book Value at the moment of revaluation in reporting currency.  """  
      self.PostedFutrDepnAmt:int = obj["PostedFutrDepnAmt"]
      """  The Depreciation value in the base currency posted to the GL after Revaluation Date.  """  
      self.DocPostedFutrDepnAmt:int = obj["DocPostedFutrDepnAmt"]
      """  The Depreciation value in the documnet currency posted to the GL after Revaluation Date.  """  
      self.Rpt1PostedFutrDepnAmt:int = obj["Rpt1PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt2PostedFutrDepnAmt:int = obj["Rpt2PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt3PostedFutrDepnAmt:int = obj["Rpt3PostedFutrDepnAmt"]
      """  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.PostedFutrGrantDepnAmt:int = obj["PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the base currency posted to the GL  after Revaluation Date.  """  
      self.DocPostedFutrGrantDepnAmt:int = obj["DocPostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the document currency posted to the GL  after Revaluation Date.  """  
      self.Rpt1PostedFutrGrantDepnAmt:int = obj["Rpt1PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt2PostedFutrGrantDepnAmt:int = obj["Rpt2PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.Rpt3PostedFutrGrantDepnAmt:int = obj["Rpt3PostedFutrGrantDepnAmt"]
      """  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  """  
      self.NewAssetLife:int = obj["NewAssetLife"]
      """  New Estimated Life  """  
      self.NewLifeModifier:str = obj["NewLifeModifier"]
      """  New Life Modifier. Available Values (PERIODS or YEARS)  """  
      self.NewResidualValue:int = obj["NewResidualValue"]
      """  New Residual value of the asset in base currency. By default it is equaled current value.  """  
      self.DocNewResidualValue:int = obj["DocNewResidualValue"]
      """  New Residual value of the asset in document currency. By default it is equaled current value.  """  
      self.Rpt1NewResidualValue:int = obj["Rpt1NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.Rpt2NewResidualValue:int = obj["Rpt2NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.Rpt3NewResidualValue:int = obj["Rpt3NewResidualValue"]
      """  New Residual value of the asset in reporting currency. By default it is equaled current value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision Identifier for this row. It is incremented upon oach write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Uniquue identifier for this row. The value is a GUID.  """  
      self.DepOnDisposal:int = obj["DepOnDisposal"]
      """  Value of Depreciation on Disposal/Revaluation setting of the asset, that was used to create the Revaluation.  """  
      self.OrigCurrPerDepn:int = obj["OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation.  """  
      self.DocOrigCurrPerDepn:int = obj["DocOrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in document currency.  """  
      self.Rpt1OrigCurrPerDepn:int = obj["Rpt1OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt2OrigCurrPerDepn:int = obj["Rpt2OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt3OrigCurrPerDepn:int = obj["Rpt3OrigCurrPerDepn"]
      """  Accumulated depreciation in the period of revaluation in reporting currency.  """  
      self.OrigCurrPerGrantDepn:int = obj["OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation.  """  
      self.DocOrigCurrPerGrantDepn:int = obj["DocOrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in document currency.  """  
      self.Rpt1OrigCurrPerGrantDepn:int = obj["Rpt1OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt2OrigCurrPerGrantDepn:int = obj["Rpt2OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.Rpt3OrigCurrPerGrantDepn:int = obj["Rpt3OrigCurrPerGrantDepn"]
      """  Accumulated grant depreciation in the period of revaluation in reporting currency.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocNewBookValue:int = obj["DocNewBookValue"]
      self.NewBookValue:int = obj["NewBookValue"]
      self.Rpt1NewBookValue:int = obj["Rpt1NewBookValue"]
      self.Rpt2NewBookValue:int = obj["Rpt2NewBookValue"]
      self.Rpt3NewBookValue:int = obj["Rpt3NewBookValue"]
      self.BitFlag:int = obj["BitFlag"]
      self.FARevalueReadyToPost:bool = obj["FARevalueReadyToPost"]
      self.FARevaluePostedBy:str = obj["FARevaluePostedBy"]
      self.FARevalueDocNewBookValue:int = obj["FARevalueDocNewBookValue"]
      self.FARevaluePosted:bool = obj["FARevaluePosted"]
      self.FARevalueRpt3NewBookValue:int = obj["FARevalueRpt3NewBookValue"]
      self.FARevalueDescription:str = obj["FARevalueDescription"]
      self.FARevaluePostDate:str = obj["FARevaluePostDate"]
      self.FARevalueNewBookValue:int = obj["FARevalueNewBookValue"]
      self.FARevalueCurrencyCode:str = obj["FARevalueCurrencyCode"]
      self.FARevalueValuationDate:str = obj["FARevalueValuationDate"]
      self.FARevalueApplyDate:str = obj["FARevalueApplyDate"]
      self.FARevalueRpt2NewBookValue:int = obj["FARevalueRpt2NewBookValue"]
      self.FARevalueRpt1NewBookValue:int = obj["FARevalueRpt1NewBookValue"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FARevalueRegSearchTableset:
   def __init__(self, obj):
      self.FARevalueRegSearch:list[Erp_Tablesets_FARevalueRegSearchRow] = obj["FARevalueRegSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtFARevalueRegSearchTableset:
   def __init__(self, obj):
      self.FARevalueRegSearch:list[Erp_Tablesets_FARevalueRegSearchRow] = obj["FARevalueRegSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   assetNum
   revalueNum
   assetRegID
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.revalueNum:int = obj["revalueNum"]
      self.assetRegID:str = obj["assetRegID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FARevalueRegSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FARevalueRegSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FARevalueRegSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FARevalueRegSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFARevalueRegSearch_input:
   """ Required : 
   ds
   assetNum
   revalueNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueRegSearchTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      self.revalueNum:int = obj["revalueNum"]
      pass

class GetNewFARevalueRegSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueRegSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFARevalueRegSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFARevalueRegSearch:str = obj["whereClauseFARevalueRegSearch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FARevalueRegSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtFARevalueRegSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFARevalueRegSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueRegSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FARevalueRegSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

